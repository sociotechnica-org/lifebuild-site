# Cognitive Lab v0.1 — Build Spec

A single self-contained HTML file that renders a top-down pixel-art floor plan
of the cognitive load management lab. Click an area, side drawer slides in
with that area's items, artifacts, and lab notes. Local storage shadow for
edits; JSON export for persistence.

**Output path:** `.context/cognitive-lab-v0.1.html`
**Served from:** the existing local server at port 8765
**Dependencies:** none — vanilla HTML + CSS + JS, no build step

---

## Visual style (borrowed from agentplay)

**Palette:**
- Background: `#1a1a2e` (dark navy)
- Foreground: `#e8e0d4` (warm beige)
- Panel bg: `#16213e`
- Panel border: `#2a3a5c`
- Accent (primary): `#e2a04a` (warm orange)
- Accent dim: `#a87832`
- Teal: `#2d8a7e`
- Danger: `#c44d4d`
- Success: `#4daa57`
- Warning: `#d4a843`
- Floor tiles: `#4a3a2a` / `#5a4a3a` / `#6a5a4a` / `#3a2a1e` (gap)

**Typography:**
- Body: system sans
- Pixel/heading: Courier New, bold, uppercase, 1px letter-spacing, ~10–11px
- Headings tall and chunky

**Panel style:**
- 2px border in panel-border color
- 8px border-radius
- Header band in panel-border color, white-bold-uppercase text

**Buttons (retro):**
- Accent background, dark text
- 6px radius, chunky, uppercase Courier
- Hover: scale(1.04) + lighten
- Active: scale(0.97)

**Tiles:** 16px × 16px. Use a simple two-tone checker for floor (`#4a3a2a` / `#5a4a3a`).
**Walls:** along top and bottom edges. Color: `#2a2a3a` or similar dark.

---

## Sprite vocabulary

Source: `.context/attachments/pasted_text_2026-05-01_11-29-00.txt`, sprite
definitions starting at line ~2354 (`furniture.ts`).

For v0.1, we draw simplified versions in canvas-style pixel art, OR we use CSS
shapes/emojis for v0.1 simplicity. **Recommendation: CSS-pixel-art using
small grid of colored divs**, OR a single SVG-per-sprite. Either is fine —
canvas rendering is overkill for v0.1.

**Sprites we need:**

- **Desk** (32×16): warm wood `#8a6a3a` with darker edges `#6a4a2a`
- **Chair** (16×16): dark grey-blue `#3a3a4a`
- **PC monitor** (16×12): frame `#2a3a4a`, screen `#6aa8c8`
- **Plant** (12×20): pot `#5a3a1e`, leaves `#3a8a3a`
- **Bookshelf** (16×24): shelf `#6a4a2a`, multi-color books
- **Folder icon** (10×8): `#e2a04a`

Or simpler: render each "area" as a styled box (panel + label + signpost) and
add a few decorative emoji/CSS shapes (📋 📁 📚 🌱 etc.) inside as flavor.
**For v0.1, prefer the simpler box-with-emoji approach** — it captures the
spatial / game-y vibe without the canvas complexity.

---

## Layout (20 cols × 14 rows on a tile grid)

The lab has four bands top-to-bottom:

```
Row 0:    [WALL ────────────────────────────────────]
Rows 1-3: [LIBRARY  ]   [DECK THEATER  ]   [BACKLOG WALL ]
                  (research)        (deck)        (priority list)

Rows 4-6: [FRAME] → [COMPREHEND] → [SYNC] → [PUSH] → [DEBRIEF] → [RECOVER]
          (the six-phase cycle, left-to-right, with arrows)

Rows 7-9: [PILOT CHECK]      [GAUGE — center]      [DIRECTOR DESK]
          (multi-signal)      (capacity inst.)     (you, sprite)

Rows 10-12: [TRANSITION]    [TRIM]    [ARCHIVE]
            (meta)         (meta)    (lab notes/decisions/shipped)

Row 13:   [WALL ────────────────────────────────────]
```

Each lettered area is a clickable region with its own panel/sign.

---

## Areas (full list with content)

Each area gets a panel on the floor with its name, signpost, decorations, and
a click target. Click → drawer.

