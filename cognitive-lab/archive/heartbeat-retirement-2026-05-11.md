# Heartbeat retirement — 2026-05-11

## Rationale

Heartbeat retired in favor of "the bookended day" as the second central image; the rhythm got absorbed into Pilot Check + Recovery as concrete instruments rather than a metaphor about them.

## Archived content

### Deleted area: the-gauge

```json
    {
      "id": "the-gauge",
      "name": "The Gauge",
      "type": "gauge / telemetry",
      "accent": "dark",
      "description": "The capacity instrument. Read at every boundary. Gates the day's mode. The continuous read-and-dispatch cycle (capacity ↔ restoration) is the framework's heartbeat.",
      "items": ["LAB-020","LAB-021","LAB-025","LAB-030"],
      "sources": [
        { "label": "Capacity Check-In (the live instrument)", "href": "capacity-checkin.html" },
        { "label": "turn-v0.1-map.html (slides 11 + 17, multi-signal model)", "href": "turn-v0.1-map.html" },
        { "label": "PROCESS.md (heartbeat as one of two central images)", "href": "PROCESS.md" }
      ],
      "experiments": [
        {
          "id": "exp-gauge-2026-05-02-heartbeat-named",
          "title": "Heartbeat named as second central image",
          "date": "2026-05-02 (afternoon)",
          "observation": "The give-and-take of capacity check ↔ restoration plan was named as the framework's meta-rhythm. Not just a phase — the rhythm that makes every phase work. Capacity reading dispatches: cleared (continue) or grounded (insert recovery, re-read). The cycle runs continuously, between every phase, across days.",
          "impact": "Now treated as one of two central images for the framework, alongside the cache-game (Frame's organizing metaphor). The cache-game designs the day; the heartbeat keeps you alive playing it. Captured as a chunk on this area; queued for integration into the deck (LAB-030)."
        },
        {
          "id": "exp-gauge-2026-05-02-merger-architecture",
          "title": "Capacity check-in + Pilot Check converge into unified Gauge",
          "date": "2026-05-02 (morning)",
          "observation": "The capacity check-in PoC and the Pilot Check Station are different views of the same instrument. Each is half-built; together they're the complete instrument. The PoC has felt-sense + bank metaphor + morning-after; the Pilot Check has three-dimension rule-out + targeted prescription. Naming them as separate areas was creating duplication.",
          "impact": "Architecture decided: merger queued as LAB-025 (Make the Gauge a workshop, embed capacity check-in). Pilot Check Station may dissolve into a use-pattern of the Gauge after the merger."
        }
      ],
      "chunks": [
        {
          "id": "chunk-hash-house-gauge-pilot-check",
          "title": "Hash house = Pilot Check visit (refuel, re-orient, decide)",
          "summary": "The lab's heartbeat IS the hash house. Pilot Check = hash-house visit: refuel, re-orient, decide whether to continue. A tightening of an existing instrument, not a new one.",
          "body": "In rogaining, the **hash house** is the central base camp. Racers return there to refuel, check time, re-orient, and decide whether to continue the current route or revise. Elite racers treat each hash-house visit as a decision point, not just a rest stop: they assess their capacity against remaining time and course, then commit or pivot.\n\nThe lab's Pilot Check is the hash house visit. The parallels are direct:\n\n- **Refuel** → capacity read (Cognitive / Emotional / Physical sliders).\n- **Re-orient** → Gauge dispatch (cleared or grounded) + diagnosis of which dimension is red.\n- **Decide whether to continue** → Full Turn vs. Partial Turn vs. Recovery insertion.\n\nThis framing tightens an instrument that already exists — it doesn't add a new one. The Gauge is the continuous instrument (between every phase); the Pilot Check is the explicit pre-leg hash-house visit (before a Full Turn starts).\n\nPractical implication: the Pilot Check form can be framed to the author as 'you're at the hash house — what's your read?' rather than 'complete this checklist.' The framing change may improve compliance on sessions where the operator is inclined to skip the check. The hash-house visit is non-optional in rogaining; that normative weight transfers.\n\nThe Debrief's 'Capacity + next' field closes the loop: post-leg gauge read = leaving the hash house for the next leg.\n\nCross-ref: chunk-gauge-heartbeat (The Gauge) — the heartbeat is the continuous rhythm; the hash house is the explicit check-in point within that rhythm."
        },
        {
          "id": "chunk-gauge-heartbeat",
          "title": "The heartbeat — capacity ↔ restoration as meta-rhythm",
          "summary": "The continuous Gauge-read-and-dispatch cycle is the framework's beating rhythm. Without it, the framework is just phases without honoring capacity.",
          "body": "The framework has two central images. The cache-game (Jess's contribution) names how the day's game gets designed — Frame as the game-design moment. The heartbeat names how the day's rhythm cycles.\n\nThe heartbeat: capacity check → action plan → capacity check → action plan. The Gauge reads, the result dispatches: cleared (continue with the planned phase) or grounded (insert recovery, re-read). The cycle runs continuously throughout the day, between every phase, across days.\n\nWith the heartbeat, every phase boundary is gated by capacity and every grounded reading dispatches a targeted recovery. Without it, the cycle just runs through phases regardless of state — and the framework collapses into ritual.\n\nThe Pilot Check is the explicit pre-flight version of the heartbeat (rule-out across cognitive / emotional / physical, dispatching recovery hours per red dimension). The Gauge is the continuous instrument the heartbeat runs on.\n\nThe two images compose. The cache-game is *how the day's game is designed.* The heartbeat is *how the day's rhythm cycles.* Neither alone is the framework; together they make the practice live."
        }
      ],
      "notes": [
        "The capacity check-in is the felt-sense layer of the Gauge. It's been doing real recovery-planning work and is the seed the Gauge grows from.",
        "2026-04-30 — The morning gauge worked (recovery turnaround)."
      ]
    }
```

