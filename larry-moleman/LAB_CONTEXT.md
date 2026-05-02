# Lab Context — for Larry Moleman

Where the cognitive lab lives, how to read it, and where to write to it.

## Where the lab lives

- **`cognitive-lab/cognitive-lab-v0.1.html`** — the lab itself. Source of truth is the embedded JSON in `<script type="application/json" id="lab-data">`.
- **`cognitive-lab/capacity-checkin.html`** — the original capacity check-in PoC (felt-sense layer of the Gauge).
- **`cognitive-lab/turn-v0.1-map.html`** — the four-act deck.
- **`cognitive-lab/turn-v0.1-phases-and-leverage.md`** — phase structure + research grounding.
- **`cognitive-lab/turn-v0.1-hacks-today.md`** — satisficing-mode practice notes.
- **`cognitive-lab/frame-research-and-practice.md`** — Frame's research-and-practice doc; the template for other phases' equivalents.
- **`cognitive-lab/cognitive-lab-plan.md`** — scope tiers (v0.1/v0.2/v0.3).

For workspace-local development before merge, paths may live under `.context/` instead. Check both. If neither has it, ask the author.

## Reading the lab

The data lives as embedded JSON inside the HTML. To read it:

```bash
# Get the lab data block
grep -A 99999 '<script type="application/json" id="lab-data">' cognitive-lab/cognitive-lab-v0.1.html | head -n -1 | tail -n +2
```

Or use the Read tool to read the file and locate the data section. The structure:

```js
{
  "areas": [
    {
      "id": "frame-workshop",
      "name": "Frame Workshop",
      "type": "phase / required",
      "accent": "blue",
      "workshop": true,
      "description": "...",
      "items": ["LAB-001", "LAB-002"],
      "sources": [{"label": "...", "href": "..."}],
      "experiments": [
        {
          "id": "...",
          "title": "...",
          "date": "...",
          "observation": "...",
          "impact": "..."
        }
      ],
      "chunks": [
        {
          "id": "...",
          "title": "...",
          "summary": "...",
          "body": "..."
        }
      ]
    }
  ],
  "items": {
    "LAB-001": {
      "id": "LAB-001",
      "title": "...",
      "status": "live",
      "priority": "P0",
      "area": "frame-workshop",
      "brief": "...",
      "full": "..."
    }
  }
}
```

## Writing to the lab

Use the Edit tool to make precise changes inside the JSON. Patterns:

### Adding a Log entry to an area's experiments array

Find the area's `"experiments": [` and prepend the new entry. Newest-first ordering.

### Adding a To-Do (LAB item)

1. Add to the `items` dictionary at the bottom.
2. Add the LAB-XXX id to the relevant area's `"items": [...]` array.
3. Add the LAB-XXX id to Backlog Wall's `"items": [...]` array.

### Updating an item's status

Status lives in the user's localStorage shadow, not the baseline JSON. The shadow is keyed `cognitive-lab-v0.1` and only available when the lab is open in a browser. Don't try to update status from disk; it has to happen in-browser via the UI's status cycle.

If the author asks you to "mark X live," the right move is to confirm they should cycle the status badge in the UI themselves. The auto-Log fires when they do.

### Adding a Source

Find the area's `"sources": [` (falls back to legacy `artifacts`) and append.

### Adding or updating a Chunk

Find the area's `"chunks": [` and prepend the new chunk, or update an existing one in place.

## Areas in the lab (for routing)

| Area ID               | Name                | Workshop? |
| --------------------- | ------------------- | --------- |
| `frame-workshop`      | Frame Workshop      | yes       |
| `comprehend-station`  | Comprehend Station  | no        |
| `sync-floor`          | Sync Floor          | no        |
| `push-bay`            | Produce Bay         | no        |
| `debrief-booth`       | Debrief Booth       | no        |
| `recovery-room`       | Recovery Room       | no        |
| `the-gauge`           | The Gauge           | no        |
| `pilot-check-station` | Pilot Check Station | yes       |
| `transition-hallway`  | Transition Hallway  | no        |
| `trim-bench`          | Trim Bench          | no        |
| `library`             | The Library         | no        |
| `archive`             | The Archive         | no        |
| `backlog-wall`        | Backlog Wall        | no        |
| `deck-theater`        | Deck Theater        | no        |
| `director-desk`       | Director's Desk     | no        |

This list will grow as more areas become workshops and as new areas are added.

## Local development server

The lab serves cleanly via Python with `.md` mime override:

```bash
cd cognitive-lab
python3 -c "
import http.server, socketserver
H = http.server.SimpleHTTPRequestHandler
H.extensions_map['.md']  = 'text/plain; charset=utf-8'
H.extensions_map['.txt'] = 'text/plain; charset=utf-8'
H.extensions_map['']     = 'text/plain; charset=utf-8'
with socketserver.TCPServer(('', 8765), H) as httpd:
    httpd.serve_forever()
"
```

Then `http://localhost:8765/cognitive-lab-v0.1.html`.

When you edit the lab HTML, the next browser refresh shows your changes. If localStorage is in use, baseline edits don't override user edits — the shadow takes precedence.

## When you can't find something

If a file path doesn't resolve, an item ID is missing, or the data shape doesn't match what's documented here, return a `Couldn't do` receipt rather than fabricating. The author or Quenton will resolve.
