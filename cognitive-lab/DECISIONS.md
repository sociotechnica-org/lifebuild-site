# Cognitive Lab — Decisions Log

Synthesized cross-cutting record of major design calls, with reasoning. Per-area Log entries in the lab capture the lived data; this file captures the *why* behind the framework-level decisions.

Entries are reverse-chronological (newest first). Each has: date, decision, reasoning, status, references.

---

## 2026-05-04 · Phase 5 click-throughs and Sync form deferred to backlog

**Decision.** Phase 5 of the rogaine-spine arc ships the Snap Circuit Leg view in read-only form. Click-through wiring (zone → form/drawer) and the Sync station form are explicitly deferred.

**Reasoning.** The read-only board delivers the cognitive job (orientation at the leg scale) without requiring fully-built forms for every phase. Wiring click-throughs before all target forms exist would create dead-end interactions. The deferred items are scoped as LAB-037 (click-throughs) and LAB-035 (Sync form) — both P2, both unblocked by the current phase shipping cleanly.

**Status.** Active. LAB-037 and LAB-035 in backlog.

**References.** Commit `11c6cd1` (Phase 5 fixes), `cognitive-lab/cognitive-lab-v0.1.html` (LAB-035, LAB-037).

---

## 2026-05-04 · Course Coach named as future agent role

**Decision.** A future agent role — Course Coach — is named and scoped. It reads the current Course's `legs[]` array like poker hand histories and suggests better moves for the next leg's Frame.

**Reasoning.** Once 4–5 legs have completed Frame and Debrief sub-records, patterns become detectable: consistent over-scoping, frontier items that keep getting skipped, capacity mis-reads recurring on the same day-of-week. A poker-coach framing (reading hand histories, surfacing patterns, suggesting adjustments) is the right shape. Whether it's a sub-agent or top-level agent is a design call for Quenton — deferred until leg-history depth accumulates.

**Status.** Active (spec only). Implementation queued as LAB-034, P2.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (LAB-034, chunk-course-tier-spec).

---

## 2026-05-04 · Bruner / Snap Circuits design language adopted

**Decision.** The lab's design language is explicitly Bruner-grounded: push every representation from symbolic toward iconic and enactive. Hex Map (Course/week scale) and Snap Circuit board (Leg/turn scale) are the first two implementations. All subsequent visual decisions are evaluated against this standard.

**Reasoning.** The lab as built is heavily symbolic — text fields, JSON, written labels. Bruner's three modes (enactive / iconic / symbolic) name the gap. Alan Kay: "constructing a diagram is much less difficult than reading one." WS004 ("Beyond the Symbolic") established the Snap Circuits analogy for AI agent composition — a child snapping components is performing the architecture, not reading about it. The rogaine-spine arc brought that analogy into the lab's own UI: the five-zone circuit board makes the turn structure tactile. Every new view now starts with the question: what is the iconic/enactive equivalent of what we're expressing symbolically?

**Status.** Active. Applies to all future lab UI work.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-bruner-snap-design-language), WS004, commits `c554317` (Hex Map), `21f4cdc` (Snap Circuit board).

---

## 2026-05-04 · Two-tier visualization split (Hex Map for Course/Map, Snap Circuits for Leg)

**Decision.** The lab uses two distinct visualizations that do different cognitive jobs and don't overlap: Hex Map for the Course/week scale; Snap Circuit board for the Leg/turn scale.

**Reasoning.** A single visualization trying to show both week-level terrain and leg-level wiring would either be too dense or too abstract. The split lets each metaphor do its native job cleanly: the Hex Map gives bird's-eye terrain orientation (where is the work, what's in fog, what's glowing P0); the Snap Circuit board gives signal-flow orientation (how does this leg wire together, which zones are live). The two compose — you consult the map to know the week, you consult the circuit to run the leg.

**Status.** Active. Hex Map v0.1 (read-only) and Snap Circuit board v0.1 (read-only) shipped. v0.2 interaction queued as LAB-041 and LAB-037.

