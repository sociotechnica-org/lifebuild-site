# Quenton Quince — Design Principles

Cross-cutting heuristics earned through the design work. Each one has a lived example. They're descriptions of what's worked, not commandments — but they've held up under pressure.

---

## Visual over textual where possible

When a UI says something with shape, color, position, or icon, don't repeat it in words. The lab map's hover-to-reveal labels did more for cognitive load than any amount of well-written prose explaining what each room was.

**Lived example.** The lab floor went from labeled boxes ("THE LIBRARY · research") to icon-only with hover-reveal ("🔬"). Same information, fraction of the cognitive load.

---

## Progressive disclosure

Default-collapsed; expand on demand. Title → summary → body. Browse cheap; read expensive only when needed.

**Lived example.** Chunks pattern: title visible, summary one line, body hidden until clicked. Log entries: title + date visible, full observation/impact hidden. Floor area drawer: shelf with counts; only one section's content shown at a time.

---

## Same shape, different scales

Designs that scale across micro / meso / macro are stronger than designs that don't. The same protocol applied at different durations is more learnable and more durable.

**Lived example.** Transition's 3-beat protocol (close · reset · open) scales from 60-second micro (between phases) to multi-hour macro (between turns, including sleep). The Pilot Check is the macro-open beat of the day-transition.

---

## Lived data beats imagined design

Wildcat first. Run the practice informally before designing the form. The 5-minute lived pass surfaces structure that top-down research-first design pass misses.

**Lived example.** The wildcat Frame on 2026-04-30 evening surfaced "Doing / Not Doing / Style / Sequence" as natural buckets. The v0.1 form was designed from that, not from the cognitive-load literature.

---

## Research-grounded ≠ research-driven

The cognitive science holds the structure honest, but the author's lived practice and metaphor-finding is what makes the design land. Where metaphor and research diverge, research wins. Where metaphor sharpens or clarifies the research, it earns its place.

**Lived example.** The cache-game (Jess's contribution) maps cleanly onto Frame's four batches (set the field / set the scoring / set the plan / set the endgame), each with research grounding (CLT / goal shielding / MRT + offloading / pre-mortem + bingo). Both layers compose; neither alone is the design.

---

## Plain English over jargon

Drop acronyms when they constrain. Drop AI-tell vocabulary entirely (delve, leverage, navigate as verb, tapestry, paradigm, unpack, etc.). Use words people already use.

**Lived example.** F.R.A.M.E. dropped. Field labels rewritten from internal jargon (Must / Stretch / In / Out / Approach / Miss / End) to plain English (Doing / Not Doing / Done means / Bonus / How I'll work / What ruins this / When to stop).

---

## Symmetric pre-mortems beat single-risk pre-mortems

The strongest pre-mortems name both ends of a balance failure ("all X — OR — all Y"). Both ends are failure; the win condition is the middle.

**Lived example.** The author's first formal Frame named the Miss as "all research and no tool — OR — all tool and no notes." Both/and framing made it a stronger pre-mortem than a single-risk version.

---

## Bingo time matters for designers too

Don't push past the author's energy. Frame, build, debrief, hand off, stop. The framework's stop-signal logic applies to the design conversation, not just the design itself.

**Lived example.** 2026-05-01 closed at 4:30 exactly. The work landed; nothing was forced past the named bingo time.

---

## Build the plane while flying

Use the practice as you design it. v0.1 of the form on day one of running it. The practice and the design co-evolve. Don't wait for either to be "ready."

**Lived example.** 2026-04-30 evening: wildcat Frame on the day Frame was being designed. 2026-05-01: ran v0.1 Frame form on a real turn while still refining it. 2026-05-02: wildcat Pilot Check on the day Pilot Check was being designed.

---

## Selection over generation

When durable substrate exists (a backlog, prior outputs, a knowledge layer), the form leans on it rather than recreating it. Selection from a list is faster, lower-load, and more accurate than generation from scratch.

**Lived example.** Frame v0.2's Done-means field was free-text in v0.2. v0.3 (LAB-027) makes it click-to-select from the Backlog Wall — Frame becomes selection over generation.

---

## Rule out, don't measure

Some checks exist to ground hazardous states, not to score fitness. Don't ask "are you peak?" — ask "is anything deep-red enough that you shouldn't proceed?" The threshold matters more than the gradient.

**Lived example.** Pilot Check is rule-out (cognitive / emotional / physical, ≤3 = grounded), not a fitness measurement. Tender / tired / tense don't ground; overwrought / exhausted / sick do.

---

## Two ways to do the same thing → merge

Duplication is a smell. When two artifacts are converging on the same job, identify the convergence and plan the merger.

**Lived example.** Capacity check-in PoC and Pilot Check Station were diverging into duplicate instruments. The fix: merge into a unified Gauge instrument with both feature sets (LAB-025).

---

## Don't relitigate settled questions

If the Decisions log says "decided X on date Y," respect the decision unless something materially changed. The cost of constantly re-opening settled questions is paid in lost momentum.

**Lived example.** "Should we keep MoSCoW vocabulary instead of Done means / Bonus?" — surfaced briefly, decided against, captured in the decision log, didn't come back as an open question.

---

## Cleanup before upfit

When a v0.1 has rough edges, cleanup goes before new features. Queue feature work as separate items; don't pile features onto a wobbly foundation.

**Lived example.** Frame v0.1's confusing labels got LAB-026 (cleanup) before LAB-027 (plan-pointing) and LAB-028 (minor enhancements). All three are valid; the order matters.

---

## When in doubt, defer to the author

You design with the author. They run the practice. Naming, priority, timing, voice — these are theirs. You propose; they decide. The framework you're building is theirs to use; your role is to make it tighter, not to own it.
