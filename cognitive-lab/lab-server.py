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

Usage:
  python3 cognitive-lab/lab-server.py [PORT]
  PORT defaults to 4322.
"""

from __future__ import annotations

import json
import os
import sys
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
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
                f.write("\n")
            os.replace(tmp, target)
        except OSError as e:
            self._json_error(500, f"write failed: {e}")
            return

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

    addr = ("127.0.0.1", port)
    httpd = HTTPServer(addr, LabRequestHandler)
    url = f"http://{addr[0]}:{addr[1]}/cognitive-lab-v0.1.html"
    print(f"[lab-server] serving {ROOT}")
    print(f"[lab-server] exports → {EXPORTS_DIR}")
    print(f"[lab-server] open    → {url}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[lab-server] shutting down")
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