**References.** Commits `c554317` (Hex Map), `21f4cdc` (Snap Circuit board), `cognitive-lab/cognitive-lab-v0.1.html` (chunk-hex-map-course-view-v01, chunk-snap-circuit-leg-view).

---

## 2026-05-04 · Frontier-not-itinerary as the Course planning call

**Decision.** A Course names what is *reachable* this week — items on `course.frontier[]` — not which leg hits which item. Per-leg Frame picks from the frontier at turn-start. Debrief feeds back via `changes_to_course`.

**Reasoning.** The itinerary version (leg 1 = items A+B, leg 2 = C+D) violates the rogaine condition: the racer doesn't plan checkpoints in order; they choose dynamically based on terrain and capacity. An itinerary creates guilt debt and stale plans. A frontier creates feedback loops — each leg's Frame is a real-time route decision against current conditions. Quenton's formulation: "The Course names the terrain. The racer picks the route." The design also solves the self-imposed-constraint problem: a well-set frontier is genuinely larger than any seven legs can reach, preserving real selectivity at planning time.

**Status.** Active. Implemented in the Course data model.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-frontier-vs-itinerary, chunk-course-tier-spec, chunk-course-setter-problem-self-set).

---

## 2026-05-04 · "7 leg courses" naming locked to book title

**Decision.** The canonical week-scale unit is a **7 leg course**. One Full Turn = one leg. One ISO week = one Course (7 legs). The naming is locked to the book title *The 7 Turn Work Week*.

**Reasoning.** The three-tier model (Course → Leg → Phase) embeds the book's central claim in the data architecture. "Turn" and "leg" are synonyms at the turn scale — "leg" is the rogaine vocabulary for a segment of a larger course, making the metaphor structurally consistent. The ISO-week Course ID convention (`YYYY-WNN`) is unambiguous and human-readable. Locking the naming to the book title makes every Course in the lab a lived proof point of the book's argument.

**Status.** Active. Locked 2026-05-04.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-7-leg-courses-naming), branch `danversfleury/lab-course-tier`.

---

## 2026-05-04 · Course tier added (three-tier data model: Map → Course → Leg)

**Decision.** The lab's data model gains a third tier above the existing phase-level records: Map (the lab itself) → Course (one ISO week, 7-leg arc) → Leg (one Full Turn, wrapping Frame · Comprehend · Sync · Produce · Debrief sub-records).

**Reasoning.** The structural realization: each lab station (Frame, Comprehend, Sync, Produce, Debrief) isn't a separate form/function — there's a **unit of work** flowing through every phase. Danvers brought a deep research brief on rogaining (the Australian orienteering sport) and proposed that knowledge work is best modeled as a turn-based rogaine. A turn = a "leg" (one Full Turn). A week = a "7 leg course" — locked to the book title. The three-tier model resolves a prior architecture mismatch: the Frame card was being treated as a filing artifact (save and archive), when its real job is to *start a leg*. Every later station is a different lens on the same underlying unit of work. The Leg record wraps all five sub-records and stays open until Debrief closes it.

**Status.** Active. Phase 1–5 of the rogaine-spine arc implemented and merged on branch `danversfleury/lab-course-tier` (11 commits beyond main as of 2026-05-04).

**References.** Commits `a377f9b` through `11c6cd1`, `cognitive-lab/cognitive-lab-v0.1.html` (chunk-course-tier-spec, chunk-7-leg-courses-naming, chunk-course-as-spine-station-as-lens).

---

## 2026-05-02 · Two-role agent split — Quenton (design) / Larry (operations)

**Decision.** Two distinct AI agents for working in the lab, each with its own companion folder following the Zelda/ghostwriter pattern.

- **Quenton Quince** — design collaborator. Co-architects, pushes back, names tradeoffs.
- **Larry Moleman** — lab assistant. Captures, files, maintains hygiene, suggests but doesn't decide.

