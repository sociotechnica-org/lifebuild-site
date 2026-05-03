# Cognitive Lab — Decisions Log

Synthesized cross-cutting record of major design calls, with reasoning. Per-area Log entries in the lab capture the lived data; this file captures the *why* behind the framework-level decisions.

Entries are reverse-chronological (newest first). Each has: date, decision, reasoning, status, references.

---

## 2026-05-03 · Priority spec — turn-based P0, hard cap of 3, surface merge

**Decision.** P0 means "next up to bat or at bat for the upcoming or current Produce phase." Hard cap of 3 P0s across the whole lab, no override. The toolbar Priority view is the canonical priority surface; the Backlog Wall floor tile retires. Priority shifts happen at turn boundaries (Frame picks the P0s; Debrief retires/demotes/stages). Continuation across turns is carried by the status badge (in-progress/drafted = at bat; backlog on a P0 = next up to bat) — no new priority tier needed.

**Reasoning.** The lab had accumulated P0s without enforcement. Cognitive load management means not having 25 open to-dos — extraneous load reduction is the highest-ROI cognitive intervention (Sweller CLT). A hard cap isn't a flexibility constraint; it's the mechanism. Override-as-data sounds reasonable until the fourth P0 is just as urgent as the first three, which means priority has collapsed back into a flat list. The turn-unit framing keeps priority honest: if it's not in the next or current Produce, it's not P0.

**Status.** Active. Spec captured in chunk-priority-spec-v0.1 on director-desk. In-app enforcement queued as LAB-035 (post-Debrief). Backlog Wall tile retirement queued as LAB-034.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-priority-spec-v0.1, director-desk area), LAB-034, LAB-035.

---

## 2026-05-03 · Three Done flavors — completion, milestone, effort

**Decision.** Frame's Done means field carries three named flavors: completion (full delivery), milestone (a bar crossed, more remains), effort (the Push happened; output is what moved). Each is a legitimate Done shape. The Frame card names which flavor applies per slot. Selection-over-generation argument: a three-way pick is lower-load and more precise than free-text description of what "done" means.

**Reasoning.** Knowledge work produces heterogeneous Done shapes. Forcing all done conditions into a single implicit model (delivery = done) produces wrong reconciliations at Debrief — an effort-based turn looks like a failure if measured against a completion standard. Naming the flavor in Frame lets Debrief reconcile on the right dimension: completion verifies delivery, milestone verifies bar-crossing, effort verifies the Push happened and what moved. The flavor vocabulary also extends the selection-over-generation principle from "what item" (the picker) to "what kind of done" (the flavor).

**Status.** Active. Shipped in LAB-027 v3. Per-flavor Debrief reconciliation shape deferred to LAB-032 v0.2 (LAB-045).

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (frame-workshop experiments: exp-frame-2026-05-03-done-flavors), LAB-027, LAB-045.

---

## 2026-05-03 · Persistence server adopted — Option A (local server with write endpoint)

**Decision.** lab-server.py (local Python server, 172 lines) is the durable persistence layer for the lab. Endpoints: /api/save (writes to cognitive-lab/exports/), /api/load (returns saved state on init). localStorage remains the fast read layer; the server is the durable write layer.

**Reasoning.** Three options evaluated: (A) local server with write endpoint, (B) File System Access API (browser-native file write), (C) session-close auto-export. The trigger was a concrete data loss: the 2026-05-01 12:29 Frame card content was lost when the dev server port changed — localStorage is per-origin (protocol + hostname + port). Option A is the most transparent, survives port changes, requires no browser permission dialogs (FSA API requires a permission grant per file), and enables import/export round-trips. Option C was rejected because discipline-based saves fail at the worst moment (when the session is ending and the author is depleted).

**Status.** Active. Shipped in PR #128. Shadow persistence (chunks, experiments, item statuses) still localStorage-only; queued for server v0.2 as LAB-036.

**References.** `cognitive-lab/lab-server.py`, `cognitive-lab/exports/.gitkeep`, LAB-036.

---

## 2026-05-03 · LAB-027 sequencing — v2 picker → v2.5 cap+notes → v3 Approach unfold

**Decision.** LAB-027 shipped in three phases in a single session: v2 (priority-sorted picker replacing free-text Done means; refs persist as [{id, title}] arrays), v2.5 (hard cap of 3, at-cap UI states with counter + dimmed rows + disabled Browse button, field-level optional notes textarea `must_notes`), v3 (per-slot Approach unfold with four prompts: Mode, Leaning on, AI/people, Done this turn; three Done flavors as inline placeholder; auto-expand on pick and on load with data; view-mode read-only).

