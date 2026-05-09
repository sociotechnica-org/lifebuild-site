# The Cognitive Lab — Interactive Map · Project Plan

A spatial, click-to-explore HTML artifact that doubles as (1) the Lab Plan
(priorities, backlog, status) and (2) the hub for the cognitive load management
work (lab notes, drafts, experiments, research). You walk into the lab; you
visit areas; each area shows what's there and what's in progress.

---

## v0.1 — what gets built first (achievable in one session)

**Single self-contained HTML file**, no dependencies. Top-down floor plan of
the lab. Click an area, side panel opens with what's in that area.

### What you can do in v0.1

- See the whole lab at a glance.
- Click any area → side panel with: description, current status, linked
  artifacts (markdown docs, the deck, the PoC), active items, recent lab notes.
- Stable item IDs (`LAB-001`, etc.) so any area's items can be referenced from
  Frame, Debrief, and the lab notes themselves.
- Filter view by status (backlog / in-progress / drafted / live / archived) or
  priority (P0 / P1 / P2).
- Direct-link via URL hash to any area (e.g. `#frame-workshop`).

### Areas in the lab (v0.1)

The cycle along the main floor (six phase rooms):

1. **The Frame Workshop** — Frame practice, form, chapter
2. **The Comprehend Station** — Comprehend practice, form, chapter
3. **The Sync Floor** — Sync practice, form, chapter
4. **The Push Bay** — Push practice, form, chapter (incl. bingo fuel, decision order)
5. **The Debrief Booth** — Debrief practice, form, chapter
6. **The Recovery Room** — Recover modes (Detach/Relax/Master/Choose), chapter

Center of the floor (always visible):

- **The Gauge** — the capacity instrument; links to the existing capacity
  check-in PoC; multi-signal model lives here

Side wings:

- **The Pilot Check Station** — multi-signal capacity, bright-red tripwire
- **The Transition Hallway** — meta-discipline for boundaries
- **The Trim Bench** — meta-discipline for selection

Back of the lab (Band 1 — four areas):

- **Research Repository** (formerly The Library) — research & findings.
  External research (Sweller, Hobfoll, Sonnentag, Hockey, Leroy, Klein,
  Gawande, IM SAFE, naval watchstanding, etc.) plus our own internal
  findings. Reports flow in via the Drive manifest.
- **The Daily Journal** (formerly The Archive) — scratchpad, decision log,
  date-organized editions. The lab's historical record. Three shelves;
  editions auto-skip empty days.
- **Explainer Theater** (formerly Deck Theater) — writeups, decks, demos.
  Material we made to explain something to a person.
- **Strategy & Plans** — plans, roadmaps, architecture. Raw source material
  for the living libraries (Alexandria for product; corporate library for
  business). The room exists so this stuff doesn't get lost.

The retired Backlog Wall is no longer a Band-1 area — its job moved to the
toolbar's By Status and Priority views.

### Art style for v0.1 (before agentplay code arrives)

- Clean 2D floor plan, color-coded by phase category (required / conditional
  / insertable / meta / archive)
- Simple labels and icons
- Hover highlight, click opens panel
- No avatars yet; rooms are rooms. People come in v0.2.

### Data model (v0.1)

Embedded JSON in the HTML for now. Easy to migrate later.

```json
{
  "areas": {
    "frame-workshop": {
      "title": "The Frame Workshop",
      "category": "required",
      "phase_role": "phase",
      "blurb": "Where the Frame practice, form, and chapter are designed.",
      "x": 80, "y": 120, "w": 220, "h": 150,
      "items": ["LAB-001", "LAB-010"],
      "artifacts": [
        { "title": "Phases & Leverage doc — Frame section",
          "url": "turn-v0.1-phases-and-leverage.md#frame" },
        { "title": "Wildcat Frame example (lab note 2026-04-30)",
          "url": "turn-v0.1-hacks-today.md#lab-notes-live" }
      ],
      "experiments_live": []
    }
  },
  "items": {
    "LAB-001": {
      "title": "Frame form v1",
      "status": "in-progress",
      "priority": "P0",
      "area": "frame-workshop",
      "blurb": "Drop the F/R/A/M/E acronym; ground in plan-pointing; deliver runnable form."
    }
  }
}
```

---

## v0.2 — after agentplay code lands

**People at desks.** Avatars in rooms doing the work. Status indicators visible
from the floor view (which agents are running, which areas are active right
now). Borrows agentplay's art style and likely:

- Avatar/desk visuals
- Idle / working / blocked animations or indicators
- Hover and click interaction patterns
- Ambient room state (e.g., a "lit" room is the active area for the current turn)

