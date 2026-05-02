# Cognitive Lab — Process

How the lab works as a living system: who plays which role, how the agents compose, how the lab feeds the book, and the rhythm that holds it all together.

---

## The roles

The lab has six roles. One human, five AI agents.

| Role | Who | What they do |
|---|---|---|
| **Author / Director** | The human (Danvers) | Designs the framework, runs the practice, makes priority and naming calls, approves architecture, owns the book's voice |
| **Quenton Quince** | `.claude/agents/quenton-quince.md` | Design collaborator — co-architects with the author, pushes back, names tradeoffs, builds artifacts together when green-lit |
| **Larry Moleman** | `.claude/agents/larry-moleman.md` | Lab assistant — captures, files, records, maintains hygiene, polishes prose lightly, suggests but doesn't decide |
| **Zelda** | `.claude/agents/zelda.md` | Developmental editor for the book — chapter analysis, controlling-idea work, structural diagnosis |
| **ghostwriter** | `.claude/agents/ghostwriter.md` | Voice-matched copywriter — turns chapter-shaped chunks into final prose in the labnotes register |
| **grepzilla2** | `.claude/agents/grepzilla2.md` | Code/content review for the broader Astro site |

The split between Quenton (design) and Larry (operations) is the most important one inside the lab itself. The split between the lab (Quenton + Larry) and the book (Zelda + ghostwriter) is the most important one in the broader system.

---

## How the agents compose

A typical full session, from start to finish:

```
┌─────────────────────────────────────────────────────────────────┐
│  AUTHOR runs Pilot Check → cleared. Frames the turn.             │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  AUTHOR + QUENTON design — propose, push back, build artifacts.  │
│  Output: lab updates, chunk additions, decisions made.           │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  QUENTON hands off to LARRY for operational follow-up:           │
│   - Capture session decisions as Log entries                     │
│   - Update item statuses                                         │
│   - Cross-reference deck and docs                                │
│   - Suggest priority drift if any surfaced                       │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  AUTHOR runs Debrief at end of turn. Captures lived data.        │
│  Bingo time hits → close.                                        │
└─────────────────────────────────────────────────────────────────┘
```

When the work moves toward the book, the flow extends:

```
LAB CHUNKS (in workshop area's Chapter tile)
    │
    │  When a chunk reaches "ready for prose"
    ▼
GHOSTWRITER (voice-matched draft in labnotes register)
    │
    │  Draft lands in src/content/book/ or as chapter draft
    ▼
ZELDA (chapter analysis, reverse outline, structural feedback)
    │
    │  Revision directives back to ghostwriter or author
    ▼
PUBLISHED CHAPTER
```

Quenton and Larry don't write chapter-final prose. The chunks they help shape are inputs to ghostwriter and Zelda.

---

## The two central images

The framework has two organizing metaphors. Both have research backing. Both surfaced through lived practice.

### The cache-game

Originated from Jess's adventure-caching race story. Frame is the *game-design* moment — you're setting the rules of play for the day's game. The four batches map to four game-design moves:

- **Set the field** (Scope: Doing / Not Doing) — what's playable today, what's off
- **Set the scoring** (Outcome: Done means / Bonus) — high-value catches, bonuses
- **Set the plan** (Approach: How I'll work) — strategy
- **Set the endgame** (Safety: What ruins this / When to stop) — the three ways the day ends

Three end-states: collected enough → finish line; tired/hurt with what you got → head home early; time runs out → buzzer. These map to End's three triggers (Done means delivered, capacity floor, bingo time).

### The heartbeat

The give-and-take rhythm of capacity check ↔ restoration. The Gauge reads, the result dispatches: cleared (continue) or grounded (insert recovery, re-read). This rhythm runs continuously throughout the day, between every phase.

Without the heartbeat, the framework is just phases without honoring capacity. With it, every boundary is gated by capacity and every grounded reading dispatches targeted recovery.

The Pilot Check is the explicit pre-flight version of the heartbeat (rule-out across cognitive / emotional / physical, dispatching recovery hours per red dimension). The Gauge is the continuous instrument the heartbeat runs on.

**Together:** The cache-game is *how the day's game is designed* (Frame's metaphor). The heartbeat is *how the day's rhythm cycles* (the Gauge↔Recovery meta-rhythm). They compose; neither alone is the whole framework.

