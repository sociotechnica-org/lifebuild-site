# Lab Context — for Quenton Quince

Where the cognitive lab lives, how to read it, and the framework's central images.

## Where the lab lives

The cognitive lab is a self-contained interactive HTML artifact:

- **`cognitive-lab/cognitive-lab-v0.1.html`** — the lab itself. Single self-contained file, embedded JSON in `<script type="application/json" id="lab-data">` is the source of truth for areas, items, chunks, experiments, sources.
- **`cognitive-lab/capacity-checkin.html`** — the original capacity check-in PoC; the felt-sense layer of the Gauge.
- **`cognitive-lab/turn-v0.1-map.html`** — the four-act deck (21 slides, beginner-facing).
- **`cognitive-lab/turn-v0.1-phases-and-leverage.md`** — phase structure and research grounding.
- **`cognitive-lab/turn-v0.1-hacks-today.md`** — satisficing-mode practice notes.
- **`cognitive-lab/frame-research-and-practice.md`** — worked example of how chunk material gets developed for one phase. Use as the template for other phases.
- **`cognitive-lab/cognitive-lab-plan.md`** — v0.1/v0.2/v0.3 scope tiers.
- **`cognitive-lab/cognitive-lab-spec.md`** — the v0.1 build spec.

For local development, the lab is typically served via Python's built-in HTTP server with `.md` files served as `text/plain` so artifact links open in a tab rather than downloading:

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

Then open `http://localhost:8765/cognitive-lab-v0.1.html`.

## How the lab is structured

The lab is a top-down, click-to-explore floor plan with four bands:

**Band 1 — Reference / aux** (gestalt visuals, hover for label):

- The Library (research)
- The Archive (lab notes, decisions, shipped)
- Deck Theater (the v0.2 presentation)
- Backlog Wall (priority list)

**Band 2 — Phase cycle** (six rooms left-to-right):

- Frame · Comprehend · Sync · Produce (formerly Push) · Debrief · Recover

**Band 3 — Meta-disciplines:**

- Transition Hallway · Trim Bench

**Band 4 — Bottom (instruments + Director):**

- The Gauge · Pilot Check Station · Director's Desk

Click any area opens a side drawer (drawer expands to 66vw if the area has `workshop: true`). Drawers contain:

- A description (shown via the (i) tooltip in the header)
- Top half: the prototype (forms, sliders) — workshop areas only
- Bottom half: the four-tile floor shelf — **To Do · Log · Chapter · Sources**

## The four-tile shelf (every area)

| Tile           | What lives here                                                                           |
| -------------- | ----------------------------------------------------------------------------------------- |
| **✓ To Do**    | Forward-looking work — items to build, run, or write                                      |
| **📓 Log**     | Backward-looking observations — what happened during runs, what was noticed, what changed |
| **📚 Chapter** | Book material as chunks (title → summary → longform body). Chunks are editable.           |
| **📎 Sources** | Inputs — research references, past versions, related files                                |

Items have stable IDs (LAB-001, LAB-002, etc.). Status cycles: backlog → in-progress → drafted → live → archived. When an item moves to live or archived, an auto-Log entry captures the transition.

## The framework's central images

Two metaphors carry the framework's coherence. Use them when they sharpen the thinking.

### The cache-game

Originated from Jess's adventure-caching race story. Maps to Frame's four-batch structure:

- **Set the field** (Scope: Doing / Not Doing) — what's on the playing field today, what's off
- **Set the scoring** (Outcome: Done means / Bonus) — high-value catches and bonuses
- **Set the plan** (Approach: How I'll work) — strategy for playing
- **Set the endgame** (Safety: What ruins this / When to stop) — the three ways the day ends

Three end-states: collected enough → finish line; tired/hurt/done with what you got → head home early; time runs out → buzzer.

### The heartbeat

The give-and-take rhythm of capacity check ↔ restoration. The Gauge reads, the result dispatches: cleared (continue) or grounded (insert recovery, re-read). This rhythm runs continuously, between phases, across days. Without the heartbeat, the framework is just phases without honoring capacity. With it, every boundary is gated and every grounded reading dispatches targeted recovery.

The Pilot Check is the explicit pre-flight version of the heartbeat (rule-out across cognitive / emotional / physical, dispatching recovery hours per red dimension). The Gauge is the continuous instrument the heartbeat runs on.

## The framework in one paragraph

Knowledge work used to come in batches (mornings = email, afternoons = meetings). AI made it continuous — agents work 24/7, output is functionally infinite. Continuous-flow work breaks the people doing it because the management interface (calendars, project software, willpower) was built for batched work. The Turn is a structured cycle for AI-native work: six phases, three categories (required / conditional / insertable), gated by a continuously-read capacity gauge, paced by deliberate recovery. The framework borrows from cognitive load research, occupational health psychology, and industries that have long operated continuously (aviation, naval, manufacturing, medicine, sport).

## When you don't have the context

If a file path referenced here doesn't exist (e.g., the lab is in `.context/` rather than `cognitive-lab/` because the merge hasn't happened in this workspace), ask the author for the current location before proceeding. Don't fabricate state.