Plus:

- Inline editing of items (mark P0→shipped, add new items, change status)
- Persistence via localStorage (with JSON export, matching the capacity check-in PoC pattern)
- Embedded mini-views of live experiments (capacity check-in, the deck) accessible from the relevant rooms

---

## v0.3 — eventually

- Multiplayer view (you + Jess present in the lab simultaneously)
- Backend persistence (Sheets / Supabase / file-watcher) so two devices stay in sync
- Real-time agent status feeds from conductor workspaces (this is the actual Cockpit problem; the lab becomes the cockpit when this works)
- Direct integration with Cowork (morning prompt opens the lab to today's Frame card)

---

## Layout sketch (v0.1)

```
┌───────────────────────────────────────────────────────────────┐
│  THE COGNITIVE LAB                                             │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│   ┌──────┐  ┌──────────┐  ┌──────┐  ┌──────┐  ┌──────────┐   │
│   │FRAME │→ │COMPREHEND│→ │ SYNC │→ │ PUSH │→ │ DEBRIEF  │   │
│   └──────┘  └──────────┘  └──────┘  └──────┘  └──────────┘   │
│       ↑                                              ↓         │
│       └──────── ┌──────────┐ ──────── ┌──────────┐ ←┘         │
│                 │  GAUGE   │          │ RECOVERY │             │
│                 │  (always)│          │   ROOM   │             │
│                 └──────────┘          └──────────┘             │
│                                                                │
│   ┌──────────────┐    ┌──────────────────┐                    │
│   │ PILOT CHECKS │    │ TRANSITION HALL  │                    │
│   └──────────────┘    │ + TRIM BENCH     │                    │
│                       └──────────────────┘                    │
│                                                                │
│   ┌─────────────┐   ┌──────────────┐    ┌─────────────────┐ │
│ │ RESEARCH    │ │ DAILY JOURNAL │ │ EXPLAINER  │ │ STRATEGY  │ │
│ │ REPOSITORY  │ │ (scratchpad,  │ │ THEATER    │ │ & PLANS   │ │
│ │ (research   │ │  decisions,   │ │ (writeups, │ │ (plans,   │ │
│ │  & findings)│ │  editions)    │ │  decks,    │ │  roadmaps,│ │
│ │             │ │               │ │  demos)    │ │  arch)    │ │
│ └─────────────┘ └───────────────┘ └────────────┘ └───────────┘ │
└───────────────────────────────────────────────────────────────┘
```

Phases on the main floor in cycle order (the Turn). Gauge in the center,
Recovery loops back. Pilot Checks adjacent to Push (where they fire most).
Transition + Trim as a meta corridor. Band 1 (the back row) is the four
holding-pen areas: Research Repository · Daily Journal · Explainer Theater
· Strategy & Plans. The toolbar's By Status / Priority views replace the
retired Backlog Wall as the global priority/status surfaces.

---

## Open questions

1. **Naming.** Each area has a working name. We'll keep them light until the
   work shape is clear. ("Workshop / Station / Floor / Bay / Booth / Room"
   was a quick-pick; could simplify.)
2. **Persistence model for v0.1.** Pure embedded JSON (no editing) keeps it
   read-only — fast to ship, but you'd edit by hand-editing the file. Or
   embedded JSON + localStorage shadow (changes saved locally, baseline in
   file) — slightly more complex but actually usable as a tool.
3. **Where does the Gauge appear?** Currently center-stage. Could be a
   persistent sidebar/HUD instead (always visible regardless of room).
4. **~~Backlog Wall: separate area or integrated into each room?~~** Resolved:
   the Backlog Wall area was retired. Its job moved to the toolbar's By Status
   and Priority views, which already provided global priority + status surfaces.
   Items are now anchored to their declared `area` field.
5. **agentplay code reuse — what's actually available?** Determines how big
   the v0.1 → v0.2 jump is. If avatars are easy to import, v0.1 might already
   include them.

---

## Sequence

1. **Confirm v0.1 scope** with you (this doc).
2. **Pull agentplay code** so I can see what's borrowable for art/interaction.
3. **Build v0.1** as a single HTML file in `.context/`, served via the
   existing local server.
4. **Populate** the data model with current items from this session
   (Frame v1, Debrief v1, Transition, Pilot Checks, etc.).
5. **Use it** — Frame against it tomorrow morning. The Frame card becomes
   "select from the lab" instead of "answer five questions."
6. **Iterate** v0.2 once agentplay's pieces are wired in.
