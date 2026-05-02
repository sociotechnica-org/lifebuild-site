# The Turn · Phases, Research, and Leverage (v0.1)

Companion to `turn-v0.1-map.md`. Where the map shows the structure, this document explains
what each phase is doing, what the cognitive science says about it, what edges we have so
far, where else to look, and — at the end — which phase deserves the most love first.

The phase labels are stable enough to work with. The edge labels are provisional — what
matters is the function each one serves, not the name. If a label isn't earning its keep,
swap it.

---

## The regulation loop, across the cycle

The cycle borrows its skeleton from how occupational health psychology talks about effort
and recovery. There are four jobs the cycle has to do, and each phase is one job (or a
share of one):

- **Reduce demand** before the work starts. *Frame* does this.
- **Regulate during** the work. *Comprehend, Sync, Push* share this job.
- **Measure** what happened. *Debrief* does this.
- **Recover after.** *Recover* does this.

Two disciplines run *across* the cycle, not inside any one phase:

- **Transition** — every phase boundary is taxed. The literature on attention residue
  (Leroy, 2009) measures the cost of moving from one task to the next; the cost is real
  and it accumulates across the day. Transition discipline is what makes phase boundaries
  cheap instead of expensive.
- **Trim** — selection discipline. Lives mostly inside Frame, but applies inside every
  other phase too: don't comprehend everything, don't sync on everything, don't decide
  everything, don't capture everything.

Underneath all of this sits the **Ledger** — telemetry that tells you whether the cycle is
actually working. The cycle is the engine; the Ledger is the gauge.

---

## Phase by phase

### 1. Frame  (5–15 min) · Reduce demand

**Function.** Decide what is *not* in this turn before deciding what is. Set scope. Trim
inputs before they enter the funnel. Lean on durable knowledge sources (Library, Ledger,
Playbook) so you don't have to re-derive what's already known.

**Research base.**
- *Cognitive Load Theory* (Sweller). Reducing extraneous load is the highest-ROI
  intervention; cheaper to prevent load than manage it.
- *Conservation of Resources* (Hobfoll). Resource investment decisions matter most before
  you commit, because loss spirals start small and compound.
- *Goal shielding* (Shah, Friedman, Kruglanski). An explicitly chosen goal inhibits
  competing goals downstream. Without explicit selection, every input competes for
  attention.
- *Cognitive offloading* (Risko & Gilbert). Knowing *when* to externalize cognition into a
  durable system reduces load; knowing when not to prevents monitoring tax.

