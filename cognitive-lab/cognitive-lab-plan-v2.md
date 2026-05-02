# The Cognitive Lab — Updated Project Plan (v0.2 onward)

A research-grounded revision of the original plan, written after the spatial-knowledge-UI literature review (2026-05-01). Keeps what v0.1 got right, drops the v0.2/v0.3 ideas the evidence flags as graveyards, and reorders the roadmap around the patterns the research actually supports.

The original plan lives at `cognitive-lab-plan.md` and is preserved as the v0.1-era artifact.

---

## What v0.1 landed (and what to keep)

The shipped v0.1 is, by accident or instinct, well inside the design envelope the research defends:

- **2D top-down floor plan**, not 3D — avoids the Magic Cap / Task Gallery / BumpTop failure mode.
- **User-authored placement** — every item lives in a room you put it in. The *binding act* is what carries the recall benefit; immersion barely matters.
- **Diegetic containers** — Frame Workshop, Library, Backlog Wall, Pilot Check Station. Finite, hand-shaped, named. Same pattern as the *Animal Crossing* museum and the *Myst* library.
- **Inside the 100–1,000-item sweet spot** — 14 areas, 25 items. Comfortably below the threshold where spatial memory loses to search.
- **Persistent landmarks** — The Gauge centered, the cycle laid out with arrows, Recovery looping back. Single-screen layout means you can't get lost.
- **Stable item IDs** — LAB-### references are stable across the lab, the chapters, and lab notes.

Keep all of this. The next moves are additions, not replacements.

---

## The design envelope (rules we're building inside)

From the research synthesis. Treat as constraints, not aspirations:

1. **2.5D max.** Tilted planes are fine; locomotion-heavy 3D is not.
2. **Hand-place items the user cares about remembering.** Auto-layout is a *view*, never canonical data.
3. **Build for 100–1,000 items as the primary affordance.** Add escape hatches (search, teleport) for edges, not as the main UI.
4. **Multiple views over one corpus, not multiple corpora.** Same items, switchable lenses.
5. **Render the unknown.** Empty slots, ghost nodes, "more here" markers.
6. **Search is non-negotiable.** Cmd-K is the last-mile aid after spatial recall gets you to the neighborhood.
7. **Reward revisiting.** Surface what changed since last visit.

---

## v0.2 — high-leverage build, in priority order

### P0a — Multiple views over one corpus (the Map/Rumor toggle)

The biggest creative win in this plan. Currently the Backlog Wall is its own area on the floor — a half-baked version of this idea. Promote it from area to *view*.

**What ships:**
- A view-mode toggle at the top of the lab: **Floor · Priority · Timeline · By Status**.
- All four modes render the same underlying items. No new data; new lenses.
  - **Floor** (default): the current spatial layout.
  - **Priority**: items grouped P0 / P1 / P2, sorted by status. (Replaces the Backlog Wall as a standalone area.)
  - **Timeline**: items sorted by `lastTouched` date (status change, note added, edited). Shows what's hot and what's gone cold.
  - **By Status**: kanban-style columns: backlog / in-progress / drafted / live / archived.
- Toggle persists per session in localStorage.
- Drawer contents are identical regardless of view — clicking an item opens the same drawer.

**What this lets you do:** ask "what's hot this week" (Timeline), "what's the next P0" (Priority), "where am I stuck" (By Status), "where does this live in the framework" (Floor) — without leaving the lab.

**What this displaces:**
- Backlog Wall as a floor area is removed; its contents become the Priority view.
- The Archive's date-stamped notes inform Timeline (notes appear inline alongside items by date).

**Cost:** Medium. Mostly rendering work; data model is unchanged.

---

### P0b — Cmd-K search

Non-negotiable per the research. Less urgent than the toggle at 25 items, but cheap to ship and scales the lab.

**What ships:**
- Cmd-K (and Ctrl-K) opens a search palette overlay.
- Searches: item titles + briefs + full descriptions, area names + descriptions, lab notes, decisions log.
- Enter teleports: opens the right drawer, scrolls to the right item, in whichever view mode is active.
- Recent searches and recent items at the top when the palette is empty.

**Cost:** Small. Single new component, indexes the same JSON the lab already loads.

---

### P0c — Gaps as guides + ghost items