### Deleted LAB items

```json
    "LAB-020": {
      "id": "LAB-020",
      "title": "Per-turn gauge entries (vs only per-day)",
      "status": "backlog",
      "priority": "P1",
      "area": "the-gauge",
      "brief": "Upgrade the gauge to record a reading at the start of each turn, not just daily.",
      "full": "Upgrade the gauge to record a reading at the start of each turn, not just once per day. This feeds the multi-signal model and enables intra-day capacity tracking."
    },
    "LAB-021": {
      "id": "LAB-021",
      "title": "Capacity check-in v0.2 (turn-aware data model)",
      "status": "backlog",
      "priority": "P1",
      "area": "the-gauge",
      "brief": "Rebuild the check-in PoC with a turn-aware data model.",
      "full": "Rebuild the capacity check-in PoC with a turn-aware data model. Each record tagged with turn ID, time-of-day, and which phase triggered the check-in. Enables correlation analysis between gauge readings and turn outcomes."
    },
    "LAB-025": {
      "id": "LAB-025",
      "title": "Make the Gauge a workshop (embed capacity check-in)",
      "status": "backlog",
      "priority": "P1",
      "area": "the-gauge",
      "brief": "Promote the Gauge from a regular area to a workshop, with the capacity check-in PoC embedded as the instrument view.",
      "full": "Same workshop pattern as Frame. Top half of drawer = the live instrument (capacity check-in PoC, embedded as iframe or directly merged), bottom half = the floor view (items, artifacts, notes, recent gauge readings as cards). Eventually adds the multi-signal layers (behavioral, temporal) on top of the felt-sense PoC. Architecturally, makes the PoC's daily ritual a first-class part of the lab rather than a side artifact."
    },
    "LAB-030": {
      "id": "LAB-030",
      "title": "Integrate the heartbeat into the deck",
      "status": "backlog",
      "priority": "P1",
      "area": "the-gauge",
      "brief": "Update deck slides to surface the heartbeat as the framework's second central image alongside the cache-game.",
      "full": "The framework now has two named central images. The cache-game is well-represented in the deck (Frame batches with subtitles tied to the metaphor). The heartbeat (capacity ↔ restoration as continuous meta-rhythm) is not yet in the deck. Update slides 11 and 17–18 (Gauge and multi-signal model) to name the heartbeat explicitly. Possibly add a slide that pairs the two images. Coordinates with chunk-gauge-heartbeat in the-gauge area."
    }
```