**Reasoning.** Each phase was a precondition for the next. The picker without a cap would let the Director add unlimited P0s — the cap validates the picker. The per-slot Approach without a cap would be potentially boundless. The sequencing honored the cleanup-before-upfit principle: each version was shippable before the next was built, not a big-bang rebuild.

**Status.** Active. LAB-027 status → drafted (form ships; live after author runs first real Frame using it end-to-end).

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (frame-workshop experiments: exp-frame-2026-05-03-done-flavors, exp-frame-2026-05-03-v3-design-calls), LAB-027.

---

## 2026-05-03 · LAB-032 v0.1 shipped — per-flavor reconciliation deferred to v0.2

**Decision.** Debrief Workshop v0.1 form bootstrapped: Subject field + six probe fields, card history, save/edit/delete state machine. Preliminary process chunk (chunk-debrief-preliminary-process) filed on debrief-booth. Per-flavor Debrief reconciliation (the "Where they diverged" field adapting to completion/milestone/effort flavor) deferred to v0.2 (LAB-045) — lands when LAB-032 picker integration arrives.

**Reasoning.** The v0.1 form can run with free-text reconciliation. The per-flavor shape is the right design but requires stable Frame card flavor data to be meaningful. Build the thing that runs first; refine with lived data.

**Status.** Active. LAB-032 status → drafted (form runnable; live after first real Debrief runs end-to-end through it).

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (debrief-booth chunks: chunk-debrief-preliminary-process), LAB-032, LAB-045.

---

## 2026-05-03 · Quenton's three design calls for LAB-027 v3

**Decision.** Three Quenton design calls for the per-slot Approach unfold: (1) Schema-flat — Approach data nests inside the Done means chip object, not a parallel array. (2) UI-inline-expand — Approach unfolds inline under each chip on click, not side panel or modal. (3) Bonus-no-unfold — Bonus slots don't get per-slot Approach; their Approach is captured in the top-level How I'll work field.

**Reasoning.** Schema-flat keeps the Frame card a single readable record without cross-referencing. Inline-expand preserves spatial context. Bonus-no-unfold is the right scope: Bonus items are opportunistic pickups with no committed Done shape; per-slot Approach is for Must-equivalent items (Done means slots) that carry committed deliverable shapes.

**Status.** Active. These three calls constrain LAB-027 v4 (LAB-039).

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (frame-workshop experiments: exp-frame-2026-05-03-v3-design-calls), LAB-039.

---

## 2026-05-03 · Re-immerse phase named as Debrief design constraint

**Decision.** Same-session Debrief = consolidation (operator warm on the work; re-immerse skips). Multi-day-later Debrief = reconstruction-then-consolidation (operator spun up on context but cold on detail; re-immerse mandatory). These are structurally different Debrief modes, not just a phase that's sometimes fast. Exit criterion: operator says "I've settled the truth."

**Reasoning.** The presentation-shape finding (exp-debrief-2026-05-03-reimmerse-presentation-shape) named the output shape. This decision promotes the re-immerse phase from "phase listed" to "named design constraint" — the cognitive model behind the split is now explicit. Without the reconstruction pass in multi-day cases, the Phase 2 probe-field answers are built on misremembered produce-stage details and the reconciliation is unreliable.

**Status.** Active. chunk-debrief-preliminary-process Phase 1 section updated to reflect the named constraint.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (debrief-booth experiments: exp-debrief-2026-05-03-reimmerse-constraint-named, exp-debrief-2026-05-03-reimmerse-presentation-shape).

---

## 2026-05-03 · Selection-over-generation expanded — "speak in the language of the job at hand"

**Decision.** The Selection-over-generation principle in quenton-quince/PRINCIPLES.md expanded with a second lived example. The new text covers: (1) the entry-point case (Done means picker: without it, Done is invented each time; with it, it's chosen from named/prioritized items), (2) vocabulary selection as a form of selection-over-generation (Done flavors, Mode picker), (3) the Frame ← Debrief chain (structured Frame data is a precondition for automated Debrief comparison; free-text Frame cards produce manual reconstruction). The principle name stays "Selection over generation" — no new separate principle created.

**Reasoning.** Quenton recommended expanding the existing principle rather than creating a new "Speak in the language of the job at hand" principle. The lived example is operational, not voice-final, so Larry handled the write-up; no ghostwriter routing needed.

**Status.** Active.

**References.** `quenton-quince/PRINCIPLES.md` (Selection-over-generation entry).

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