The clearest transferable insight from games to PKM (*Stardew*, *Obra Dinn*, *Outer Wilds*). One feature with two surfaces.

**Gaps as guides** — render expected-but-missing items as empty slots:
- Each phase area has a known shape: every phase eventually wants `<phase> form v1`, `<phase> chapter`, `<phase> practice`. When the slot is empty, render it greyed-out and labeled, e.g., the Sync Floor shows an empty `Sync chapter v1` slot until one exists.
- Slots are configured per area (not per item). The interface tells you what's next.

**Ghost items** — surface referenced-but-not-yet-captured items:
- When a chapter, lab note, or decision references something that isn't yet a LAB-### item, render it as a ghost on the relevant area's wall.
- Click a ghost to promote: it becomes a real LAB-### with `status: backlog` and an auto-filled brief from the referencing context.
- A small "promote" affordance is enough; no need for a wizard.

**Detection of ghosts** — look for unresolved references:
- Plain-text mentions in lab notes / decisions that follow a `[[bracketed name]]` or `>>name<<` convention (decide on the syntax). Anything not matching a known LAB-### is a ghost candidate.
- For chapter cross-references: parse the markdown for `LAB-###` patterns; if the ID isn't in the items table, it's a ghost.

**Cost:** Medium. Empty slots are cheap. Ghost detection needs a parser pass over notes and chapters.

---

### P1a — Since-last-visit delta

Cheap, high return. The "reward for revisiting" principle.

**What ships:**
- Each area drawer opens with a small banner: "Since you were last here: 2 lab notes, 1 status change, 1 new ghost."
- Clicking the banner expands a list of changes since the last `lastVisited[areaId]` timestamp.
- Closes when dismissed or when you click an item; updates the timestamp on close.

**Cost:** Small. Track `lastVisited` per area in localStorage; diff against `lastTouched` on items / notes / decisions.

---

### P1b — Lab notes placed spatially

The method-of-loci binding act. Notes stop being a flat date-stamped list and start hanging on walls.

**What ships:**
- New shape on each lab note: `area`. Defaults to whichever drawer is open when the note is created.
- Notes render on the wall of their area as small stickies (3–6 visible per area; "+N more" link to expand).
- Notes also still appear in the Archive (the Archive becomes a *view* across all areas, not the only home).
- Can be moved between areas via drag or a dropdown.

**Cost:** Medium. Visual change in each area drawer, plus a migration to add `area` to existing notes (default to the area mentioned in the note text, fall back to "the-archive").

---

### P2 — Mild 2.5D tilt (Data Mountain treatment)

Polish, not foundational. The research is most confident about a 9–28% recall bump from tilted/bent layouts vs. pure flat 2D.

**What ships:**
- Subtle isometric tilt on the floor plan (CSS `transform: perspective() rotateX()` is enough — no real 3D engine).
- Areas in the foreground render slightly larger; background areas slightly smaller. No occlusion; no locomotion.
- Toggle to flat view in settings (some users get motion sensitivity from tilted planes).

**Cost:** Small. Pure CSS. Can ship after agentplay code lands or alongside it.

---

## v0.3 — what's worth doing later

The original v0.3 vision (multiplayer presence, real-time agent feeds, "the cockpit") is downscoped to its load-bearing pieces. The fantasy of two avatars in a shared room is dropped; the actually-useful integrations stay.

- **Two-device sync via Supabase or similar.** Not multiplayer presence — just "the same lab, viewable from laptop and phone, edits land on both." No avatars, no cursors, no real-time collaboration UI.
- **Cowork integration.** Morning prompt opens the lab to today's Frame card. Already half-implied by the Frame Workshop being a special area.
- **Embedded mini-views of live experiments.** The capacity check-in PoC visible inside the Gauge drawer (iframe is fine). The deck visible inside the Deck Theater drawer.
- **Inline editing of items.** Edit titles, briefs, descriptions, areas — not just status. Already partly in v0.2 with ghost promotion; complete it here.

Everything below is gated on the v0.2 features earning their keep first. No reason to ship sync if the toggle and the gaps haven't proved useful.

---

## Explicitly NOT building (with rationale)

These are recorded so the question doesn't get re-litigated. Each one has a research-backed reason to stay out.

