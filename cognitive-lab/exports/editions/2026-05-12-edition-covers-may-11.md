# The Cognitive Lab Daily

**Tuesday, May 12, 2026 · Issue 1 · Covering May 11 activity**

---

## THE HEARTBEAT IS DEAD. LONG LIVE THE BOOKENDED DAY.

### And: Frame form reverts to textareas — pickers out, "What ruins this" up

---

Two independent threads ran in parallel yesterday and both landed on main before close. Thread one was a planned lab restructure, months in the making, that retired the framework's second central image and rebuilt the day's architecture around two bookending rituals. Thread two was a separate rollback of Frame's Outcome picker — simpler, faster, and a genuine improvement. Neither waited for the other. Six PRs merged.

---

**BELOW THE FOLD**

- Recovery Room workshop ships with three screens and a Drive mirror
- Four-band floor replaces the flat layout; Pilot Check and Recovery get their own band
- Open turns at lock: carry, drop, defer
- The stacked-base merge problem explained

---

## THE RESTRUCTURE

**Heartbeat retired.** The heartbeat was the framework's second central image since May 2. It described a continuous read-and-dispatch cycle: the Gauge reads capacity at every phase boundary; the result routes you to recovery or forward. The cycle was called the framework's heartbeat — capacity ↔ restoration, running everywhere, always.

The problem: the Gauge was a theoretical instrument. The practice that actually ran was two discrete rituals. Pilot Check in the morning. Recovery Room at close. The heartbeat described a product that didn't exist; the bookended day describes what does.

**The bookended day.** Pilot Check opens. Recovery Room closes. The two share one reference point: this morning's three-dimension reading becomes tonight's anchor. Withdrawal = anchor − current. The day is bounded by a measurement pair, not a continuous loop. The cache-game (Frame's metaphor) asks how you design a day worth playing. The bookended day asks how you open and close it reliably. Both together describe a day with a shape.

*From the DECISIONS log, 2026-05-11:* "The heartbeat described a continuous telemetry instrument that doesn't exist in practice and may not need to be. The bookended-day framing describes what actually happens."

**Gauge area retired.** LAB-020, LAB-021, LAB-025, LAB-030 archived to `cognitive-lab/archive/heartbeat-retirement-2026-05-11.md`. The chunk-hash-house-pilot-check was salvaged and relocated to Pilot Check Station. Two 2026-05-02 DECISIONS entries marked Superseded.

---

## FRAME ROLLBACK

**Pickers out.** The Done means picker (typed-ref multi-select scoped to the Course frontier), the Bonus picker, the per-card Approach unfold, the Course/Full-lab scope toggle, and the day-level "How I'll work — overall" scaffold are all gone from the rendered form. The form returns to four plain textareas.

**What improved.** The Outcome batch now pairs Done means with What ruins this — the both/and twin. These two fields were previously split across the Outcome and Safety batches. Putting them side-by-side in the same batch makes the tension visible: what success looks like and what would ruin it belong in the same moment of thinking.

*From the DECISIONS log, 2026-05-11:* "The fix isn't 'make the picker better' — it's 'earn the picker back when daily Frame is running reliably without it.'"

**Restoration gate.** LAB-058 captures two conditions: (1) daily Frame runs steadily for ≥ 2 weeks on the textarea form, and (2) the rogaine loop (off-board picks → Debrief pre-fill) is identifiable as the actual constraint on weekly planning quality. Until both are true, the picker stays out. Status revisit queued for LAB-027, LAB-036, LAB-042.

---

## RECOVERY ROOM SHIPS

Three-screen workshop. Step 1 measures the need: sliders pre-set to this morning's Pilot Check reading; withdrawal computed as anchor − current. Step 2 shapes the recovery: chip-based day-shape selector maps to Sonnentag & Fritz mechanisms (Detach / Relax / Master / Control); activity-chip pool keyed by mechanism × locus. Step 3 plans it — including a new "Open turns at lock" section.

**Open turns at lock.** Three choices for live turns you can't close tonight: carry (this turn continues tomorrow), drop (abandon), defer (valid work, park in backlog). Named vocabulary instead of a blank textarea. The Recovery Room is now the place you close not just your body but your open cognitive loops.

Lock persists to localStorage and mirrors to Drive via `/api/save/recoveries` — new server route, same pattern as Frames and Pilot Checks.

---

## FOUR-BAND FLOOR

The lab floor is restructured. Four bands now:

| Band | Contents |
|---|---|
| Band 1 | Storage / holding pens (Drive-canonical) |
| Day-band | Pilot Check + Recovery Room |
| Turn-cycle row | Frame · Comprehend · Sync · Produce · Debrief |
| Meta row | Transition Hallway · Trim Bench · Director's Desk |

Recovery Room moves from the turn-cycle row to the day-band. This is not a visual change only — it's a design claim: Recovery is a daily ritual, not a per-turn phase. `PHASE_SLOTS['recovery-room']` deleted. `kind` taxonomy field added to every non-Band-1 area (ritual / phase / meta).

---

## THE STACKING PROBLEM

PRs #139, #140, and #141 were stacked. Each was meant to merge into main, but each merged into its stacked-base branch instead. Their content didn't reach main on initial merge. PR #143 recovered: the PR3 branch (which held the cumulative content) was opened directly to main, conflicts vs. PR #142 resolved, and the full set landed. Six PRs total, two redundant merge operations, zero lost work.

---

## STAT BOX

| Metric | Count |
|---|---|
| PRs merged to main | 6 |
| Lab items created | 1 (LAB-058) |
| Lab items archived | 4 (LAB-020, LAB-021, LAB-025, LAB-030) |
| LAB briefs rewritten | 2 (LAB-008, LAB-004) |
| DECISIONS entries added | 3 (Heartbeat retirement, Four-band floor, Frame rollback) |
| DECISIONS entries marked Superseded | 2 (Two central images, Gauge merger) |
| New chunks added | 3 (chunk-pilot-yoked-to-recovery, chunk-recovery-bookended-day, chunk-hash-house-pilot-check relocated) |
| Log entries added (May 11 EOD, landed May 12) | 7 (across 6 areas) |

---

## LOOKING AHEAD

May 12 morning: Quenton's lab-restructure walk in Comprehend Station. The Walk Studio product walk for the new floor layout was drafted in parallel — it replaces any walk steps that still reference the retired six-phase layout or the Gauge. The Walk Studio's first authored walk predates the May 11 restructure; some step descriptions are stale. The sweep is queued.

First thing May 12: open the lab, check the new four-band floor, run a Pilot Check, confirm the Recovery Room's anchor-setting path works end-to-end. The bookended day is live in architecture; it needs its first full run.

---

*Filed by Larry Moleman, lab assistant. This edition is the durable record of 2026-05-11's work. For architectural reasoning, see `cognitive-lab/DECISIONS.md`. For the lab's current state, see `cognitive-lab/cognitive-lab-v0.1.html`.*