---

## Satisficing mode

The framework is being built while being used. The build-the-plane-while-flying meta-frame:

- **v0.1 of the practice on day one of running it.** The wildcat Frame on 2026-04-30 was the design AND the first run.
- **Lab and book co-evolve.** The lab is where the practice lives; the book is where the practice gets explained. Both are in motion.
- **The framework's tools can be used to design themselves.** Frame designs Frame. Pilot Check assesses readiness to design Pilot Check.

This isn't a phase to graduate from. It's the working mode. New phases (Comprehend, Sync, Produce, Debrief, Recover) will follow the same pattern: wildcat first, form second, workshop third, chapter from chunks fourth.

When the practice has stabilized enough to publish, that's when ghostwriter and Zelda enter the flow. Until then: stay in the practice, capture what's learned, keep the lab honest.

---

## Daily / weekly rhythm

A loose target shape, not a rigid schedule:

**Daily (when working in the framework):**
1. Morning: **Pilot Check** at the day's threshold. Cleared → continue. Grounded → insert recovery, re-check.
2. **Frame** the turn (or pick up an in-flight turn that crossed sleep).
3. **Push** with the Frame card visible. Bingo time pre-committed.
4. **Debrief** at turn close. Capture in the Log. Update items.
5. **Recovery** until next turn (or sleep, the special Recover insertion).

**Weekly (loose):**
- Daily summaries (Larry's play) catch drift.
- Backlog review with the author — surface stale items, propose re-prioritizations.
- Cross-reference audit if framework changed substantially that week.
- A reflective Debrief over recent Log entries to surface patterns that should propagate to chunks.

**Per-PR or per-substantial-change:**
- Decisions log entry capturing what changed and why.
- Cross-reference audit to make sure docs, deck, and lab agree.
- Status hygiene (items shipped → live; items abandoned → archived).

---

## Where things live

| Artifact | Location |
|---|---|
| The lab itself | `cognitive-lab/cognitive-lab-v0.1.html` |
| Capacity check-in PoC | `cognitive-lab/capacity-checkin.html` |
| The deck | `cognitive-lab/turn-v0.1-map.html` |
| Phase / leverage research doc | `cognitive-lab/turn-v0.1-phases-and-leverage.md` |
| Hacks-today (satisficing practice) | `cognitive-lab/turn-v0.1-hacks-today.md` |
| Frame research-and-practice | `cognitive-lab/frame-research-and-practice.md` |
| Lab plan & spec | `cognitive-lab/cognitive-lab-plan.md`, `cognitive-lab-spec.md` |
| Decisions log | `cognitive-lab/DECISIONS.md` |
| This process doc | `cognitive-lab/PROCESS.md` |
| Quenton's brain | `quenton-quince/` |
| Larry's brain | `larry-moleman/` |
| Zelda's brain | `zelda/` |
| ghostwriter's brain | `ghostwriter/` |
| grepzilla2 | `.claude/agents/grepzilla2.md` |
| Book chapter prose | `src/content/book/` |
| Chapter metadata | `src/data/bookChapters.ts` |

---

## When this process changes

This document is durable but not frozen. Update it when:

- A new agent role joins the system (with what they do, where they fit).
- The lab → book flow changes (e.g., when chunks become directly editable as chapter drafts, the ghostwriter step may shift).
- The two central images expand (a third metaphor earns its keep).
- A new phase becomes a workshop, changing the typical session shape.

Track changes in `DECISIONS.md` so the reasoning trail survives.