- **Walking avatars / desk animations / physics piles.** The Magic Cap / Task Gallery / BumpTop pattern. Reviewers consistently described BumpTop as "fun for two minutes, annoying for an hour." Task Gallery scored 5.3/7 satisfaction but 3.1/7 on "I always knew what to do" — the metaphor shatters the moment real content appears inside it. **What we'll do instead:** ambient room state — a "lit" room when an area is the active phase; a small badge when an agent is running. Indicators, not theater.
- **Real-time multiplayer presence.** Workrooms shut down February 2026. Spatial.io pivoted away from work. Synchronous spatial co-presence is not where the value is. **What we'll do instead:** sync the *data*, not the *presence* (see v0.3).
- **VR / 3D / Vision Pro mode.** Recall bump is 9–28%; friction is enormous; 2026 reviews call third-party PKM in visionOS "early days." Not worth it for knowledge work.
- **Auto-clustering / AI semantic placement.** Earns its keep on uncurated 10k-item canvases (Mymind, Kosmik). At 25 hand-placed items it solves a problem we don't have.
- **Force-directed graph view.** Hairball past 500 nodes; froze a 6k-note Obsidian vault. If a graph view ever ships, it's a hand-curated dependency map (LAB-001 → LAB-010 arrows), not a physics blob over all references.
- **Zoom / pan / camera.** The framework fits in one viewport. That's a feature. Power-law zoom is for tools that have given up on fitting.
- **Forced taxonomy / required tags.** Shipman & Marshall's "Formality Considered Harmful" — users refuse to pay the cost of premature categorization. Our taxonomy is the floor plan; nothing else is required.

---

## Updated layout sketch

```
┌───────────────────────────────────────────────────────────────────┐
│  THE COGNITIVE LAB        [Floor] Priority  Timeline  By Status    │  ← view toggle
├───────────────────────────────────────────────────────────────────┤
│                                          [⌘K Search...]            │  ← Cmd-K palette
│                                                                    │
│   ┌──────┐  ┌──────────┐  ┌──────┐  ┌──────┐  ┌──────────┐       │
│   │FRAME │→ │COMPREHEND│→ │ SYNC │→ │ PUSH │→ │ DEBRIEF  │       │
│   │ ▣ ◌  │  │   ◌ ◌    │  │  ▣◌  │  │  ▣ ▣ │  │   ◌ ◌    │       │  ← ▣ filled, ◌ ghost/empty
│   └──────┘  └──────────┘  └──────┘  └──────┘  └──────────┘       │
│       ↑                                              ↓             │
│       └──────── ┌──────────┐ ──────── ┌──────────┐ ←┘              │
│                 │  GAUGE   │          │ RECOVERY │                  │
│                 │          │          │          │                  │
│                 └──────────┘          └──────────┘                  │
│                                                                    │
│   ┌──────────────┐    ┌──────────────────┐                        │
│   │ PILOT CHECKS │    │ TRANSITION HALL  │                        │
│   └──────────────┘    │ + TRIM BENCH     │                        │
│                       └──────────────────┘                        │
│   ┌─────────────┐   ┌──────────────┐    ┌─────────────────┐      │
│   │  LIBRARY    │   │   ARCHIVE    │    │  DECK THEATER   │      │
│   │ (research)  │   │ (notes view) │    │ (presentation)  │      │
│   └─────────────┘   └──────────────┘    └─────────────────┘      │
└───────────────────────────────────────────────────────────────────┘

Drawer (any area):
┌────────────────────────────────┐
│ THE FRAME WORKSHOP        [X]  │
│ Since last visit:              │  ← P1a delta banner
│   2 lab notes · 1 status flip  │
├────────────────────────────────┤
│ Items                          │
│  ▣ LAB-001  Frame form v1      │
│  ▣ LAB-010  Frame chapter      │
│  ◌ Frame practice v1 (gap)     │  ← P0c expected-but-missing slot
│  ◌ wildcat-frame-pattern       │  ← P0c ghost (referenced in note)
├────────────────────────────────┤
│ Notes (on the wall)            │
│  • Wildcat Frame example 4/30  │  ← P1b note placed in this area
│  • Dropped F/R/A/M/E acronym   │
└────────────────────────────────┘
```

