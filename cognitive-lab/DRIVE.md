# Drive filing — cognitive lab holding pens

`file-to-drive.py` is the agent-callable CLI for filing documents into the
lab's Drive folders. It exists because the Claude.ai Drive MCP can
create files at root but cannot write into specific folders, which breaks
the holding-pen pattern.

Folder targets (already created in Drive):

| `--area`        | Drive folder        |
| --------------- | ------------------- |
| `research`      | Research Repository |
| `journal`       | Daily Journal       |
| `explainer`     | Explainer Theater   |
| `strategy`      | Strategy & Plans    |
| `director-desk` | Director's Desk (pending-room — staged for a future Band-1 surface) |

## Setup (one-time, ~5 min)

1. https://console.cloud.google.com → create project "Cognitive Lab Personal"
2. APIs & Services → Library → enable **Google Drive API**
3. APIs & Services → OAuth consent screen → External; add your email as a
   test user (skips the verification queue)
4. APIs & Services → Credentials → Create Credentials → OAuth client ID →
   **Desktop app**
5. Download the JSON → save as `~/.config/cognitive-lab/credentials.json`
6. Install Python deps:

   ```bash
   cd cognitive-lab
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## First run

```bash
echo "first journal entry" > /tmp/entry.md
python3 file-to-drive.py \
  --area journal \
  --title "2026-05-09 — first edition" \
  --content-file /tmp/entry.md \
  --format md
```

A browser opens once. Consent. The token caches at
`~/.config/cognitive-lab/token.json` and is refreshed silently after.

The script prints the Drive URL on stdout, exits non-zero on failure.

## Modes

**Create** (default) — uploads the content as a new Drive file in the
area folder, appends an entry to the area's manifest.

**Update** (`--update-id <driveFileId>`) — overwrites the content of an
existing Drive file in place. Drive keeps the prior versions in its own
File → Version history. The lab continues to point at the same file.
The matching manifest entry is refreshed (not duplicated). If
`--title` is provided in update mode, the file is also renamed.

```bash
# Update an existing file's content (and optionally its title)
python3 file-to-drive.py \
  --area explainer \
  --content-file ./investor-2pager-v2.pdf \
  --format pdf \
  --update-id 1abc...XYZ \
  --summary "v2 — added the funding ask section."
```

## Optional flags

| Flag             | Purpose                                                   |
| ---------------- | --------------------------------------------------------- |
| `--date YYYY-MM-DD` | Date the entry sorts under in the lab. Default: today UTC. Backdating is fully supported. |
| `--summary "..."`  | 1–3 sentence agent-written note. Lab renders this under the entry's title. |
| `--tags a,b,c`   | Comma-separated tags. Used for lab grouping/filtering.    |
| `--update-id <id>` | Update existing file instead of creating new (see above). |
| `--no-manifest`  | Skip the manifest write side effect. Drive write still happens. |

## Manifests

Each area writes a manifest at `cognitive-lab/exports/<area>-manifest.json`
— a JSON array of entries, one per Drive file. The lab reads the manifest
to render the area's drawer (Editions / Reports / Explainers shelves).

Per-entry fields:

```json
{
  "date":     "2026-05-09",
  "title":    "first edition",
  "driveUrl": "https://drive.google.com/file/d/.../view",
  "driveId":  "1d2Wz7NW0PjYllbZxKAGrXuMFihsdRFGn",
  "format":   "md",
  "summary":  "Top row renamed; Drive holding pens wired.",
  "tags":     ["lab-cleanup", "drive"],
  "filedAt":  "2026-05-09T15:51:00Z"
}
```

`date` vs `filedAt`: `date` is what the entry *belongs to* in the lab's
view (sortable, backdate-able). `filedAt` is when the script ran (audit
trail). They can differ — a 2026-05-04 research report filed today
sorts under 5/4 but logs 5/9 as the moment it entered the system.

If the Drive write succeeds but the manifest write fails, the URL still
prints to stdout. The error appears on stderr and the process exits
with code `2` so the caller can retry the manifest update.

## Formats

| `--format` | Upload type       | Drive result          |
| ---------- | ----------------- | --------------------- |
| `md`       | `text/markdown`   | `.md` file            |
| `gdoc`     | `text/plain`      | Google Doc (auto-convert) |
| `pdf`      | `application/pdf` | PDF                   |
| `docx`     | docx mime         | Word doc              |
| `html`     | `text/html`       | `.html` file          |
| `txt`      | `text/plain`      | plain `.txt`          |

For things that benefit from version history (drafts, evolving 2-pagers),
prefer `gdoc` — Google Docs has built-in versioning and works with the
`--update-id` flow seamlessly.

## Secrets

`credentials.json` and `token.json` live at `~/.config/cognitive-lab/`,
outside the repo. Never check them in.

## Scope

`file-to-drive.py` is the **generic write path** for filing whole
documents into one of the holding-pen folders. Reads / search /
browse happen in Drive's own UI. The lab itself stays a static HTML
viewer that imports exports as needed.

For the Daily Journal's three shelves (Scratchpad, Decision Log,
Editions), `file-to-drive.py` handles Editions but Scratchpad and
Decision Log have their own append-style CLIs — see below.

---

# Journal entry-add CLIs

The Daily Journal's Scratchpad and Decision Log shelves are
Drive-canonical, with one dated md file per day per shelf. Two small
CLIs append entries to today's docs (creating the dated doc on first
use of the day):

## scratchpad-add.py

```bash
python3 cognitive-lab/scratchpad-add.py \
  "Three rooms of the lab need filing — could be agentic." \
  --tags lab-cleanup,filing
```

Behavior:
- Looks up today's scratchpad doc in `journal-manifest.json`
  (matched on `shelf="scratchpad"` + today's local date).
- If found: fetches current content via Drive API, appends the new
  entry with timestamp + tags, uploads via `--update-id` semantics.
  Drive keeps the per-edit revision history.
- If not: creates a new dated md doc (`<date> — scratchpad`),
  populates with the entry as first content, appends a manifest
  entry with `shelf="scratchpad"`.

Prints the Drive URL on stdout. Subsequent same-day calls return the
same URL (same doc, appended).

## decision-log-add.py

```bash
python3 cognitive-lab/decision-log-add.py \
  "Backlog Wall retired; status views replace it." \
  --why "Item-area anchoring + toolbar views provide same coverage with less surface." \
  --by "Dan + Claude (PR #134 design)" \
  --link "https://github.com/sociotechnica-org/lifebuild-site/pull/134" \
  --tags architecture
```

Same behavior as `scratchpad-add.py`, but writes to the decision-log
shelf with structured fields (Why / By / Links). `--link` is
repeatable.

## Manifest schema — `shelf` discriminator

Journal manifest entries gain a `shelf` field with values
`"edition" | "scratchpad" | "decisionLog"`. Lab UI filters by `shelf`
to render each tab. Pre-existing entries without `shelf` are legacy
(filed before this convention) and should be treated as `"edition"`
or backfilled as needed.