### Phase row (cycle)

#### `frame-workshop` — Frame Workshop
- Type: phase / required
- Color: blue `#4a7bd4` accent border
- Description: "Where the Frame practice and chapter live. The phase that decides what the turn is for."
- Items: LAB-001, LAB-002
- Artifacts:
  - `.context/turn-v0.1-phases-and-leverage.md` (Frame section)
  - `.context/turn-v0.1-hacks-today.md` (today.md template + Match section)
  - `.context/turn-v0.1-map.html` (deck slide 13)
- Lab notes: 2026-04-30 wildcat Frame
- Decoration: desk + PC + folder icon (active)

#### `comprehend-station` — Comprehend Station
- Type: phase / conditional
- Color: amber `#d4a030` accent border
- Description: "Where Comprehend practice and chapter live. The phase that loads remaining state from agents and prior work."
- Items: LAB-009, LAB-010
- Artifacts: `.context/turn-v0.1-phases-and-leverage.md` (Comprehend section)
- Decoration: desk + PC + bookshelf (research)

#### `sync-floor` — Sync Floor
- Type: phase / conditional
- Color: amber `#d4a030`
- Description: "Where Sync practice and chapter live. The phase that aligns humans and agents and confirms zones."
- Items: LAB-011, LAB-012
- Artifacts: `.context/turn-v0.1-phases-and-leverage.md` (Sync section)
- Decoration: desk + PC + plant

#### `push-bay` — Push Bay
- Type: phase / conditional
- Color: amber `#d4a030`
- Description: "Where Push practice and chapter live. Decision work, hardest first, with bingo-fuel stop signal."
- Items: LAB-013, LAB-014
- Artifacts: `.context/turn-v0.1-phases-and-leverage.md` (Push section), `.context/turn-v0.1-map.html` (deck slide 18 — bright-red tripwire)
- Notes: Jess's bike-race metaphor lives here as central illustration
- Decoration: desk + PC + folder icon

#### `debrief-booth` — Debrief Booth
- Type: phase / required
- Color: blue `#4a7bd4`
- Description: "Where Debrief practice and chapter live. Closes the cycle, captures, sets up the next gauge read."
- Items: LAB-003, LAB-004
- Artifacts: `.context/turn-v0.1-phases-and-leverage.md` (Debrief section)
- Decoration: desk + PC + folder icon