The Backlog Wall is gone as a floor area — it's now the Priority view of the same items. The Archive is now a Timeline-style cross-area view of notes. Both of these are gains, not losses: rooms freed up, function improved.

---

## Updated data model deltas

Minimal. Most additions are sidecar fields:

```jsonc
{
  "areas": {
    "frame-workshop": {
      // existing fields...
      "expected_slots": [          // P0c gaps — what should exist here
        { "kind": "form",     "name": "Frame form v1" },
        { "kind": "chapter",  "name": "Frame chapter" },
        { "kind": "practice", "name": "Frame practice v1" }
      ]
    }
  },
  "items": {
    "LAB-001": {
      // existing fields...
      "lastTouched": "2026-04-30T18:00:00Z",   // P0a Timeline
      "ghost": false                            // P0c (true for ghost items)
    }
  },
  "notes": [
    {
      "id": "note-2026-04-30-wildcat",
      "area": "frame-workshop",                 // P1b spatial placement
      "date": "2026-04-30",
      "text": "..."
    }
  ],
  "ui": {
    "lastVisited": {                            // P1a since-last-visit
      "frame-workshop": "2026-04-29T07:30:00Z"
    }
  }
}
```

`ui.lastVisited` is localStorage-only, not exported.

---

## Open questions

Most of the original plan's open questions are answered by the research:

- **Naming** (Workshop / Station / Bay / Booth): keep. Diegetic naming is a feature.
- **Persistence model** (read-only vs. localStorage shadow): keep the localStorage shadow. Already shipped.
- **Gauge placement** (center vs. HUD): keep center. Persistent landmark.
- **Backlog Wall as area or per-room**: **answered** — neither. It becomes the Priority view.

Genuinely open:

1. **Ghost detection syntax.** `[[name]]` is wiki-standard but collides with markdown link syntax in some renderers. `>>name<<` is unambiguous but ugly. Or detect ghosts only by `LAB-###` IDs that don't resolve, and ignore plain-text mentions. Lean toward the last option for v0.2; revisit if the ghost surface feels thin.
2. **Promote-ghost flow.** Single click → real item with auto-filled brief, OR open a small modal so you can edit the title/area before promoting? Prefer single click; let the user edit afterward via inline edit (v0.3).
3. **Timeline view granularity.** Day-level (one row per day, items + notes touched that day) or item-level (one row per item, sorted by recency)? Day-level reads more like a logbook, which fits the lab metaphor.
4. **2.5D tilt as a default or opt-in.** Some users get queasy from tilted planes. Default flat for v0.2; add tilt as a settings toggle. Revisit defaults after a week of self-use.

---

## Sequence

1. **Ship P0a (view toggle)** first. Biggest design win, displaces the Backlog Wall, exercises the most of the data model. Single session.
2. **Ship P0b (Cmd-K)** second. Cheap, scales the lab, validates the toggle by giving users a way to find anything regardless of view.
3. **Ship P0c (gaps + ghosts)** third. The most game-flavored feature; will probably reshape how chapters cross-reference items. Two sessions.
4. **Use it for two weeks.** Real-world Frame cards, real lab notes, real status changes. The P1 features depend on observed patterns of revisit and note creation.
5. **Ship P1a (since-last-visit)** when the lab has accumulated enough activity to make it useful. Probably one session.
6. **Ship P1b (spatial notes)** when the Archive has gotten cluttered enough to feel like a list problem. Note migration is the bulk of the work.
7. **Ship P2 (2.5D tilt)** when everything else feels stable. Polish.
8. **Defer v0.3 (sync, Cowork integration, mini-views)** until v0.2 has earned its keep. The research is clear that adding cross-device synchrony before single-device usefulness is settled is a graveyard pattern.

---

## What success looks like

A tool the author opens daily without thinking about the tool itself. Frame card in the morning, status flips and lab notes during the day, a quick Timeline view in the evening to see what moved. Spatial recall handles 90% of "where does this live"; Cmd-K handles the 10% that doesn't. Empty slots and ghosts make "what's next" obvious without a separate planning ritual. The lab is a place that reflects the shape of what's been learned, with honest gaps visible at the edges of the map.

That's narrower than the Borgesian dream and broader than a flat task list — exactly the envelope the research defends.
