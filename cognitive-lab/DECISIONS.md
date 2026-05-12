# Cognitive Lab — Decisions Log

Synthesized cross-cutting record of major design calls, with reasoning. Per-area Log entries in the lab capture the lived data; this file captures the *why* behind the framework-level decisions.

Entries are reverse-chronological (newest first). Each has: date, decision, reasoning, status, references.

---

## 2026-05-11 · Frame form rollback — picker / Bonus / per-card Approach ripped from rendered form

**Decision.** The Outcome-batch picker (Done means as typed-ref multi-select with cap), Bonus field, per-slot Approach unfold, free-text fallback, Course/Full-lab scope toggle, and day-level "How I'll work — overall" scaffold are removed from the rendered Frame form. The form returns to plain textareas across all four batches. The Outcome batch now pairs **Done means** with **What ruins this** (its both/and twin); the Safety batch keeps only **When to stop**. Batch subtitles rewritten across all four. Saved-card schema is preserved silently — legacy `must`-as-array, `stretch`, `must_notes`, and per-slot ref fields stay in localStorage; old chips still route to the lab item via the viewing-mode click handler, but the picker form is no longer rendered.

**Reasoning.** Selection over generation is the right *long-run* shape for Frame (per LAB-027's argument: pick from the lab plan rather than re-type the goal). But it depends on a populated, well-maintained lab whose items are concrete enough to pick from. In current conditions the lab is being authored in parallel with the framework — items churn, titles drift, priorities reshuffle. Picking from a moving lab adds cognitive load instead of removing it. The per-card Approach unfold was treated as ceremony rather than a thinking prompt; empty unfolds were the dominant pattern. The fix isn't "make the picker better" — it's "earn the picker back when daily Frame is running reliably without it." Pairing "Done means" with "What ruins this" in the same batch surfaces the both/and trap structurally, which the spread-across-batches layout obscured.

**Status.** Active. Shipped on branch `danvers/frame-rollback-outcome-ruin`. Restoration trigger captured in LAB-058: (1) daily Frame runs steadily for ≥ 2 weeks on the textarea form, and (2) the rogaine loop (off-board picks → Debrief pre-fill) is identifiable as the actual constraint on weekly planning quality. Until both are true, the picker stays out.

**References.** Branch `danvers/frame-rollback-outcome-ruin`. `cognitive-lab/cognitive-lab-v0.1.html` (form markup ~5249–5301, FF_FIELDS / FF_LABELS ~7574–7579, form helpers ~7587–7625, viewing-mode renderer ~8323–8348, rollback comment block where renderFramePicker + handlers used to live ~8724–8732). Backlog: LAB-058 (this rollback's archeology + restoration trigger). Related items: LAB-027 (Frame v0.2 — plan-pointing + per-card Approach, *queued for status revisit by Larry*), LAB-036 (Frame Approach iconic skin, *queued for status revisit*), LAB-042 (Off-board picks → Debrief pre-fill, *queued for status revisit*).

---

## 2026-05-04 (later) · Move 2 (Comprehension Station arc) — orientation workshop, Walk Studio, C-before-F, iframe pattern, LAB-009 status

**Decision.** Five sub-phases shipped in the Move 2 arc (branch `danversfleury/lab-course-tier`, 11 commits since the v0.4 session-close):

1. **Comprehend Station ships as a workshop (Move 2a–2e).** Comprehend Station promoted to `workshop: true`. "Where you are" orientation snapshot at top of the drawer: active leg + Course, last 3 comprehend acts, time since last touch, last debrief if present. Collapsible via sessionStorage; click a recent entry to expand inline. Walk Studio sidebar + main split: sidebar lists available walks; main pane renders a presentation deck or a product walk (step renderer + iframe of the live lab). Walk start and completion log to `leg.comprehend[]` as `kind:'walk'`. cc-kind-walk chip color (reddish-purple). Leg view zone subtitle counts walks alongside notes/synthesis/decks.

2. **Walk Studio meta-loop: the lab teaches itself.** The realization driving Move 2: when Claude ships a feature and asks for a test, instructions live in chat. That's friction. The fix: instructions live inside the lab as structured product walks. The full loop — Claude ships a feature, authors a walk, author opens Comprehend Station, walks through the live lab in an iframe, completion logs to the leg — is now real. First authored walk: 'Walk: Build canvas v0.1' (8 steps), replacing the chat-instructed test of the v0.4 build canvas.

3. **C-before-F floor reorder.** Band 2 reorders to Comprehend → Frame. The principle: orientation precedes scoping. You can't pick what to do this turn until you've loaded what just happened. The C-before-F principle stands in layout; the boot-strip gate (hard Comprehend checkpoint before Frame) is explicitly deferred to LAB-048 (P2).

4. **Walk-mode iframe pattern + localStorage isolation.** Walk Studio loads the lab inside an iframe with `?walk=1`. Lab init applies `body.walk-mode`, hides Comprehend Station from the floor (opacity 0.3 + pointer-events none + aria-hidden — recursion defense), and suppresses localStorage writes for view+lens so iframe navigation doesn't bleed to the parent lab's own state. This is now a documented convention for any future feature that embeds the lab in an iframe.

5. **LAB-009 (Comprehend form) — call: drafted.** Comprehend Station now ships as an orientation workshop with Walk Studio. The structured re-immersion form (agent-context picker, 'context loaded' gate before Produce) isn't yet built — that's the chapter material. Status is drafted: the workshop form is live; the chapter material isn't.

**Reasoning.** The test-in-chat loop was friction that compounded with each shipped feature. Authoring the test as a walk inside the lab transforms every feature shipping into a self-documenting artifact. The Walk Studio embeds the lab's own surfaces inside the lab — the metaphor holds: Comprehend Station orients you to the lab, and the lab teaches you how to use it. The C-before-F reorder makes the principle structural rather than incidental. The iframe + localStorage isolation pattern resolves a real engineering risk (iframe navigation bleeding to parent state) in a reusable, named way.

**Status.** Active. All five sub-phases shipped on branch `danversfleury/lab-course-tier`. New deferred items: LAB-052 (interactive walks), LAB-053 (persistent walk progress), LAB-054 (JSON-loaded WALKS), LAB-055 (in-lab authoring UI), LAB-056 (sandbox-Course mode), LAB-057 (multi-walk sequences).

**References.** Branch `danversfleury/lab-course-tier` (11 commits since `fbcd25e`). `cognitive-lab/cognitive-lab-v0.1.html` (chunks: chunk-comprehend-station-v0.1, chunk-walk-studio-meta-loop, chunk-c-before-f-floor-reorder, chunk-walk-mode-iframe-recursion-defense; items LAB-009 [drafted], LAB-052–LAB-057).

---

## 2026-05-04 (late) · Build canvas v0.1 — snap-circuit grid, lens architecture, HTML tooltip; LAB-043/044/046 reclassified

**Decision.** Four framework-level calls shipped in the v0.4 arc (branch `danversfleury/lab-course-tier`, 14 commits since `7437bc4`):

1. **Build canvas v0.1 ships (click-to-place; not drag-and-drop).** The Course view gains a user-authored snap-circuit grid (7×10 cells, ARIA grid). The author places items from the tool drawer onto the grid; positions persist in `course.build_positions`. Template apply and Clear board are first-class actions. Drag-and-drop was explicitly deferred per Quenton's design call — ship click-to-place first, then let dogfood surface whether DnD is worth the cost (LAB-049).

2. **Lens architecture (one canvas, three lenses).** The Course view now has three tabs: Build (default, author-owned canvas) / By function (v0.2 biome Hex Map, restored as a reference lens) / By priority (v0.3 concentric-rings Hex Map). The active lens persists in localStorage. The two Hex Map lenses are read-only re-projections of the underlying lab data; the Build lens is the only authoring surface. `wireHexSVGListeners` was consolidated to fix double-registration on lens switch.

3. **Snap-circuits-with-build-book reframe.** The architectural pivot driving v0.4: snap circuits ship with a build book — a catalog of circuits you can build. The lab should give the user a board, a parts bin, and a builds book (templates = release plans in planning status) rather than generating maps for them. Kay's principle redirected at the user: *"It's easier to build a diagram than read a diagram."* The user building their own placement learns the structure; reading an auto-generated map consumes it.

4. **HTML tooltip pattern (instant hex hover).** SVG `<title>` has a 1-second browser delay. Replaced with an HTML tooltip layer (z-index 450, above toolbar), driven by `mousemove`. `aria-label` replaces `<title>` on each polygon to suppress the duplicate native browser tooltip while preserving accessibility. Pattern is reusable for any future SVG with polygons needing instant hover identity.

**Data hygiene.** LAB-043, LAB-044, and LAB-046 carried invalid `"P3"` priority values in their `priority` fields (the schema enum is P0/P1/P2). All three were promoted to `"P2 (later)"` to match the v0.2 priority spec enum. This was caught during the cumulative sweep and fixed before the session-close commit.

**Reasoning.** The build-canvas pivot resolves the passive/active tension in the prior Hex Map: the map was *generated* from lab data, positioning the author as a reader of a system-produced artifact. The snap-circuit analogy (from Bruner/WS004, already embedded in the Leg view's circuit board) applied at the Course/week scale: give the author components and let them compose. The three-lens architecture preserves the Hex Map's value (it's a good reference view) without making it the default. Build is the primary surface because it's the one the author authors.

Click-to-place over drag-and-drop is a deliberate scope constraint, not a compromise. Quenton's call: dogfood the simpler interaction first. DnD tracked as LAB-049.

**Status.** Active. All four shipped on branch `danversfleury/lab-course-tier`. New deferred items: LAB-047 (Release as 4th tier), LAB-048 (Comprehend boot gate), LAB-049 (DnD v0.5+), LAB-050 (chain edges on Build canvas), LAB-051 (map world long-vision).

**References.** Commits `a5de21f` (HTML tooltip), `d0171b9` (lens dispatcher, Move 3a), `43b1add` (empty snap-circuit grid, Move 3b), plus Move 3c–3e + cumulative sweep commits on branch `danversfleury/lab-course-tier`. `cognitive-lab/cognitive-lab-v0.1.html` (chunks: chunk-build-canvas-v0.1, chunk-snap-circuit-builds-book, chunk-lens-architecture, chunk-instant-hex-tooltip; items LAB-047–LAB-051).

---

## 2026-05-04 (evening) · Hex Map v0.3 — concentric rings + map-legend palette

**Decision.** Hex Map v0.3 drops the red P0 stroke and replaces stroke-as-priority with spatial position: concentric rings carry priority (P0 center → P1 → P2). The palette moves to Okabe-Ito (color-blind safe). An explicit map legend names each area → color, the way a geographic map names blue = water. Hover reveals genus:species identity (area name + item name); per-hex LAB-### labels are dropped.

**Reasoning.** The author dogfooded v0.2 and found the red borders distracting — the stroke was competing with biome color in the same visual layer, creating the same channel-collision problem v0.2 was designed to fix. Concentric rings resolve this by encoding priority through position (a distinct channel from color and stroke). The Okabe-Ito palette with an explicit legend makes the map readable as a map — the reader doesn't infer color meaning from context; the legend states it. Genus:species hover frees the hex face to carry only its color signal; identity is revealed on demand rather than baked into the face as text clutter.

**Status.** Active. Shipped on branch `danversfleury/lab-course-tier` (commits `6c40ddb` and `664e479`).

**References.** Commits `6c40ddb` (concentric rings + palette + legend + hover) and `664e479` (fixes: drop dead .pulse-once.p0 rule, escape priority/status, document palette collision), `cognitive-lab/cognitive-lab-v0.1.html` (chunk-hex-map-v03).

---

## 2026-05-04 (evening) · Frontier-first Frame picker with expand

**Decision.** The per-leg Frame picker defaults to the active Course's frontier. Expand to Full lab is the deliberate emergence valve. Off-frontier picks are tagged with `ref.off_frontier=true` and shown with a chip badge. The strict-only and glow-only alternatives were rejected.

**Reasoning.** Morning dogfood surfaced the seam bug: the picker was showing the entire lab instead of the Course frontier, defeating the rogaine metaphor at the per-leg level. The expand toggle was chosen over a strict frontier-only picker because emergence is a legitimate reason to go off-frontier — something surfaces mid-leg that wasn't visible at Course-planning time. Strict-only would suppress that. Glow-only (highlight off-frontier picks without tagging) would surface the data visually but lose it for Debrief writeback. The tag + chip badge preserves both: visible to the author in the Frame, queryable by the Debrief save handler (LAB-042, deferred).

**Status.** Active. Tag in place; Debrief pre-fill queued as LAB-042 (P2).

**References.** Commits on branch `danversfleury/lab-course-tier` (v0.2 arc), `cognitive-lab/cognitive-lab-v0.1.html` (chunk-frontier-first-picker, LAB-042).

---

## 2026-05-04 (evening) · Comprehend Signals: deck-open + status-cycle auto-log; conservative surveillance line

**Decision.** Comprehend auto-logs three kinds of intentional acts: `note` (manual), `synthesis` (status cycle to live/archived), `deck` (deck-open matched by DECK_FILE_RE). Frame card field activity is explicitly excluded for now.

**Reasoning.** The seam bug the author caught in morning dogfood: the Comprehend zone was showing "idle" while real comprehension activity was happening elsewhere (deck walks, status cycles). The fix required a surveillance line — a principle for which acts merit a log entry. The line drawn: only acts the user *intentionally took* and *would expect to leave a record*. Status cycles and deck-opens clear this bar. Field edits in Frame (Doing / Not Doing / Approach) do not — they're exploratory; the user may type and delete without committing. Logging them would capture intent-noise. One Course of dogfood will reveal whether the signal is sparse enough to warrant expansion (LAB-044, P2).

**Status.** Active. Surveillance line is a first-class constraint, not a footnote. Expansion criteria deferred to LAB-044.

**References.** Branch `danversfleury/lab-course-tier` (v0.2 arc), `cognitive-lab/cognitive-lab-v0.1.html` (chunk-comprehend-signals, LAB-044, LAB-046).

---

## 2026-05-04 (evening) · Four-channel Hex Map encoding (hue / luminosity / stroke / motion)

**Decision.** Hex Map v0.2 encodes four cognitive jobs across four independent visual channels: hue=biome (stable identity), luminosity=relevance (4-state ramp), stroke=priority (P0 → 2px ring), motion=attention (pulse on select + breath on active-leg working set). Replaces the v0.1 fill-vs-outline approach and the purple "both" override ring.

**Reasoning.** Morning dogfood surfaced the misread: P0 red was winning the visual fight against biome hue, making it impossible to read frontier state independently of priority state. The v0.1 fill-vs-outline encoding was trying to carry multiple states through a single channel, which collapsed when states co-occurred. Four independent channels solve this: each type of information has its own visual grammar; they compose without ambiguity. The design follows the Bruner/Snap Circuits principle already adopted for the lab: each cognitive job gets its own representation primitive rather than overloading a single channel.

**Status.** Active. All four channels shipped in the v0.2 arc.

**References.** Branch `danversfleury/lab-course-tier` (v0.2 arc), `cognitive-lab/cognitive-lab-v0.1.html` (chunk-four-channel-hex-encoding).

---

## 2026-05-04 (evening) · Luminosity ramp (4-state: archived / available / in-frontier / active)

**Decision.** The luminosity channel uses four states: 18% (archived — terrain), 50% (available — items exist but not on frontier), 100% (in-frontier — reachable this week), 100% + saturation boost (active — in current leg's working set). Steps are logarithmic-ish for perceptual evenness.

**Reasoning.** Linear steps (0-25-50-100) would make the archived→available step perceptually large and the available→frontier step small — the wrong distribution for the cognitive jobs each state does. Logarithmic-ish distribution (18-50-100) makes archived recede into background (terrain), available readable but muted, frontier fully lit. The 18% floor keeps archived hexes visible as terrain context rather than invisible — the map is a map, not a spotlight. The saturation boost for active-leg distinguishes "on course frontier" from "actually in this leg's working set" without adding a fifth luminosity state.

**Status.** Active.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-luminosity-ramp).

---

## 2026-05-04 (evening) · Motion budget: pulse + breath only; prefers-reduced-motion honored

**Decision.** The Hex Map uses exactly two motion behaviors: a single 600ms pulse on select, and a slow 6s ±5% ambient breath on the active-leg working set. No additional motion states. Both suppressed when prefers-reduced-motion is set.

**Reasoning.** Motion is a preattentive feature — it pulls attention before the user consciously decides to look. Uncontrolled motion would pull attention out of the author's current task continuously. The cap is cognitive-load-driven: the same principle (extraneous load reduction is the highest-ROI cognitive intervention) that drives the P0 hard cap at 3 applies to motion in the UI. The pulse confirms selection without persisting; the breath signals "live right now" from the periphery without demanding focus. prefers-reduced-motion compliance is a hard constraint, not optional.

**Status.** Active.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-motion-budget).

---

## 2026-05-04 (evening) · Biome regions replace the random Hex Map grid

**Decision.** Hex Map v0.2 clusters hexes into labeled, biome-tinted regions rather than a flat grid. Regions are the legend; the separate swatch row is dropped. Regions sort biggest-first. Semantic adjacency within biomes is deferred (LAB-043, P2).

**Reasoning.** Morning dogfood surfaced the misread: the v0.1 grid layout looked random — spatial proximity implied relationship, but the grid had no relationship logic. This imposed extraneous load (inferring meaning from position that had none). Biome regions give the map a spatial grammar: you navigate to the turn-phases cluster or the capacity-instruments cluster, not to cell (3,2). Regions-as-legend drops the redundant swatch row — the map tells its own story. Sorting biggest-first makes the dominant cognitive territory (turn phases, 5–6 hexes) visually anchor the layout.

**Status.** Active. Within-biome semantic adjacency deferred per Quenton's call — revisit after one Course of lived use shows whether it matters.

**References.** `cognitive-lab/cognitive-lab-v0.1.html` (chunk-biome-regions, LAB-043).

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