### Deleted heartbeat prose from LAB_CONTEXT.md

The heartbeat section was in `quenton-quince/LAB_CONTEXT.md` (lines 90–95) and `cognitive-lab/PROCESS.md` (lines 92–100). The `cognitive-lab/LAB_CONTEXT.md` file did not exist at the time of this retirement — the DECISIONS.md entry references the path the brief specified; see PR1 git log for context.

**From `quenton-quince/LAB_CONTEXT.md` (lines 90–95):**

```
### The heartbeat

The give-and-take rhythm of capacity check ↔ restoration. The Gauge reads, the result dispatches: cleared (continue) or grounded (insert recovery, re-read). This rhythm runs continuously, between phases, across days. Without the heartbeat, the framework is just phases without honoring capacity. With it, every boundary is gated and every grounded reading dispatches targeted recovery.

The Pilot Check is the explicit pre-flight version of the heartbeat (rule-out across cognitive / emotional / physical, dispatching recovery hours per red dimension). The Gauge is the continuous instrument the heartbeat runs on.
```

### Deleted heartbeat block from PROCESS.md

**From `cognitive-lab/PROCESS.md` (lines 92–100):**

```
### The heartbeat

The give-and-take rhythm of capacity check ↔ restoration. The Gauge reads, the result dispatches: cleared (continue) or grounded (insert recovery, re-read). This rhythm runs continuously throughout the day, between every phase.

Without the heartbeat, the framework is just phases without honoring capacity. With it, every boundary is gated by capacity and every grounded reading dispatches targeted recovery.

The Pilot Check is the explicit pre-flight version of the heartbeat (rule-out across cognitive / emotional / physical, dispatching recovery hours per red dimension). The Gauge is the continuous instrument the heartbeat runs on.

**Together:** The cache-game is *how the day's game is designed* (Frame's metaphor). The heartbeat is *how the day's rhythm cycles* (the Gauge↔Recovery meta-rhythm). They compose; neither alone is the whole framework.
```

### Deleted chunk: chunk-gauge-heartbeat

```
{
  "id": "chunk-gauge-heartbeat",
  "title": "The heartbeat — capacity ↔ restoration as meta-rhythm",
  "summary": "The continuous Gauge-read-and-dispatch cycle is the framework's beating rhythm. Without it, the framework is just phases without honoring capacity.",
  "body": "The framework has two central images. The cache-game (Jess's contribution) names how the day's game gets designed — Frame as the game-design moment. The heartbeat names how the day's rhythm cycles.\n\nThe heartbeat: capacity check → action plan → capacity check → action plan. The Gauge reads, the result dispatches: cleared (continue with the planned phase) or grounded (insert recovery, re-read). The cycle runs continuously throughout the day, between every phase, across days.\n\nWith the heartbeat, every phase boundary is gated by capacity and every grounded reading dispatches a targeted recovery. Without it, the cycle just runs through phases regardless of state — and the framework collapses into ritual.\n\nThe Pilot Check is the explicit pre-flight version of the heartbeat (rule-out across cognitive / emotional / physical, dispatching recovery hours per red dimension). The Gauge is the continuous instrument the heartbeat runs on.\n\nThe two images compose. The cache-game is *how the day's game is designed.* The heartbeat is *how the day's rhythm cycles.* Neither alone is the framework; together they make the practice live."
}
```

## See also

PR1 in `git log`. DECISIONS.md entry 2026-05-11.