**Reasoning.** Earlier conversations mixed two cognitive shapes: high-variance design work and low-variance operational work. Splitting the roles lets each be optimized: Quenton runs on Opus (design judgment), Larry runs on Sonnet (reliable execution). Both route deeper work to existing agents (Zelda, ghostwriter, grepzilla2).

**Status.** Active. PR #123 merged.

**References.** `quenton-quince/`, `larry-moleman/`.

---

## 2026-05-02 · Two central images for the framework

**Decision.** The framework has two organizing metaphors, both with research backing, both surfaced through lived practice:
- **The cache-game** — Frame's organizing metaphor (set the field / set the scoring / set the plan / set the endgame)
- **The heartbeat** — the Gauge↔Recovery rhythm that runs across all phases

**Reasoning.** Earlier the cache-game was treated as Frame-only. The heartbeat insight (capacity check → restoration plan, in continuous cycle) named the meta-rhythm that makes every phase work. Both images compose: cache-game designs the day; heartbeat keeps you alive playing it.

**Status.** Active. To propagate into chapter material as the framework's central images.

**References.** Captured in `cognitive-lab/PROCESS.md`. Cache-game origin: Jess's adventure-caching race story.

---

## 2026-05-02 · Capacity check-in + Pilot Check converge into unified Gauge

**Decision.** The capacity check-in PoC and the Pilot Check Station are different views of the same instrument. They merge into a unified Gauge instrument over time.

**Reasoning.** The PoC has features the Pilot Check doesn't (morning-after test, withdrawal/replenishment bank, color verdict, history). The Pilot Check has features the PoC doesn't (three-dimension breakdown, rule-out threshold, targeted prescription). Each is half-built. Together they're the complete instrument. The author named the convergence; coexistence as separate tools would be the duplication trap.

**Status.** Architecture decided; merger queued as **LAB-025** (Make the Gauge a workshop, embed capacity check-in). Work is post-current-period.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (item LAB-025), `larry-moleman/PLAYS.md` (Merge-Duplicate-Tools play).

---

## 2026-05-02 · Pilot Check is rule-out, not measurement

**Decision.** Pilot Check follows the IM SAFE pattern — kill-switch checklist, not fitness scan. Three-dimension rule-out (cognitive king / emotional / physical), 1–10 sliders, threshold ≤3 = grounded. Output dispatches a winged prescription: 1 hour workday recovery per red dimension.

**Reasoning.** The first wildcat asked five fitness-measurement questions; the author caught the wrong shape. Aviation IM SAFE doesn't ask "are you peak?" — it asks "is anything deep-red enough to ground you?" Tender / tired / tense don't ground; overwrought / exhausted / sick do. The three dimensions come from the Book 1 capacity chapter (emotional / mental / physical).

**Status.** Active. Pilot Check Station is now a workshop with the prototype.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (pilot-check-station area, items LAB-007 / LAB-008), Book 1 capacity chapter.

---

## 2026-05-01 · Frame v0.2 four-batch structure (Scope / Outcome / Approach / Safety)

