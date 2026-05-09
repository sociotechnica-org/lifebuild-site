#!/usr/bin/env python3
"""
lab-server.py — local dev server for the cognitive lab.

Behavior:
  GET  /...                       static file serve (rooted at this script's dir)
  POST /api/save/frame-cards      body = JSON array, written to exports/frame-cards.json
  POST /api/save/debrief-cards    body = JSON array, written to exports/debrief-cards.json
  POST /api/save/pilot-checks     body = JSON array, written to exports/pilot-checks.json
  POST /api/save/courses          body = JSON array, written to exports/courses.json
  POST /api/save/legs             body = JSON array, written to exports/legs.json

Notes:
  - .md/.txt are served as text/plain so links open in a tab instead of downloading.
  - Writes are atomic: tmpfile + os.replace. Avoids partial-file corruption on crash.
  - Allowlist on the save type — no arbitrary paths.
  - Bind to 127.0.0.1 only. Local dev tool, not production.

  - **Drive mirror (optional).** After each successful local atomic
    write, the saved JSON is mirrored to a single Google Doc per card
    type in the `Cognitive Lab / Workshop Cards / ` Drive folder. The
    local file remains canonical for fast read; Drive is a durable
    backup. If the google-api-python-client deps aren't available
    (i.e., the venv with file-to-drive.py's deps isn't active), the
    mirror is silently skipped — local saves still succeed.

Usage:
  python3 cognitive-lab/lab-server.py [PORT]
  PORT defaults to 4322.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
import threading
from datetime import datetime, timezone
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPORTS_DIR = ROOT / "exports"

ALLOWED_TYPES = {
    "frame-cards":   "frame-cards.json",
    "debrief-cards": "debrief-cards.json",
    "pilot-checks":  "pilot-checks.json",
    "courses":       "courses.json",
    "legs":          "legs.json",
}

DEFAULT_PORT = 4322
MAX_BODY_BYTES = 5 * 1024 * 1024  # 5 MB; lab data is small

# ── Drive mirror config ──────────────────────────────────────────────
WORKSHOP_CARDS_FOLDER_ID = "1kt9Fxxuwb-MK9bnHdmrcpi8JDWSOSd1w"
WORKSHOP_CARDS_MANIFEST = EXPORTS_DIR / "workshop-cards-manifest.json"
WORKSHOP_CARDS_TITLE_FMT = "{save_type}.json"

# Try to load file-to-drive.py for the OAuth + Drive helpers. If the
# deps aren't available (e.g., the venv with google-api-python-client
# isn't active), mirror is disabled — local saves still work fine.
_DRIVE_MIRROR_LOCK = threading.Lock()
_drive_mirror_enabled = False
_drive_mirror_creds_present = False
_drive_mirror_disabled_reason = None  # set if a session-level error should block writes
_ftd = None
_drive_service = None

def _try_init_drive_mirror():
    """Best-effort init of the Drive mirror. Silent on failure."""
    global _drive_mirror_enabled, _drive_mirror_creds_present, _ftd, _drive_service
    try:
        spec = importlib.util.spec_from_file_location(
            "file_to_drive", str(ROOT / "file-to-drive.py")
        )
        ftd = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ftd)
        from googleapiclient.discovery import build  # noqa: F401
        # Don't actually authenticate yet — just verify deps load. Auth happens
        # on first mirror call.
        _ftd = ftd
        _drive_mirror_enabled = True
        # Probe whether OAuth creds exist so we can report accurately at boot
        # without triggering an interactive auth flow.
        _drive_mirror_creds_present = ftd.CREDENTIALS_PATH.exists()
    except Exception as e:  # noqa: BLE001
        # Could be missing google-api-python-client, missing creds file,
        # or anything else. Disable mirror; local saves still work.
        sys.stderr.write(
            f"[lab-server] Drive mirror disabled ({type(e).__name__}); "
            "local saves only.\n"
        )

def _build_drive_service():
    """Build (or reuse) a Drive service. Returns None on auth failure."""
    global _drive_service
    if _drive_service is not None:
        return _drive_service
    try:
        from googleapiclient.discovery import build
        creds = _ftd.get_credentials()
        _drive_service = build("drive", "v3", credentials=creds, cache_discovery=False)
        return _drive_service
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"[lab-server] Drive auth failed: {e}\n")
        return None

class WorkshopManifestUnreadable(Exception):
    """Raised when the workshop-cards manifest exists but can't be parsed.
    Distinct from "manifest missing" (which is normal on first run)."""

def _read_workshop_manifest() -> dict:
    """Workshop-cards manifest is a flat dict: {save_type: {driveId, ...}, ...}.

    Returns {} only when the manifest file does not exist (first-run / fresh
    machine). If the file exists but can't be parsed, raises
    WorkshopManifestUnreadable — the caller decides how to recover. Silently
    falling back to {} would strand existing Drive docs and start a fresh
    duplicate lineage."""
    if not WORKSHOP_CARDS_MANIFEST.exists():
        return {}
    try:
        data = json.loads(WORKSHOP_CARDS_MANIFEST.read_text())
    except (json.JSONDecodeError, OSError) as e:
        raise WorkshopManifestUnreadable(
            f"manifest at {WORKSHOP_CARDS_MANIFEST} exists but is not parseable: {e}"
        ) from e
    if not isinstance(data, dict):
        raise WorkshopManifestUnreadable(
            f"manifest at {WORKSHOP_CARDS_MANIFEST} is not a JSON object"
        )
    return data

def _write_workshop_manifest_atomic(manifest: dict) -> None:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmpname = tempfile.mkstemp(
        prefix="workshop-cards-manifest.", suffix=".json", dir=str(EXPORTS_DIR)
    )
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmpname, str(WORKSHOP_CARDS_MANIFEST))
    except Exception:
        if os.path.exists(tmpname):
            os.unlink(tmpname)
        raise

def _mirror_to_drive(save_type: str, content_text: str) -> None:
    """Best-effort mirror of a workshop-card save to Drive.

    Single Drive doc per save_type. First save creates the doc; later
    saves overwrite content via files().update(). Drive's revision
    history captures the change history. Failures log to stderr but
    don't break the local save.

    Runs on a background thread (caller in do_POST starts it daemon-style),
    so the POST response isn't blocked by Drive latency.
    """
    global _drive_mirror_disabled_reason
    if not _drive_mirror_enabled:
        return
    if _drive_mirror_disabled_reason is not None:
        # A prior call hit a session-killing error (e.g., unreadable manifest).
        # Refuse to create docs that would orphan existing ones.
        sys.stderr.write(
            f"[lab-server] mirror skipped ({save_type}): {_drive_mirror_disabled_reason}\n"
        )
        return
    with _DRIVE_MIRROR_LOCK:
        try:
            service = _build_drive_service()
            if service is None:
                return

            from googleapiclient.http import MediaFileUpload

            try:
                manifest = _read_workshop_manifest()
            except WorkshopManifestUnreadable as e:
                # Disable mirror for this session — refuse to create new docs
                # that would silently strand whatever Drive docs the manifest
                # used to point at. User must investigate manually.
                _drive_mirror_disabled_reason = str(e)
                sys.stderr.write(
                    f"[lab-server] mirror DISABLED for this session: {e}. "
                    "Restart after fixing the manifest, or delete it to "
                    "force fresh-doc creation.\n"
                )
                return
            entry = manifest.get(save_type)

            # Write content to a temp file for MediaFileUpload.
            with tempfile.NamedTemporaryFile(
                "w", suffix=".json", delete=False, encoding="utf-8"
            ) as f:
                f.write(content_text)
                tmppath = f.name

            try:
                if entry and entry.get("driveId"):
                    # Update existing doc — overwrites content; Drive keeps version history.
                    media = MediaFileUpload(tmppath, mimetype="text/plain", resumable=False)
                    response = service.files().update(
                        fileId=entry["driveId"],
                        media_body=media,
                        fields="id, webViewLink",
                    ).execute()
                else:
                    # Create new Drive doc for this save_type.
                    title = WORKSHOP_CARDS_TITLE_FMT.format(save_type=save_type)
                    metadata = {
                        "name": title,
                        "parents": [WORKSHOP_CARDS_FOLDER_ID],
                    }
                    media = MediaFileUpload(tmppath, mimetype="text/plain", resumable=False)
                    response = service.files().create(
                        body=metadata, media_body=media,
                        fields="id, webViewLink",
                    ).execute()

                manifest[save_type] = {
                    "driveId":  response["id"],
                    "driveUrl": response.get("webViewLink") or
                                f"https://drive.google.com/file/d/{response['id']}/view",
                    "format":   "txt",
                    "filedAt":  datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                }
                _write_workshop_manifest_atomic(manifest)
            finally:
                if os.path.exists(tmppath):
                    os.unlink(tmppath)

        except Exception as e:  # noqa: BLE001
            sys.stderr.write(
                f"[lab-server] Drive mirror for {save_type} failed: {e}\n"
            )


class LabRequestHandler(SimpleHTTPRequestHandler):
    """Static serve + tiny POST write API."""

    # Serve from the cognitive-lab dir, regardless of where the user invoked from.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    # Make Markdown/text artifact links open in-tab rather than triggering downloads.
    def guess_type(self, path):  # noqa: N802 (stdlib casing)
        ext = os.path.splitext(path)[1].lower()
        if ext in (".md", ".txt", ""):
            return "text/plain; charset=utf-8"
        return super().guess_type(path)

    # ---- POST routing -------------------------------------------------------

    def do_POST(self):  # noqa: N802 (stdlib casing)
        path = self.path.split("?", 1)[0]
        prefix = "/api/save/"
        if not path.startswith(prefix):
            self._json_error(404, f"unknown POST path: {path}")
            return

        save_type = path[len(prefix):].strip("/")
        if save_type not in ALLOWED_TYPES:
            self._json_error(
                404,
                f"unknown save type '{save_type}'. allowed: {sorted(ALLOWED_TYPES)}",
            )
            return

        # Read and bound the body.
        length_hdr = self.headers.get("Content-Length")
        try:
            length = int(length_hdr) if length_hdr is not None else -1
        except ValueError:
            self._json_error(400, "invalid Content-Length")
            return
        if length < 0:
            self._json_error(411, "Content-Length required")
            return
        if length > MAX_BODY_BYTES:
            self._json_error(413, f"body too large ({length} > {MAX_BODY_BYTES})")
            return

        raw = self.rfile.read(length) if length else b""

        # Parse to validate; we rewrite from the parsed value so we always store
        # canonical JSON (and refuse anything that wouldn't reload cleanly).
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            self._json_error(400, f"invalid JSON: {e}")
            return

        # Per-type shape check: all three are arrays of card/check objects.
        if not isinstance(payload, list):
            self._json_error(400, "expected a JSON array at top level")
            return

        try:
            EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
            target = EXPORTS_DIR / ALLOWED_TYPES[save_type]
            tmp = target.with_suffix(target.suffix + ".tmp")
            content_text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(content_text)
            os.replace(tmp, target)
        except OSError as e:
            self._json_error(500, f"write failed: {e}")
            return

        # Mirror to Drive on a background thread so Drive latency doesn't
        # delay the POST response. Mirror is best-effort; failures log to
        # stderr but don't affect the local save. Gate thread spawn on
        # both "deps loaded" AND "no session-killing error has been seen
        # already" — without this, every save after a manifest-corruption
        # event would spawn a worker that immediately logs "skipped" and
        # exits, polluting stderr.
        if _drive_mirror_enabled and _drive_mirror_disabled_reason is None:
            threading.Thread(
                target=_mirror_to_drive,
                args=(save_type, content_text),
                daemon=True,
            ).start()

        self._json_ok({
            "ok": True,
            "type": save_type,
            "count": len(payload),
            "path": str(target.relative_to(ROOT)),
        })

    # ---- helpers ------------------------------------------------------------

    def _json_ok(self, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        # No-cache so the browser never serves a stale POST response.
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json_error(self, code, message):
        body = json.dumps({"ok": False, "error": message}).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main(argv):
    port = DEFAULT_PORT
    if len(argv) > 1:
        try:
            port = int(argv[1])
        except ValueError:
            print(f"invalid port: {argv[1]}", file=sys.stderr)
            return 2

    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Best-effort init of Drive mirror. Silent on failure (logs once to stderr).
    _try_init_drive_mirror()

    addr = ("127.0.0.1", port)
    httpd = HTTPServer(addr, LabRequestHandler)
    url = f"http://{addr[0]}:{addr[1]}/cognitive-lab-v0.1.html"
    print(f"[lab-server] serving {ROOT}")
    print(f"[lab-server] exports → {EXPORTS_DIR}")
    if _drive_mirror_enabled:
        if _drive_mirror_creds_present:
            print(f"[lab-server] drive mirror → /Cognitive Lab/Workshop Cards/")
        else:
            print(
                f"[lab-server] drive mirror → enabled (auth on first save; "
                f"creds at {_ftd.CREDENTIALS_PATH} not yet present)"
            )
    print(f"[lab-server] open    → {url}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[lab-server] shutting down")
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