**Edge ideas so far.**
- Lean on durable knowledge already captured by the company (provisionally labelled "the
  Substrate").
- Decide the single most important outcome of this turn.
- Set explicit non-goals — what's deferred, by name.

**Additional areas to explore.**
- A reusable Frame template — five questions, five minutes, forces scope clarity.
- Pre-mortem: what would make this turn a waste of capacity? Avoid that specifically.
- Inbound inventory: messages, alerts, asks — which get acknowledged this turn, which get
  parked.
- The "single decision rule": what is the one decision this turn must produce? Everything
  else is supporting cast.
- Frame paired with the agent-status view: what state am I walking into? Which agents
  need a human, which don't?

---

### 2. Comprehend  (30–60 min) · Regulate during

**Function.** Load remaining state — agent output, decisions made overnight, open
questions. Rebuild situation awareness before deciding anything.

**Research base.**
- *Endsley's Situation Awareness model.* Three levels: perception (what is the data),
  comprehension (what does it mean), projection (what's coming next). All three need to
  rebuild from cold start.
- *Bainbridge's Ironies of Automation.* The human supervising automation needs *more*
  context, not less, because the system is doing things while the human is away.
- *Wickens' Multiple Resource Theory.* Verbal/symbolic channels (reading agent text) and
  spatial/visual channels (scanning a dashboard) can run in parallel without interference.
- *Naval watch handoff protocols.* Empirically refined for fast context rebuild.

**Edge ideas so far.**
- A single view of what every agent has been doing and what each needs from a human
  (provisionally "the Cockpit").
- Protected attention during agent latency — the >30s tab-switch trap (provisionally "the
  Wait").

**Additional areas to explore.**
- Comprehension index: a structured digest the agents produce for the human at the start
  of each turn (decisions made, open questions, disagreements between agents).
- Reading order discipline: latest decisions first? Open questions? Agent disagreements?
- "Comprehended enough" criteria — how do you know you can stop reading?
- Visual rebuild vs textual rebuild — SnapTool/dashboard vs scrolling threads.
- Have agents summarize *themselves* in a comprehension-ready format.

---

### 3. Sync  (30–60 min) · Regulate during

**Function.** Align humans and agents. Confirm zones of authority. Surface blockers. Set
priorities for the push that follows.

**Research base.**
- *Naval watch protocols* — "taking the conn," structured authority transfer.
- *SBAR* (Situation, Background, Assessment, Recommendation) — hospital handoffs reduced
  adverse events by 65% with structured communication.
- *Mission command / Auftragstaktik.* Authority pushed to the edge with explicit intent.
- *Endsley's team situation awareness.* Shared SA is what coordination quality depends on.
- *Toyota andon* — surface blockers fast, designed escalation.

**Edge ideas so far.**
- Zone-based ownership at handoffs (whose decisions belong where).
- Standup as a sync barrier with structured artifacts in and out.

**Additional areas to explore.**
- Async vs sync sync — can the alignment happen by written artifact rather than meeting?
- Agent participation in sync — what does it mean for agents to be "at" the sync?
- Decision-making boundary: what is *not* decided in sync (push-phase work) vs what is.
- Solo case: when working alone, what are you syncing with? (Probably yesterday's self,
  via the Ledger and durable knowledge.)

---

### 4. Push  (2–3 hr) · Regulate during

**Function.** Intense decision work. Where human judgment actually happens, where agents
get unblocked, where the highest-value moves of the turn occur.

**Research base.**
- *Decision fatigue* (Vohs, Baumeister, Schmeichel). Sequential decisions degrade in
  quality — the famous parole-judge studies.
- *Hockey's Compensatory Control Model.* Under high demand, you compensate with effort
  (costly), reduce performance, or change strategy. The cost is often invisible until
  later.
- *Goldratt's Theory of Constraints.* The bottleneck deserves the focus.
- *Csikszentmihalyi's flow.* Useful but masks cost — flow can be bright red.
- *Boyd's OODA.* The micro-cycle inside the push.

**Edge ideas so far.**
- Hardest decisions first while reserves are highest (provisionally "Decision Order").
- Stop at *can-go-home-whole*, not at *shipped* (provisionally "the Whole-Man Rule").
- Protected attention during agent latency.

**Additional areas to explore.**
- Push composition: what's the right *mix* of decision types within one push?
- Single-thread vs multi-thread push: keep one decision live, or batch?
- Mid-push checkpoint — a 30-second self-check at the midpoint, "still sharp?"
- Brief flow window inside push: 25–50 minutes of intense focus, then change.
- Calling the push early — what are the signals? Reserves dropping, decisions getting
  sloppier, irritation rising.
- Capacity budget: starting reserves × push duration ≈ decision capacity available.

---

### 5. Debrief  (10–20 min) · Measure

**Function.** Capture what happened. Close the turn. Set up the next one. Make the cycle
a learning loop instead of just a doing loop.

**Research base.**
- *Effort-Recovery Model* (Meijman & Mulder). Measurement of demand drives the recovery
  requirement.
- *After Action Review* (US Army). What was supposed to happen, what happened, why, what
  to sustain or improve. Four questions, high yield.
- *Reflection theory* (Kolb, Schön). Structured reflection is what produces learning;
  experience alone doesn't.
- *Recovery Experience Questionnaire* (Sonnentag & Fritz). Validated instruments exist
  for measuring recovery quality.

**Edge ideas so far.**
- The cognitive bank — withdrawal, replenishment, day verdict.
- Lab note as the daily-shareable artifact (this is what the book's journal cadence
  rests on).

**Additional areas to explore.**
- A five-question debrief template that fits in a ten-minute window.
- Metrics: phase durations actual vs planned, phase violations, decision quality
  (subjective 1–5), reserves at end (1–5).
- Decision log: what was decided, why, what was deferred — feeds tomorrow's Frame.
- Open-question parking lot — the questions you don't have time to answer this turn.
- What the next turn's Frame should know — Debrief is partly written *for* tomorrow.

---

### 6. Recover  (until next turn) · Recover after

**Function.** Restore capacity for the next turn. Mode-specific, not generic. The
literature is unambiguous: "rest" is too coarse to predict next-day capacity.

**Research base.**
- *Recovery Experiences* (Sonnentag & Fritz). Four mechanisms: **detachment** (mental
  off-time, the strongest predictor of next-day capacity), **relaxation** (low-arousal,
  parasympathetic), **mastery** (engaging different abilities — counterintuitively
  restorative), **control** (autonomy over what you do).
- *Effort-Recovery Model.* Insufficient recovery accumulates as strain.
- *Conservation of Resources.* Recovery is resource investment; depletion compounds.
- *Allostatic Load* (McEwen). Chronic insufficient recovery has measurable physiological
  cost.
- *Attention Restoration Theory* (Kaplan). Soft fascination — nature, art — restores
  directed-attention capacity.
- *Default mode network research.* Mind-wandering during rest is generative; incubation
  effects on creative problems happen here.

**Edge ideas so far.**
- Recovery decomposes — pick a mode, don't default to whatever's nearest.
- Detach is the heaviest hitter for next-day capacity.
- Mastery (a hard new thing during off-time) recovers *differently* from relaxation.

**Additional areas to explore.**
- Recovery prescription: which mode for which day? Should be informed by what the day
  spent.
- The "blue but actually gray" trap — passive scrolling looks like rest, doesn't restore.
  Detection heuristic needed.
- Sleep as its own sub-phase (involuntary recovery, separate budget).
- Mode-mixing: one detach activity plus one mastery activity in the same off-period.
- Recovery debt vs recovery surplus — is there a running balance the user can intuit?
- Boundary protocols: what makes Recovery *start*? What makes it *end*?

---

## Meta-disciplines

### Transition (own chapter, own experimentation area)

**Function.** Make every phase boundary cheap. Close one phase cleanly, reset, open the
next with intent. Plus the bigger boundary: turn-to-turn handoff.

**Research base.**
- *Attention residue* (Leroy 2009) — the canonical mechanism, well-measured.
- *Goal shielding loss after interruption.*
- *Transition rituals* (organizational behavior literature).
- *Sleep onset / offset* — the body's own transition templates.

**Where to explore.**
- The 60-second transition protocol — what's the actual move?
- Scaling: micro (between phases), meso (between turns), macro (start/end of week).
- Physical anchors: water, walk, posture change.
- Cognitive anchors: explicit "closed" and "opened" statements.
- Boundary risk by transition type: which boundary leaks the most? (Probably Push →
  anything, because Push has the most momentum to bleed.)

### Trim (ambient)

**Function.** Selection discipline inside every phase.

**Research base.** *Cognitive Load Theory* (extraneous load reduction), information
overload research, executive-function inhibition (Miyake et al).

**Where to explore.** Fast-no protocols. The 80/20 cut. The "trim audit" at debrief —
what shouldn't have made it past Frame? If Frame works well, this audit gets shorter
over time.

---

## Telemetry: the Ledger

Daily withdrawal, replenishment graded the next morning, color verdict, free-text on what
was actually restorative. The PoC works. Open question: does it stay daily, or shift to
per-turn capture via the Debrief phase?

The literature would suggest both — per-turn for granularity, per-day for the
morning-after honest signal. They measure different things. Daily is the sanity check;
per-turn is the operating data.

---

## Leverage: where to invest first

**Frame is the highest-leverage phase. Invest there first.**

The argument:

1. **Multiplicative downstream effect.** Everything that happens in Comprehend, Sync,
   Push, Debrief, and Recover is *downstream of what Frame let through*. Better Frame
   means less to comprehend, less to sync on, less to decide, less to capture, less to
   recover from. No other phase has multiplicative reach into all five others.

2. **Cheapest to design.** Frame is a 5–15 minute phase. A reusable template, a checklist,
   a prompt — small artifacts produce large effects. Compare to Push, which is 2–3 hours
   of variable-shape decision work that's much harder to template.

3. **The cognitive load literature already says this.** Across CLT, COR, and the
   occupational-health literature, *demand reduction before commitment* is consistently
   the highest-ROI intervention. You're cutting load before it's incurred. Every other
   phase is managing load that already exists.

4. **Measure twice, cut once.** Your axiom. Frame is the measure-twice phase.

5. **Hardest to recover from if missed.** A bad Frame can't really be fixed mid-turn. It
   corrupts everything downstream. Compare to a bad Debrief (you can re-run it) or a
   bad Recover (next turn's Frame can compensate).

6. **Where AI-native gets unique.** The leverage of leaning on durable knowledge
   substrates (Alexandria-shaped) is greatest at Frame. Traditional work design has no
   real analogue for this — every other phase has a pre-AI analogue. Frame in an
   AI-native world is a genuinely new design problem, which means the most learning is
   here.

**Runner-ups, in order:**

- **Recover** is the second-highest leverage *over time*, because it determines what
  capacity you start the next turn with. The Ledger PoC already gives partial
  instrumentation. Practice — picking a Recovery mode deliberately, detecting "blue but
  actually gray" — is the next investment.
- **Transition (meta)** is the highest *blast radius* but lower leverage per unit
  investment, because it's a discipline rather than a designed phase. Worth its own
  experimentation track in parallel with Frame work, not instead of.
- **Debrief** is small, easy to template, high yield for compounding learning. A quick
  win.
- **Push** feels like it should be highest because the work happens there, but Push
  quality is mostly downstream of Frame and Comprehend. Optimizing Push without
  optimizing Frame is a local maximum.
- **Comprehend** is partly determined by Frame (less to comprehend if Frame trimmed
  well) and the Cockpit (whether agent state is legible). Mature this *as* Frame and
  Cockpit improve.
- **Sync** matters most at team scale. For solo guinea-pig work right now, Sync is
  thinner — it's mostly alignment with yesterday's self via the Ledger and durable
  knowledge.

---

## Sequencing implication

If the leverage analysis is right, the experimentation sequence is:

1. **Frame** — design a template, run it for a week, iterate. Likely the single biggest
   capacity unlock available.
2. **Recover** — start picking a mode deliberately, log it, watch the Ledger respond.
3. **Transition (meta)** — in parallel, practice the boundary move at every phase change.
4. **Debrief** — codify the ten-minute template; it makes everything else compound.
5. **Push** — refine after the upstream phases are stable.
6. **Comprehend & Sync** — these get easier as Frame and Cockpit improve; address last.

That's the *what to love first* answer.