**Decision.** Frame's seven fields organize into four cognitive-flow batches:
- **Scope** (Doing / Not Doing)
- **Outcome** (Done means / Bonus)
- **Approach** (How I'll work)
- **Safety** (What ruins this / When to stop)

Each batch has a subtitle that names the cache-game move (set the field / set the scoring / set the plan / set the endgame).

**Reasoning.** The acronym-driven sequence (F.R.A.M.E.) forced fields into an unnatural order. Removing the acronym surfaced the natural cognitive flow: scope first (boundaries), then outcome (target), then approach (method), then safety (stop conditions). Side-by-side Doing/Not Doing supports natural iteration between the two as the author defines the day's edges.

**Status.** Active. Frame form v0.2 shipped, lived-tested.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (frame-workshop area), `cognitive-lab/frame-research-and-practice.md` (Section 6 — worked example).

---

## 2026-05-01 · End-as-Time+Temptation pattern

**Decision.** When-to-stop captures two components: time (the bingo fuel — set when fresh) AND the temptation you're pre-committing to resist when it arrives.

**Reasoning.** The author's first formal Frame on 2026-05-01 surfaced this unprompted: *"Work ends at 4:30 today. I need to have the discipline to put this down even though I'm so excited."* The temptation line is bingo-fuel in plain language — naming the bright-red trap in advance, while fresh, before in-the-moment dopamine outvotes the pre-commitment.

**Status.** Active in Frame v0.2 prompt. Candidate for splitting into a separate field in v0.3 (LAB-028).

**References.** Author's 2026-05-01 12:29 Frame card.

---

## 2026-05-01 · Renamed Push → Produce in lab display

**Decision.** The Push phase displays as "Produce" in the cognitive lab (data ID stays `push-bay` for stable links).

**Reasoning.** "Push" connoted aggressive effort; "Produce" connotes making things. The author noted "it's more factory, it's produce" — the right metaphor for the phase in AI-native work where the human's job is judgment + production, not raw effort.

**Status.** Active in lab. Framework docs (deck, phases-and-leverage) still use "Push" — to be reconciled if the rename sticks across a few weeks of lived use.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (push-bay area, name field).

---

## 2026-04-30 · Dropped F/R/A/M/E acronym

**Decision.** Abandon the F.R.A.M.E. acronym (Focus / Range / Approach / Miss / End). Use plain-English field labels in natural cognitive order.

**Reasoning.** The acronym was clever but constrained the field sequence. Naming was overshadowing structure. The author's instruction: build the infrastructure first, name it later. We can earn a name once the form has stabilized — we haven't yet.

**Status.** Active. Plain-English labels (Doing / Not Doing / Done means / Bonus / How I'll work / What ruins this / When to stop) shipped in Frame v0.2.

**References.** `quenton-quince/PLAYS.md` (Drop-the-Acronym play).

---

## 2026-04-30 · Renamed Ledger → Gauge in framework

**Decision.** The capacity instrument in Book 2's framework is **the Gauge**. The name "Ledger" is reserved for Alexandria (the AI-native operating system, separate product).

**Reasoning.** Alexandria's three core artifacts are Library / Playbook / Ledger. To avoid name collision and confusion between the two systems, the cognitive load framework's instrument is renamed.

**Status.** Active. All framework docs use "Gauge."

**References.** `cognitive-lab/turn-v0.1-map.html` (the deck), `cognitive-lab/turn-v0.1-phases-and-leverage.md`.

---

## 2026-04-30 · Adopted Must/Stretch refinement of Focus

**Decision.** Frame's outcome field splits into two: **Must** (the floor, single-shielded goal) and **Stretch** (bonus pickups, conditional on time and capacity).

**Reasoning.** Driven by Jess's bike-race metaphor — adventure-caching where you have a hard finish-line deadline plus scoring along the way. Failure modes: greedy (max pickup → don't finish) and conservative (finish early → leave points). The skill is calibrating the spectrum. Goal-shielding research backs the split: a single primary goal shields downstream attention; secondary goals are opportunistic only if named in advance.

**Status.** Active. Renamed in v0.2 to "Done means" + "Bonus" but the architecture is unchanged.

**References.** `cognitive-lab/frame-research-and-practice.md` (Section 3 — Stretch chunk).

---

## 2026-04-30 · Days are reporting periods, turns are work units

**Decision.** A turn is a work unit; a day is a reporting period. They're orthogonal. A turn can span sleep (path D in the deck).

**Reasoning.** Sleep is a special mandatory Recover insertion that doesn't necessarily end a turn. Work that ends on Sync at 6pm can continue with Push at 8am if the morning gauge passes. The capacity check-in stays anchored to days (post-sleep gauge read = morning-after test); turn-level data joins per-day data rather than replacing it.

**Status.** Active. The 7 Turn Work Week title still works (7 turns/week as a target rhythm, not 7 days × 1 turn).

**References.** `cognitive-lab/turn-v0.1-map.html` (deck slide on Path D).

---

## 2026-04-30 · Three-signal capacity model adopted

**Decision.** The Gauge alone (felt sense) is insufficient. Capacity is read across three signal types:
- **Felt sense** — subjective reading; reliable when low, unreliable mid-task in compensatory mode
- **Behavioral** — observable indicators (decision speed, irritability, breath, posture); reliable continuously with practice
- **Temporal** — clock-based (time-on-task, sleep debt, time-since-meal); always reliable; doesn't adapt to today's actual capacity

**Reasoning.** Compensatory effort under high demand suppresses the felt-sense signal exactly when you need it most (Hockey 1997). Aviation uses multiple instruments for the same reason: IM SAFE (felt), duty-time limits (temporal), crew cross-check (behavioral). The system trusts no single signal.

**Status.** Active. Implemented as the three-dimension Pilot Check (cognitive / emotional / physical mapping onto behavioral observation across mind, mood, body).

**References.** `cognitive-lab/turn-v0.1-map.html` (deck slides 17–18), `cognitive-lab/turn-v0.1-phases-and-leverage.md` (Pilot Check section).

---

## 2026-04-30 · Phase categories — required / conditional / insertable

**Decision.** The six phases sort into three categories:
- **Required** (Frame, Debrief) — always run; the bookends
- **Conditional** (Comprehend, Sync, Push) — run only when preconditions are met; can collapse or skip
- **Insertable** (Recover) — available anywhere; sleep is special

**Reasoning.** The earlier model treated phases as a fixed sequence. Lived experience showed the structure adapts: solo work skips Sync; cold-start with no agents shortens Comprehend; depleted reserves defer Push. The categorization names the rules of when each phase runs.

**Status.** Active. Implemented as workshop categories in the lab; rendered visually in the four-act deck.

**References.** `cognitive-lab/turn-v0.1-map.html` (deck slides 12–15).

---

## 2026-04-29 · Phase library — Frame · Comprehend · Sync · Push · Debrief · Recover

**Decision.** The Turn has six phases.

**Reasoning.** Original four-phase model (Comprehend / Sync / Push / Recover) was missing demand-reduction (now Frame) and in-cycle measurement (now Debrief). Adding both makes the cycle a complete regulation loop (reduce demand → regulate during → measure → recover after).

**Status.** Active. Foundation of the framework.

**References.** `cognitive-lab/turn-v0.1-phases-and-leverage.md`.

---

## 2026-04-29 · Four-act narrative structure for the deck

**Decision.** The deck for *The 7 Turn Work Week* has four acts:
- **Act I — The new pace of work** (knowledge work was batched; AI made it continuous; AI-fluent people are breaking first)
- **Act II — Why batch tools fail** (continuous flow needs continuous management; ATC analogy; symptoms)
- **Act III — Borrowed wisdom** (continuous flow isn't new; the science already exists)
- **Act IV — The framework** (match activity to capacity; the Gauge; the phase library; the cycle composes; where to start)

**Reasoning.** Earlier drafts assumed reader context. The four-act structure works for a beginner-facing presentation: setup → diagnosis → research → solution. Borrowed industries (aviation, naval, manufacturing, medicine, sport) anchor the framework as translation rather than invention.

**Status.** Active. 21-slide deck shipped.

**References.** `cognitive-lab/turn-v0.1-map.html`.

---

## How to add an entry

When a framework-level decision is made (or a substantial design call surfaces), add an entry here with:

- **Date.**
- **Decision** — one-paragraph summary of what was decided.
- **Reasoning** — why this over the alternatives. Cite the lived example or research that drove it.
- **Status** — active / superseded / deprecated. If superseded, link the entry that replaced it.
- **References** — files, items, conversations.

Entries are reverse-chronological. Don't edit prior entries when a decision is superseded — add a new entry that supersedes the old one and update the Status field of the original.

This file is durable. Per-area Log entries in the lab are operational; this is the framework-level reasoning trail.