#### `recovery-room` — Recovery Room
- Type: phase / insertable
- Color: green `#4a8a5a`
- Description: "Where Recover practice and chapter live. Pick a mode: Detach, Relax, Master, Choose. Includes Sleep as special insertion."
- Items: LAB-015, LAB-016
- Artifacts: `.context/turn-v0.1-phases-and-leverage.md` (Recover section), `.context/turn-v0.1-map.html` (deck slide 15)
- Decoration: plant + bookshelf (no desk — it's a recovery room)

### Center / always-visible

#### `the-gauge` — The Gauge
- Type: gauge / telemetry
- Color: dark `#2d3142` with orange accent
- Description: "The capacity instrument. Read at every boundary. Gates the day's mode."
- Items: LAB-020, LAB-021
- Artifacts:
  - existing capacity-checkin PoC (note: not in this folder yet — exists in user's other workspace)
  - `.context/turn-v0.1-map.html` (deck slide 11 + slide 17, multi-signal model)
- Decoration: monitor / dashboard motif

#### `director-desk` — Director's Desk (you)
- Type: aux / persistent
- Description: "Your seat. Where the Frame card sits today, where lab notes get written."
- Items: links to today's Frame card if one exists
- Decoration: desk + chair + PC + Director sprite (the only sprite in v0.1)

### Side wings

#### `pilot-check-station` — Pilot Check Station
- Type: meta-instrument / multi-signal
- Color: warning `#d4a843`
- Description: "Multi-signal capacity model: felt, behavioral, temporal. Bright-red tripwire lives here."
- Items: LAB-007, LAB-008
- Artifacts: `.context/turn-v0.1-map.html` (deck slides 17–18)
- Decoration: small desk + PC + warning glyph

#### `transition-hallway` — Transition Hallway
- Type: meta-discipline
- Color: tan `#8a7a5a`
- Description: "Every phase boundary is taxed. Close · reset · open. Practice surface for the boundary move."
- Items: LAB-005, LAB-006
- Artifacts: `.context/turn-v0.1-map.html` (deck slide 20)
- Decoration: corridor / arrow motif

#### `trim-bench` — Trim Bench
- Type: meta-discipline
- Color: tan `#8a7a5a`
- Description: "Selection discipline within each phase. Lower priority once Frame is doing its job."
- Items: LAB-017, LAB-018
- Artifacts: `.context/turn-v0.1-map.html` (deck slide 20)
- Decoration: small workbench / scissors glyph

### Back / aux

#### `library` — Research Repository (research & findings)
- Type: archive / research & findings
- Color: warm beige `#a88a5a` (bookshelf)
- Description: "The evidence base our decisions get made on. External research and our own internal findings — the truth as we best understand it, plus the receipts."
- Items: research references list (read-only) + filed reports
- Artifacts: list below; live entries flow in via the Drive manifest (`exports/research-manifest.json`)
- Decoration: large bookshelf
- Filing guide: see `filingGuide` block on the area in `cognitive-lab-v0.1.html`

  **Research references for v0.1:**
  - Sweller — Cognitive Load Theory (intrinsic / extraneous / germane)
  - Hobfoll — Conservation of Resources (loss spirals, capacity bank)
  - Sonnentag & Fritz — Recovery Experiences (detach / relax / master / control)
  - Hockey — Compensatory Control Model (effort under demand has hidden cost)
  - Leroy 2009 — Attention Residue (the tab-switch tax)
  - Gawande — The Checklist Manifesto (5–9 items, do-confirm vs read-do)
  - Klein — Pre-mortem (specific risk-naming beats optimism)
  - Bainbridge — Ironies of Automation (humans monitoring automation need more context)
  - Endsley — Situation Awareness (perception, comprehension, projection)
  - Wickens — Multiple Resource Theory (channels can run parallel)
  - IM SAFE — FAA pilot pre-flight checklist
  - Bingo fuel — combat aviation pre-committed turnback
  - Naval watchstanding — formal handoff protocols, taking the conn
  - Goldratt — Theory of Constraints, drum-buffer-rope
  - Csikszentmihalyi — Flow (useful but masks cost)
  - Risko & Gilbert 2016 — Cognitive Offloading
  - Shah, Friedman, Kruglanski — Goal Shielding
  - Vohs & Baumeister — Decision Fatigue
  - Toyota Production System — andon, takt time
  - WHO Surgical Checklist
  - McEwen — Allostatic Load
  - Kaplan — Attention Restoration Theory

#### `archive` — The Daily Journal
- Type: archive / journal
- Color: warm beige `#a88a5a`
- Description: "The lab's scratchpad and historical record. Loose notes captured throughout the day, decisions aggregated from anywhere they're made, and a date-organized newspaper of what each day produced."
- Three shelves: scratchpad (loose, current, preserved), decisionLog (aggregated decisions), editions (dated newspapers; auto-skip empty days)
- Items: editions flow in via the Drive manifest (`exports/journal-manifest.json`); legacy lab-notes / decisions / shipped lists below preserved as pre-newspaper history
- Decoration: newspaper + coffee + journal triptych (`☕ 📰 📓`)
- Filing guide: see `filingGuide` block on the area in `cognitive-lab-v0.1.html`

  **Lab notes:**
  - 2026-04-30 — Wildcat Frame example (today, evening session)
  - 2026-04-30 — The morning gauge worked (recovery turnaround)

  **Decisions log:**
  - 2026-04-30 — Dropped F/R/A/M/E acronym; build infrastructure (a Lab Plan) first, name later
  - 2026-04-30 — Renamed *Ledger* → *Gauge* in framework; reserve "Ledger" for Alexandria
  - 2026-04-30 — Adopted Must/Stretch refinement of Focus (driven by Jess's bike-race metaphor)
  - 2026-04-30 — Days are reporting periods, turns are work units (turns can span sleep)
  - 2026-04-30 — Three-signal capacity model adopted (felt + behavioral + temporal)
  - 2026-04-30 — Phase categories: required / conditional / insertable
  - 2026-04-29 — Four-act narrative structure for the deck
  - 2026-04-29 — Phase library: Frame · Comprehend · Sync · Push · Debrief · Recover (six phases)

  **Recently shipped:**
  - v0.2 deck (turn-v0.1-map.html — four-act presentation)
  - Phases-and-leverage doc (turn-v0.1-phases-and-leverage.md)
  - Hacks-today doc (turn-v0.1-hacks-today.md)
  - Cognitive lab plan (cognitive-lab-plan.md)
  - Capacity check-in PoC (capacity-checkin.html — exists in user's other workspace; daily-use discipline ongoing)

#### `strategy` — Strategy & Plans
- Type: aux / strategy
- Color: blue accent
- Description: "Raw source material for our living libraries — the product roadmap (Alexandria) and the future corporate business plan. Strategy and planning content that needs a home before — or until — the atomic libraries process it."
- Items: roadmaps, plans, lab architecture, frameworks; flow in via the Drive manifest (`exports/strategy-manifest.json`)
- Decoration: compass + map + chess piece triptych (`🧭 🗺️ ♟️`)
- Filing guide: see `filingGuide` block on the area in `cognitive-lab-v0.1.html`

#### `deck-theater` — Explainer Theater
- Type: aux / explainer
- Color: teal `#2d8a7e`
- Description: "Material we made — or co-made — to explain something to a person. Walkthroughs, 2-pagers, investor decks, onboarding docs."
- Items: explainers flow in via the Drive manifest (`exports/explainer-manifest.json`)
- Artifacts: `.context/turn-v0.1-map.html` and other lab decks
- Decoration: small theater / screen / projector
- Filing guide: see `filingGuide` block on the area in `cognitive-lab-v0.1.html`

> **Note on the retired Backlog Wall.** Earlier versions of the lab carried a fifth Band-1 area, `backlog-wall`, holding the canonical full LAB-XXX list. It was retired in favor of the toolbar's By Status and Priority views, which already provide global priority + status surfaces. Items are now anchored to their declared `area` field; the retired area is no longer needed.

---

## Items (the LAB backlog)

### P0 — must do this period

- **LAB-001** Frame form v1 — `in-progress` — frame-workshop
  Drop F/R/A/M/E acronym; ground in plan-pointing; deliver runnable form including Must/Stretch.

- **LAB-002** Frame chapter outline — `in-progress` — frame-workshop
  The trap, mechanism, aviation precedent, the form, lab notes, failure modes, current best.

- **LAB-003** Debrief form v1 — `backlog` — debrief-booth
  Five-minute close-of-turn template. Captures, lab note, sets up next gauge read.

- **LAB-004** Debrief chapter outline — `backlog` — debrief-booth
  Why measurement closes the cycle. After-action-review patterns. Reflection theory.

- **LAB-005** Transition practice — `backlog` — transition-hallway
  60-second boundary protocol. Physical + cognitive anchors. Scales: micro / meso / macro.

- **LAB-006** Transition chapter outline — `backlog` — transition-hallway
  Attention residue mechanism. Why every boundary leaks. Practice surface.

- **LAB-007** Pilot Check form — `backlog` — pilot-check-station
  Multi-signal model in practice. When to spike-check. Bright-red tripwire defaults.

- **LAB-008** Pilot Check chapter — `backlog` — pilot-check-station
  Why the Gauge alone isn't enough. The three signals. Aviation precedent (IM SAFE + duty-time + cross-check).

### P1 — soon

- **LAB-009** Comprehend form — `backlog` — comprehend-station
- **LAB-010** Comprehend chapter outline — `backlog` — comprehend-station
- **LAB-011** Sync form — `backlog` — sync-floor
- **LAB-012** Sync chapter outline — `backlog` — sync-floor
- **LAB-013** Push form — `backlog` — push-bay
  With bingo fuel + decision order + Must/Stretch composition.
- **LAB-014** Push chapter — `backlog` — push-bay
  Bike-race metaphor as central illustration. Greedy vs conservative calibration.
- **LAB-015** Recover practice — `backlog` — recovery-room
  Detach/Relax/Master/Choose discipline. Sleep as special insertion. Detection of "blue but actually gray."
- **LAB-016** Recover chapter — `backlog` — recovery-room
  Sonnentag's framework. Why mode matters. The morning-after test.
- **LAB-017** Trim practice — `backlog` — trim-bench
  Selection heuristics. Fast-no protocols. (Lower priority once Frame works.)
- **LAB-018** Trim chapter — `backlog` — trim-bench
- **LAB-019** Run 1 week of formal Frame and capture lab notes — `backlog` — frame-workshop / archive
- **LAB-020** Per-turn gauge entries (vs only per-day) — `backlog` — the-gauge
- **LAB-021** Capacity check-in v0.2 (turn-aware data model) — `backlog` — the-gauge

### P2 — later

- **LAB-022** Cowork integration (morning prompt opens Frame card) — `backlog` — director-desk
- **LAB-023** Cognitive Lab v0.2 (people at desks, animations, persistence) — `backlog` — director-desk
- **LAB-024** Multiplayer (you + Jess in lab simultaneously) — `backlog` — director-desk

---

## Behavior

### Click an area
Side drawer slides in from the right (or modal pops up — drawer preferred):
- Header: area name + type badge + close X
- Body:
  - Description paragraph
  - Items list (each with title, status badge, priority badge, brief)
    - Click an item → drilldown view (within the drawer) with full description, status toggle (cycle: backlog → in-progress → drafted → live → archived), and a "back to area" link
  - Artifacts list (each a hyperlink to the file/url)
  - Lab notes (most recent 5, expandable)
- ESC closes; X closes; clicking outside closes
- URL hash deep-link: `#area=frame-workshop` opens the drawer for that area

### Status changes
- Item status toggle button cycles through states
- Saved to localStorage immediately
- LocalStorage shadow keyed by `cognitive-lab-v0.1` with the full data blob

### Persistence
- Embedded JSON in the HTML is the baseline (read-only canonical state)
- LocalStorage shadow holds local edits (status changes, possibly added items)
- "Export JSON" button: download merged baseline + edits as JSON
- "Reset" button: clear localStorage shadow, return to baseline
- "Import JSON" button: load JSON file, overwrite localStorage
- No server writes (yet)

### Floor view
- Static layout (no camera pan/zoom for v0.1 — simpler)
- All areas visible at once
- Hover an area: subtle glow / outline highlight
- Click an area: drawer opens
- Director sprite at director-desk, idle (no animation needed)

### Visual state on the floor
- Each area shows item count badges:
  - P0 count (red dot if any P0 items not done)
  - In-progress badge (orange pulse if any in-progress)
  - Done indicator (green if all items done)

---

## Out of scope for v0.1

- Camera pan/zoom (lab fits in viewport)
- Animated agent sprites at desks
- Inline item editing (creating new items, full-text edit)
- Live experiment iframes
- Server-side persistence
- Multi-user / multiplayer
- Real-time agent status feeds from conductor

These all live in v0.2+ per the project plan.

---

## Implementation notes for the builder

- **Single HTML file** at `.context/cognitive-lab-v0.1.html`
- **No build step**, no npm, no deps
- **Vanilla JS** (or minimal alpine.js if needed — lean toward vanilla)
- **Embedded `<script type="application/json" id="lab-data">`** with the full data model
- **CSS Grid or absolute-positioned divs** for the floor — pick whichever is cleaner
- **CSS for sprites** — small grids of colored divs OR inline SVG OR emoji
  - For v0.1, **emoji + styled boxes is fine**. Lean simple.
  - The "pixel art" feel comes from the palette + Courier font + chunky borders, not from literal pixel-perfect sprites
- **Drawer:** absolute-positioned right side, slides in via CSS transform, ~400px wide
- **Hash routing:** `window.addEventListener('hashchange', ...)` handles deep-links
- **LocalStorage key:** `cognitive-lab-v0.1`
- **Print-friendly:** `@media print` shows full lab + drawer-as-section

The deliverable is one file. It opens in a browser. It tells you what the lab
contains, lets you navigate by clicking areas, lets you toggle item status,
and lets you export/import the state.
