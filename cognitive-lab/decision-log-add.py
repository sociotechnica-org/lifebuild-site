#!/usr/bin/env python3
"""
decision-log-add.py — append a decision to today's decision-log doc in Drive.

The Daily Journal's Decision Log shelf is Drive-canonical: one dated
md file per day, in the Daily Journal Drive folder, indexed by
journal-manifest.json with shelf="decisionLog". This CLI is the
agent-callable + human-callable append.

Behavior:
  python3 decision-log-add.py "<decision>" \
    [--why "..."] [--by "..."] [--link URL] [--tags tag1,tag2]

  - Looks up today's decision-log doc in journal-manifest.json
    (matched on shelf="decisionLog" + today's local date).
  - If found: fetches current content, appends the new decision
    with a timestamp + structured fields, uploads via Drive API.
  - If not: creates a new dated md doc with the decision as first
    content, appends a manifest entry with shelf="decisionLog".

Prints the Drive URL on stdout. Non-zero exit on failure.

Auth:
  Reuses ~/.config/cognitive-lab/credentials.json + token.json — same
  OAuth setup as file-to-drive.py.

Notes:
  - --link can be passed multiple times to attach multiple URLs.
  - Format is `md` (markdown). Round-trip is plain Drive API + the
    shared file-to-drive helpers.
  - "Today" is the operator's local date, not UTC.
"""

from __future__ import annotations

import argparse
import importlib.util
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# Load file-to-drive.py as a module despite the hyphen in its name.
SCRIPT_DIR = Path(__file__).resolve().parent
FTD_PATH = SCRIPT_DIR / "file-to-drive.py"
_spec = importlib.util.spec_from_file_location("file_to_drive", str(FTD_PATH))
ftd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ftd)

from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.errors import HttpError  # noqa: E402

SHELF = "decisionLog"
JOURNAL_AREA = "journal"


def today_local_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_local_time() -> str:
    return datetime.now().strftime("%H:%M")


def utc_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def find_today_entry(date: str) -> dict | None:
    for entry in ftd.read_manifest(JOURNAL_AREA):
        if entry.get("shelf") == SHELF and entry.get("date") == date:
            return entry
    return None


def fetch_md(service, file_id: str) -> str:
    raw = service.files().get_media(fileId=file_id).execute()
    return raw.decode("utf-8") if isinstance(raw, (bytes, bytearray)) else raw


def render_decision(decision: str, why: str, by: str,
                    links: list[str], tags: list[str]) -> str:
    parts = [f"\n## {now_local_time()} — {decision}\n"]
    if why:
        parts.append(f"\n**Why:** {why}\n")
    if by:
        parts.append(f"\n**By:** {by}\n")
    if links:
        parts.append("\n**Links:**\n")
        parts.extend(f"- {url}\n" for url in links)
    if tags:
        parts.append("\n" + " ".join(f"#{t}" for t in tags) + "\n")
    return "".join(parts) + "\n"


def render_doc_header(date: str) -> str:
    return f"# Decision Log — {date}\n"


def upsert_today_entry(decision: str, why: str, by: str,
                       links: list[str], tags: list[str]) -> str:
    creds = ftd.get_credentials()
    service = build("drive", "v3", credentials=creds, cache_discovery=False)

    date = today_local_date()
    title = f"{date} — decision log"
    new_section = render_decision(decision, why, by, links, tags)
    existing = find_today_entry(date)

    if existing:
        try:
            current = fetch_md(service, existing["driveId"])
        except HttpError as e:
            ftd.die(f"failed to fetch existing decision-log doc: {e}")

        new_body = current.rstrip() + "\n" + new_section
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(new_body)
            tmppath = Path(f.name)

        try:
            response = ftd.drive_update(service, existing["driveId"], None, tmppath, "md")
        finally:
            tmppath.unlink(missing_ok=True)

        entries = ftd.read_manifest(JOURNAL_AREA)
        for i, entry in enumerate(entries):
            if entry.get("driveId") == existing["driveId"]:
                merged_tags = sorted(set(entry.get("tags", []) or []) | set(tags))
                entries[i] = {**entry, "tags": merged_tags, "filedAt": utc_iso()}
                break
        ftd.write_manifest_atomic(JOURNAL_AREA, entries)

        return response.get("webViewLink") or f"https://drive.google.com/file/d/{response['id']}/view"

    # No doc for today yet — create it.
    body = render_doc_header(date) + new_section
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(body)
        tmppath = Path(f.name)

    try:
        response = ftd.drive_create(service, JOURNAL_AREA, title, tmppath, "md")
    finally:
        tmppath.unlink(missing_ok=True)

    file_id = response["id"]
    url = response.get("webViewLink") or f"https://drive.google.com/file/d/{file_id}/view"

    new_entry = {
        "shelf":    SHELF,
        "date":     date,
        "title":    title,
        "driveUrl": url,
        "driveId":  file_id,
        "format":   "md",
        "summary":  "",
        "tags":     tags,
        "filedAt":  utc_iso(),
    }
    entries = ftd.read_manifest(JOURNAL_AREA)
    entries.append(new_entry)
    ftd.write_manifest_atomic(JOURNAL_AREA, entries)

    return url


def main() -> None:
    p = argparse.ArgumentParser(
        description="Append a decision to today's decision-log doc in Drive.",
    )
    p.add_argument("decision", help="The decision (one-line summary).")
    p.add_argument("--why", default="", help="Why this decision was made.")
    p.add_argument("--by", default="", help="Who made the decision.")
    p.add_argument(
        "--link", action="append", default=[],
        help="Related URL. Repeatable.",
    )
    p.add_argument("--tags", default="", help="Comma-separated tags.")
    args = p.parse_args()

    decision = args.decision.strip()
    if not decision:
        ftd.die("decision text must be non-empty")

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    try:
        url = upsert_today_entry(decision, args.why.strip(), args.by.strip(),
                                 args.link, tags)
    except HttpError as e:
        ftd.die(f"Drive API error: {e}")
    except Exception as e:  # noqa: BLE001
        ftd.die(f"decision-log-add failed: {e}")

    print(url)


if __name__ == "__main__":
    main()
