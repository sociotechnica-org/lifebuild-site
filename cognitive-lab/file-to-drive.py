#!/usr/bin/env python3
"""
file-to-drive.py — agent-callable CLI for filing documents into the
Cognitive Lab's four Drive holding-pen folders, and updating their
manifests so the lab can render them.

Behavior:
  python3 file-to-drive.py --area research|journal|explainer
                           --title "..."
                           --content-file PATH
                           --format md|gdoc|pdf|docx|html|txt
                           [--date YYYY-MM-DD]
                           [--summary "..."]
                           [--tags tag1,tag2]
                           [--update-id <driveFileId>]
                           [--no-manifest]

  Prints the resulting Drive URL on stdout (one line).
  Non-zero exit code on any failure (with a message on stderr).
  If the Drive write succeeds but the manifest write fails, the URL
  still prints; only the manifest error is reported on stderr and the
  process exits non-zero so the caller can retry the manifest update.

Modes:
  Create (default): uploads the content as a NEW Drive file in the area
    folder. If --update-id is omitted this is what runs.
  Update (--update-id): overwrites the content of an existing Drive
    file in place. Drive keeps its own version history; the lab
    continues to point at the same canonical file. Title is also
    updated if --title is passed.

Manifests:
  Each area writes to <script-dir>/exports/<area>-manifest.json — a
  list of entries, one per Drive file. New filings append; updates
  refresh the matching entry by driveId. Atomic writes only.

Auth:
  - First run requires an OAuth client at
    ~/.config/cognitive-lab/credentials.json
    (downloaded from Google Cloud Console as a Desktop OAuth client).
  - Browser opens once for consent. Token caches at
    ~/.config/cognitive-lab/token.json. Refreshed silently after.

Folder IDs are hard-coded — these were created during the cognitive
lab's Drive setup and shouldn't move. If a folder is renamed in Drive
the IDs still resolve.

Usage:
  python3 file-to-drive.py --help
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]

CONFIG_DIR = Path.home() / ".config" / "cognitive-lab"
CREDENTIALS_PATH = CONFIG_DIR / "credentials.json"
TOKEN_PATH = CONFIG_DIR / "token.json"

AREA_FOLDERS = {
    "research":  "1PniRQqXbOGSPom17VW2a20dDosSVOLR1",
    "journal":   "1xtdbKRy1SG42wVegT_uM94MY-LB8IJZW",
    "explainer": "1_uPvHyY0yAgCZnMyD9bdwyTIBM_Ox7EO",
    "strategy":  "1YNuePt3ccfIxpZRipwmqnRZcQ5-I83jx",
}

# format → (upload mime type, convert to Google native type)
FORMAT_SPEC = {
    "md":   ("text/markdown", False),
    "gdoc": ("text/plain",    True),
    "pdf":  ("application/pdf", False),
    "docx": (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        False,
    ),
    "html": ("text/html",  False),
    "txt":  ("text/plain", False),
}

SCRIPT_DIR = Path(__file__).resolve().parent
EXPORTS_DIR = SCRIPT_DIR / "exports"


def die(msg: str, code: int = 1) -> None:
    print(f"file-to-drive: error: {msg}", file=sys.stderr)
    sys.exit(code)


def warn(msg: str) -> None:
    print(f"file-to-drive: warning: {msg}", file=sys.stderr)


def get_credentials() -> Credentials:
    if not CREDENTIALS_PATH.exists():
        die(
            f"missing OAuth client at {CREDENTIALS_PATH}. "
            "Create one in Google Cloud Console "
            "(Credentials → OAuth client ID → Desktop app), "
            "download the JSON, save it at that path."
        )

    creds: Credentials | None = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_PATH), SCOPES
            )
            creds = flow.run_local_server(port=0)
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        TOKEN_PATH.write_text(creds.to_json())

    return creds


def drive_create(service, area: str, title: str, content_file: Path,
                 fmt: str) -> dict:
    upload_mime, convert = FORMAT_SPEC[fmt]
    metadata: dict = {"name": title, "parents": [AREA_FOLDERS[area]]}
    if convert:
        metadata["mimeType"] = "application/vnd.google-apps.document"

    media = MediaFileUpload(str(content_file), mimetype=upload_mime,
                            resumable=False)
    return (
        service.files()
        .create(body=metadata, media_body=media, fields="id, webViewLink")
        .execute()
    )


def drive_update(service, file_id: str, title: str | None,
                 content_file: Path, fmt: str) -> dict:
    upload_mime, _ = FORMAT_SPEC[fmt]
    body: dict = {}
    if title:
        body["name"] = title

    media = MediaFileUpload(str(content_file), mimetype=upload_mime,
                            resumable=False)
    return (
        service.files()
        .update(fileId=file_id, body=body, media_body=media,
                fields="id, webViewLink")
        .execute()
    )


def manifest_path(area: str) -> Path:
    return EXPORTS_DIR / f"{area}-manifest.json"


def read_manifest(area: str) -> list[dict]:
    p = manifest_path(area)
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text())
        if not isinstance(data, list):
            raise ValueError(f"manifest is not a JSON array: {p}")
        return data
    except (json.JSONDecodeError, ValueError) as e:
        die(f"corrupt manifest at {p}: {e}. Refusing to overwrite.")


def write_manifest_atomic(area: str, entries: list[dict]) -> Path:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    target = manifest_path(area)
    fd, tmpname = tempfile.mkstemp(prefix=f"{area}-manifest.", suffix=".json",
                                   dir=str(EXPORTS_DIR))
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmpname, target)
    except Exception:
        if os.path.exists(tmpname):
            os.unlink(tmpname)
        raise
    return target


def upsert_manifest_entry(area: str, entry: dict, *,
                          is_update: bool) -> Path:
    """Append a new entry, or refresh an existing entry matched by driveId."""
    entries = read_manifest(area)
    if is_update:
        matched = False
        for i, existing in enumerate(entries):
            if existing.get("driveId") == entry["driveId"]:
                # Refresh in place. Preserve any caller-omitted fields.
                merged = {**existing, **entry}
                entries[i] = merged
                matched = True
                break
        if not matched:
            # File existed in Drive but not in manifest — append it now.
            entries.append(entry)
    else:
        entries.append(entry)
    return write_manifest_atomic(area, entries)


def parse_date(raw: str | None) -> str:
    if raw is None:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        datetime.strptime(raw, "%Y-%m-%d")
    except ValueError:
        die(f"--date must be YYYY-MM-DD, got: {raw}")
    return raw


def parse_tags(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [t.strip() for t in raw.split(",") if t.strip()]


def main() -> None:
    p = argparse.ArgumentParser(
        description=(
            "File a document into a Cognitive Lab Drive folder, "
            "updating the area's manifest."
        ),
    )
    p.add_argument(
        "--area", required=True, choices=list(AREA_FOLDERS),
        help="Holding-pen folder to file into.",
    )
    p.add_argument("--title", help="File title in Drive. Required for create; optional for update.")
    p.add_argument(
        "--content-file", required=True,
        help="Path to the local file to upload.",
    )
    p.add_argument(
        "--format", required=True, choices=list(FORMAT_SPEC),
        dest="fmt", help="Upload format / conversion behavior.",
    )
    p.add_argument(
        "--date", default=None,
        help="YYYY-MM-DD. Date the entry sorts under in the lab. Defaults to today (UTC).",
    )
    p.add_argument(
        "--summary", default="",
        help="1–3 sentence agent-written summary for the lab to render.",
    )
    p.add_argument(
        "--tags", default="",
        help="Comma-separated tags. Used by lab grouping/filtering.",
    )
    p.add_argument(
        "--update-id", default=None,
        help="Drive file ID. If set, overwrite content of this file in place "
             "(instead of creating new). Drive keeps version history.",
    )
    p.add_argument(
        "--no-manifest", action="store_true",
        help="Skip the manifest write side effect. Use for dry runs / one-offs.",
    )
    args = p.parse_args()

    is_update = bool(args.update_id)
    if not is_update and not args.title:
        die("--title is required when creating a new file (use --update-id to update an existing file without renaming)")

    cf = Path(args.content_file)
    if not cf.exists() or not cf.is_file():
        die(f"content file not found or not a file: {cf}")

    date = parse_date(args.date)
    tags = parse_tags(args.tags)

    creds = get_credentials()
    service = build("drive", "v3", credentials=creds, cache_discovery=False)

    try:
        if is_update:
            response = drive_update(service, args.update_id, args.title, cf, args.fmt)
        else:
            response = drive_create(service, args.area, args.title, cf, args.fmt)
    except HttpError as e:
        die(f"Drive API error: {e}")
    except Exception as e:  # noqa: BLE001
        die(f"upload failed: {e}")

    file_id = response["id"]
    url = response.get("webViewLink") or f"https://drive.google.com/file/d/{file_id}"
    print(url)

    if args.no_manifest:
        return

    entry = {
        "date":     date,
        "title":    args.title or "",  # may be empty on update without rename
        "driveUrl": url,
        "driveId":  file_id,
        "format":   args.fmt,
        "summary":  args.summary,
        "tags":     tags,
        "filedAt":  datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    # Drop the title from the merge if blank-on-update so we don't blank
    # out the existing entry's title.
    if is_update and not args.title:
        entry.pop("title", None)

    try:
        path = upsert_manifest_entry(args.area, entry, is_update=is_update)
    except Exception as e:  # noqa: BLE001
        warn(f"manifest write failed (Drive write succeeded): {e}")
        sys.exit(2)

    print(f"manifest: {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
