# Quenton Quince — Plays

Recurring design scenarios with prescribed steps. When you recognize the trigger, run the play. Each play has earned its keep through lived practice — see the **Origin** note for what surfaced it.

These are patterns, not scripts. Adapt the steps when the situation calls for it. Document new plays as they earn the right.

---

## Wildcat-First, Form-Second

**Trigger.** Starting to design a new phase form / instrument / practice. The temptation is to research first and design top-down.

**Play.**

1. Run the practice informally — talk it out, no template, ~5 minutes.
2. Capture what surfaced: what fields naturally emerged, what order they came in, what didn't get said.
3. Pull research grounding *after* the wildcat, to validate (or push back on) the lived shape.
4. Design v0.1 of the form from the wildcat output, not from the research.
5. Run the v0.1 form on a real turn the same day.

**Produces.** A form whose fields are grounded in lived experience and validated by research, in that order.

**Origin.** The wildcat Frame on 2026-04-30 (evening) seeded the v0.1 Frame form better than any research-first design pass would have. Confirmed again on 2026-05-02 with the wildcat Pilot Check (which the author reframed as rule-out, not measurement — exactly the kind of insight you'd miss without lived data).

---

## Drop-the-Acronym

**Trigger.** A clever acronym is shaping the design. Sequence feels unnatural, fields feel forced, naming dominates the conversation.

**Play.**

1. Stop. Name what the acronym is doing to the design.
2. Strip the acronym and look at the underlying structure.
3. Re-order fields by natural cognitive flow, not letter sequence.
4. Re-label in plain English.
5. Note the dropped acronym in the Decisions log.
6. Earn the right to a name later — only after the structure has settled and is being used.

**Produces.** A form whose shape follows function rather than mnemonic.

**Origin.** F.R.A.M.E. (Focus / Range / Approach / Miss / End) was clever but constrained the natural order of Frame's fields. After dropping the acronym, the field order rearranged into four batches (Scope / Outcome / Approach / Safety) following the actual cognitive flow.

---

## Bootstrap-a-Workshop

**Trigger.** A meta or phase area in the lab needs to become a working workshop with a prototype.

**Play.**

1. **Wildcat the practice** (see Wildcat-First Play). Get lived data.
2. **Mark the area** with `workshop: true` in the lab data. Drawer expands when opened.
3. **Build the prototype** as the top half of the workshop drawer. Mode-state machine (resting / editing / viewing) if it makes sense; flat layout (sliders + dispatch) if simpler.
4. **Add a save handler** that writes both to a workshop-specific localStorage key and as a Log entry on the area's experiments array. Each prototype run should auto-Log.
5. **Seed the area's chunks** with research-grounded chapter material (use Chunks-from-Research-Doc Play if a substantive doc exists).
6. **Seed the area's Sources** with the relevant research papers, deck slides, and prior docs.
7. **Update the area's To-Do items** to reflect what's been built and what's queued.
8. **Update the area's description** in the lab data (shows in the (i) tooltip).

**Produces.** A workshop that the author can use immediately, with a prototype, captured runs, and chapter material ready to evolve.

**Origin.** Frame Workshop on 2026-05-01 and Pilot Check Station on 2026-05-02 both followed this arc. The pattern is identical; only the specifics of the prototype change.

---

## Merge-Duplicate-Tools

**Trigger.** Two artifacts in the lab are converging on the same job. Two areas. Two instruments for the same signal. The author notices the duplication.

**Play.**

1. **Confirm the convergence** is real, not just adjacent. Are they doing the same cognitive work? Producing similar outputs?
2. **Identify which absorbs which.** Usually the more general absorbs the specific.
3. **Sketch the merger architecture** — what features carry, what consolidates, what gets dropped.
4. **Don't merge yet.** Capture the insight as a Log entry on the relevant area; queue the merger work as a To-Do.
5. **Wait for the lab merge / dependency** if the merger touches in-flight PR work.
6. **Execute the merger** when the path is clear: move data structures, update references, retire deprecated areas.

**Produces.** A unified instrument with full feature set, plus a clear retirement of the duplicate.

**Origin.** Capacity check-in PoC and Pilot Check Station were diverging into duplicate instruments on 2026-05-02. The author caught the convergence; the merger plan was queued as LAB-025 ("Make the Gauge a workshop") rather than executed mid-flight.

---

## Chunks-from-Research-Doc

**Trigger.** A substantive `.md` doc exists for a phase or topic (e.g., research-and-practice for Frame). Need to surface it as editable Chapter chunks in the lab.

**Play.**

1. **Read the doc** end-to-end.
2. **Identify natural section boundaries** — usually the doc's own sections become chunks (8 chunks for Frame's research doc).
3. **For each section, write three things:**
   - **Title** (4–8 words, distinct, scannable)
   - **Summary** (one line, captures the section's claim)
   - **Body** (concise version of the section, preserves the substance, drops redundancy with other chunks)
4. **Add to the area's `chunks` array** in the lab data. Order matches the doc's logical sequence.
5. **Reference the source doc** in the area's Sources tile.
6. **Update the area's Log** with an entry capturing the seeding.

**Produces.** Editable Chapter chunks in the workshop that the author and Larry can refine, and that ghostwriter can later pull into chapter prose.

**Origin.** `frame-research-and-practice.md` became 8 seed chunks in the Frame Workshop on 2026-05-01.

---

## Research-Grounded Design

**Trigger.** About to commit to a design choice that will be load-bearing.

**Play.**

1. **Name the cognitive function.** What is this field / phase / instrument doing for the brain?
2. **Cite the specific research.** "Sweller (CLT) says X" — not "the research suggests."
3. **Check metaphor coherence.** If a metaphor is in play, does it map onto the research, or does it diverge? Where they diverge, research wins.
4. **Note any extra creativity.** Anything beyond what research strictly requires — flag it, ask whether it earns its keep.
5. **Commit only after this check.** If the answer to "why is this field here" is just "it's clever," that's not enough.

**Produces.** Designs where each piece can defend its existence with both research and lived practice.

**Origin.** The user's question on 2026-05-01: "are we still following the research that kicked off the FRAME exercise?" Surfaced that "Approach" was loose — research said specifically Mode + Scaffold (Wickens MRT + Risko & Gilbert offloading). The fix: tighten the prompt to walk through both.

---

## Symmetric Pre-mortem

**Trigger.** A pre-mortem field is about to be filled. The temptation is to name a single risk.

**Play.**

1. **Imagine the failure.** What does a bad outcome look like?
2. **Look for both ends of a balance failure.** The strongest pre-mortems name a both/and trap, not a single risk.
3. **Write it as "X — OR — Y."** Both ends of the spectrum are failure; the win condition is the middle.

**Produces.** A pre-mortem that catches in-flight drift in either direction, not just one.

**Origin.** The author's first formal Frame on 2026-05-01 named "lots of research and no tool — OR — just the tool and no notes" as the Miss. The symmetric framing made it a stronger pre-mortem than a single-risk version would have been.

---

## Cleanup-Then-Upfit

**Trigger.** A v0.1 has shipped with rough edges (labels, prompts, structure) and you're tempted to add new features.

**Play.**

1. **Acknowledge the rough edges.** Name what's specifically off — labels, prompts, sequence, sub-features.
2. **Stop the feature work.** Queue any new features as future LAB items. Don't pile them onto the rough v0.1.
3. **Run the cleanup pass.** Labels in plain English. Prompts that read instructionally. Sequence that follows cognitive flow.
4. **Ship the cleanup as v0.2** before adding any new features.
5. **Then upfit.** Plan-pointing, integrations, polish — all on top of the cleaned foundation.

**Produces.** A v0.2 that is structurally sound, with new-feature LAB items clearly queued behind the cleanup.

**Origin.** Frame v0.1 had obscure labels (Must / Stretch / In / Out / Approach / Miss / End) that ran successfully but confused on second read. The author's call: "cleanup first, upfit second." LAB-026 (cleanup) ran; LAB-027 and LAB-028 (upfits) queued behind.

---

## Build-While-Flying

**Trigger.** About to design a phase or practice. The framework's existing tools could be used to design themselves.

**Play.**

1. **Recognize the confluence.** The framework gives you Frame for designing; you're designing Frame. The framework gives you Pilot Check for assessing capacity; you're designing Pilot Check.
2. **Use the practice as you design it.** Run a wildcat Frame on the day you're designing the Frame form. Run a wildcat Pilot Check on the day you're designing the Pilot Check.
3. **Capture lived data as you go.** Each use is an experiment. Each experiment informs the design.
4. **Don't wait for the practice to be perfect.** v0.1 of the form on day one of running it. The practice and the design co-evolve.

**Produces.** Designs that are credible because they were used in the act of being designed.

**Origin.** 2026-04-30 evening: wildcat Frame to design Frame. 2026-05-01: ran v0.1 Frame form on a real turn while still designing it. 2026-05-02: ran wildcat Pilot Check that immediately surfaced the rule-out reframe.

---

## When to *not* run a play

Plays are patterns, not obligations. Skip them when:

- The author is in Push and asking for a small move. Don't bootstrap a workshop when they want a typo fixed.
- The work has a deadline that doesn't accommodate the play's full arc. A wildcat-first approach when there's no time to wildcat is just delay.
- The trigger is partially present but the play would be over-engineering. Trust the read.

When in doubt: the author's energy and goals are the constraint. The plays exist to serve those, not to be completed.
