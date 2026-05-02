# Frame · Research, Form, and Practice

The chunky blocks for the Frame chapter. Skeleton for Zelda to weave from.

This document covers: the form, the research behind each field, the mechanism each
field is operationalizing, when to use the form, how to run it, a worked example
from a real first run, common failure modes, and open questions for v0.2.

---

## 1. The form

Seven fields, plain English, runnable in 5–10 minutes, produces a written card
the Director can refer back to mid-turn.

| Field        | What you write                              | One-line                                                  |
|--------------|---------------------------------------------|-----------------------------------------------------------|
| **Must**     | The floor deliverable(s) for this turn      | What this turn is *not done* without                      |
| **Stretch**  | Bonus pickups, named in advance             | What gets picked up if time and capacity allow            |
| **In**       | Areas, topics, surfaces in scope            | What this turn is touching                                |
| **Out**      | Non-goals, named explicitly                 | What you're deliberately not touching, even when tempted  |
| **Approach** | Mode + what you're leaning on               | How you'll work, and the external scaffold you're using   |
| **Miss**     | Pre-mortem in one or two lines              | What would make this turn a waste                         |
| **End**      | Stop signal — time, output, capacity floor  | When you stop, decided in advance                         |

The form is **selection more than generation**. When the supporting infrastructure
is in place — a backlog of named work items, a record of recent Debriefs, the Gauge
reading — most fields are picked, not invented. Frame leans on a plan rather than
recreating one each morning.

---

## 2. The research behind each field

Eight cognitive-science territories ground the form. None are speculative; all have
decades of empirical work behind them. Most aren't pop-psych; they're the kind of
research that runs in occupational health journals and human factors labs and gets
applied in aviation, manufacturing, medicine, and military operations.

| Field         | Research grounding                                                                                                                                                              |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Must, Stretch | **Goal shielding** (Shah, Friedman, Kruglanski 2002) — one named goal inhibits competing goals; multiple un-ranked goals = no shielding.                                       |
| In, Out       | **Cognitive Load Theory** (Sweller 1988+) — extraneous load reduction is the highest-ROI cognitive intervention. The act of *naming* what's out produces inhibition.            |
| Approach      | **Multiple Resource Theory** (Wickens 1980/2002) — different cognitive modes use different channels; mode-switching is taxed. **Cognitive Offloading** (Risko & Gilbert 2016).  |
| Miss          | **Pre-mortem reasoning** (Klein 2007) — imagining specific failure produces concrete risks; imagining success produces optimistic plans that ignore failure paths.              |
| End           | **Bingo fuel** (combat aviation precedent) + **Compensatory Control Model** (Hockey 1997) + **Conservation of Resources** (Hobfoll 1989) — the cost of pushing past End is real, invisible while it's happening, and paid out of tomorrow's reserves. |

The form as a whole follows the **Checklist Manifesto** design principles
(Gawande 2009): 5–9 items, each item triggers a specific action, runnable in
under ten minutes, and the **IM SAFE** precedent from FAA aviation, where a
short pre-flight ritual is mandatory before every flight and "not today" is a
sanctioned outcome.

---

## 3. How the research works in the form

This is the load-bearing section. For each field: the cognitive job it does, the
mechanism named, and what fails if you skip it.

### Must

**Cognitive job.** Establish a single shielded goal that downstream attention can
defend.

**Mechanism.** Goal shielding (Shah, Friedman, Kruglanski 2002). Once a goal is
explicitly named, the brain inhibits competing goals at both attentional and
behavioral levels. The shielding is automatic, but it requires articulation —
the brain shields what's been named, not what's been vaguely intended. Multiple
un-ranked goals defeat the mechanism; a single primary goal preserves it.

**Failure mode if skipped.** Drift. Mid-turn, the Director re-decides what to
work on three or four times. Each re-decision spends decision capacity on
something that should have been settled at Frame. Decision fatigue arrives
earlier than expected.

### Stretch

**Cognitive job.** Honest acknowledgment that exploratory work is often
multi-output. Structured handling of bonus capacity once the floor is delivered.

**Mechanism.** Goal shielding works on a single primary goal but doesn't preclude
opportunistic secondary goals *if* they're named in advance and ranked below the
primary. Naming Stretch up front prevents two failure modes: (a) Stretch items
getting accidentally promoted to Must mid-turn (which corrupts the shield), and
(b) finishing Must early and not knowing what to do next, so the Director either
wanders or closes the laptop unsure.

The bike-race analogy makes this concrete. In a fixed-time scoring race — make
the finish line by 6 PM, score is determined by what you collected along the way
— two failure modes show up: greedy racers who collect too much and don't make
the finish, and conservative racers who finish early and leave points on the
field. The skill is calibrating where on that spectrum the day should sit.
Frame names the floor; the calibration happens during Push.

**Failure mode if skipped.** Either the Director pushes too hard trying to
complete everything (the racer who missed the deadline) or finishes the floor
and squanders the remaining capacity (the racer who left points on the field).

### In / Out

**Cognitive job.** Make the boundary of the turn explicit and defensible.

**Mechanism.** Cognitive Load Theory (Sweller). Reducing extraneous load — the
load imposed by the *design* of the work, separable from the work's inherent
difficulty — is the highest-ROI cognitive intervention. Naming what's *In*
defines the surface; naming what's *Out* defends it. The act of writing what's
Out is what produces the inhibition. The brain treats unnamed possibilities as
live goals (still competing for attention) and named-as-out possibilities as
deferred. Implicit deferral isn't the same as explicit deferral.

**Failure mode if skipped.** Scope creep. The Director starts on Must, drifts
into a Stretch-adjacent area, then into something that wasn't on either list,
and by mid-Push can't remember why the day began.

### Approach

**Cognitive job.** Pre-select a cognitive mode and a named external scaffold,
preventing mode-switching and pre-loading what Comprehend will need.

**Mechanism (two parts).**

- *Multiple Resource Theory* (Wickens). Cognitive resources are not a single pool
  but a small set of channel-specific pools — verbal-symbolic, spatial-visual,
  motor, etc. Some pairs of tasks can run in parallel without interference (read
  while listening to instrumental music) and others can't (read while listening
  to a podcast). Mode-switching mid-turn — pair-programming, then delegating,
  then writing, then reviewing — pays the switching cost over and over. Choosing
  one mode in Frame defeats the cost.
- *Cognitive Offloading* (Risko & Gilbert 2016). Externalizing cognition to a
  durable system reduces in-head load — but only when the system is *named* and
  *committed to* in advance. Frame's "leaning on" line names what the Director
  is offloading to, which becomes the thing Comprehend loads at the start of
  Push. Without naming it, the Director either re-derives information already
  captured (waste) or doesn't trust the externalized version (also waste).

**Failure mode if skipped.** Mode-thrashing. The Director starts in pair-prog,
switches to delegation when an agent finishes early, switches back when a
decision needs them, switches to writing when wanting to capture something —
each switch leaks attention residue (Leroy 2009; see also the Transition
chapter). Fatigue arrives early. Fewer artifacts get produced.

### Miss

**Cognitive job.** Pre-mortem. Specific risk-naming.

**Mechanism.** Pre-mortem reasoning (Klein 2007). When humans imagine future
success, they generate plans that systematically under-weight failure paths.
When they imagine future failure, they generate specific, concrete risks and
the mitigations against them. The cognitive shift is from
forward-confidence to backward-risk. Naming a Miss in advance creates a
cognitive marker — when the named failure pattern starts to materialize during
Push, the marker fires and the Director redirects in real time, instead of
discovering the lopsidedness only at Debrief.

The strongest Misses name a *symmetric pair* of failures rather than a single
risk. A Director writing a chapter for the first time might name: "lots of
research with no working tool — OR — just a working tool with no notes to
tell the story." Both ends of the balance are named; the win condition becomes
the middle.

**Failure mode if skipped.** The Director won't see the failure mode coming.
Generic worry doesn't create the marker; specific naming does. Without the
named risk, the lopsidedness only surfaces at Debrief, when it's too late to
correct.

### End

**Cognitive job.** Pre-commit a stop signal that survives mid-Push compensatory
effort.

**Mechanism (three parts).**

- *Bingo fuel* (combat aviation). The turnback time is decided when the pilot
  is fresh and on the ground; it's executed regardless of in-the-moment
  confidence about fuel reserves. Pilots in the air, especially after intense
  engagement, systematically misjudge how much fuel they have — the
  pre-commitment defeats the in-the-moment misjudgment. Frame's End is the
  knowledge-work analogue: pre-committed when fresh, executed without
  negotiation when the time comes.
- *Compensatory Control Model* (Hockey 1997). Under high task demand, humans
  compensate for capacity strain by spending more effort, but the cost of that
  effort is invisible to introspection during the activity. Subjective "I feel
  fine" is not a reliable stop signal under load. An external pre-committed
  signal — a clock time, a delivered deliverable — is.
- *Conservation of Resources* (Hobfoll 1989) and recovery research (Sonnentag).
  The cost of pushing past End is paid out of tomorrow's reserves. Loss
  spirals from over-extension are documented; recovery sufficiency is what
  prevents them. End is what protects the next turn.

The strongest End conditions in practice have **two components**: a temporal
limit (the bingo fuel) *and* a named temptation to resist. The temptation
component matters because the bright-red trap — feeling great mid-Push because
dopamine has fully masked depletion — is exactly when "the time is up but I
feel fine" is most persuasive. Naming the temptation in advance ("the desire
to push past 4:30 because the work is exciting") creates a counter-marker
that fires when the temptation arrives.

**Failure mode if skipped.** The 85→100 trap. The Director pushes from
restorable into bright-red territory, and pays tomorrow with hours of
impaired capacity. The temptation to push past is highest exactly when
feeling-good has masked the cost.

---

## 4. When to use the form

**At the start of every Full Turn.** Once the Gauge dispatches "Full," Frame
is the first phase. Required.

**Not on Recovery days.** If the Gauge says "Recovery," there's no turn and no
Frame. Recovery isn't a turn; it's a different mode entirely.

**Lighter form on Partial Turns.** When the Gauge dispatches Partial — reserves
mid, low-load work, no AI — the full form is overkill. A three-field Frame
(Must, In/Out, End) is sufficient. The other fields collapse to defaults.

**Re-Frame triggers.** If conditions change mid-day — a major interruption, a
new urgent request, a Recovery insertion that resets capacity — re-read the
Gauge. If the new reading dispatches a different mode or substantially
different scope, run a new Frame card. The previous one closes; the new one
opens.

**Multi-Push days.** A turn may contain multiple Pushes separated by Recovers.
Run *one* Frame per turn, not one per Push. The Frame holds across the cycle.

**Turns that span sleep.** Frame at evening, work spans sleep, post-sleep
gauge re-read at morning. If the morning re-read dispatches the same scope
as the evening Frame, the same Frame card stays valid — it's the same turn.
If the scope shifts overnight, run a new Frame for the morning continuation.

**Solo vs. team turns.** Solo turns Frame normally. Team turns include a
shared Frame artifact at the Sync phase — the team converges on a shared
Must, individuals retain personal Approach lines.

---

## 5. How to run the form

The actual ritual, from sit-down to first Push action:

1. **Open the workshop.** Click Frame on the lab floor. The drawer expands
   to two-thirds of the screen; the form takes the top half, the floor takes
   the bottom.
2. **Confirm the Gauge dispatch.** Before filling fields, confirm where you
   are on capacity. Frame is for Full Turns. If the Gauge says Partial or
   Recovery, you're in the wrong room.
3. **Write Must first.** Names the floor. *Concrete output*, not topic.
   *"Decide X"*, *"produce Y"*, *"ship Z"* — not *"work on X"* or
   *"explore Y."* The verb tells you whether you've written a Must or a
   Stretch.
4. **Write Stretch.** Bonus pickups, named, prioritized. Empty Stretch is
   fine for tightly-scoped turns.
5. **Write In and Out.** *In* names the surface. *Out* names what you'll be
   tempted by but won't do. Out is doing more cognitive work than In; spend
   more time on it.
6. **Write Approach.** Mode (pair-prog / delegate / write / synth / review)
   and what you're leaning on (specific files, prior turns' outputs, durable
   knowledge sources). Names the external scaffold.
7. **Write Miss.** Pre-mortem in one or two lines. Specific. Often a
   both/and balance failure rather than a single risk.
8. **Write End.** Two parts: *time* (the bingo fuel — when does the turn
   end regardless?) and *temptation* (what will pull you past it that you're
   pre-naming now, while fresh).
9. **Save the card.** It's now the reference for mid-Push checkpoints.
10. **Refer back at mid-Push checkpoints.** Every 50 minutes or so, glance at
    the card. Are you working on Must or have you drifted to Out? Is the
    bingo time approaching? Is the named Miss starting to materialize?
11. **At Debrief, the card is input.** What was framed vs. what happened.
    The delta is the lab note that informs the next Frame.

---

## 6. Worked example — first formal run

Real card produced by the Director on 2026-05-01 at 12:29 PM, after the
workshop layout and form went live the same day. Annotation in italics shows
which cognitive job each field was performing.

**Must.** Completed preliminary FRAME concept and have corresponding research
& "book chapter."

> *Three named outputs (concept, research, chapter). Honestly multi-output for
> an exploratory turn. The bike-race accommodates this — Must can be a small
> bundle when the work is genuinely exploratory, as long as the floor is
> defended.*

**Stretch.** Work on the bookend to this piece of the framework.

> *"Bookend" = Debrief. The Director is thinking in pairs / structure. The
> stretch is named but loosely — would benefit from 2–3 specific Debrief
> outputs to give the bike-race calibration something concrete to chase.*

**In.** Building the workshop to do the work — building the backlog to do the
work. Finalizing the preliminary turn phase.

> *Three threads named: build the workshop, build the backlog, finalize the
> preliminary turn phase. Notice the recursion — using the lab itself as a
> tool to build the framework. This is exactly the plan-pointing principle:
> Frame leans on a backlog; the backlog enables Frame.*

**Out.** Alexandria-ing it. Working on Alexandria. Being more of a blogger
than a creator.

> *Two anti-patterns named in the Director's own voice. Implicit deferral
> wouldn't have produced these. The act of writing them is what shielded
> against them — when an Alexandria-shaped task surfaces during Push, the
> named anti-pattern fires.*

**Approach.** Pair work — try to lean on the environment as much as possible.
Build a magical workshop to support my work.

> *Mode (pair work) + leaning-on (the environment). The word "magical" is
> doing real work — it captures a quality target for the Workshop UX. Worth
> capturing as a lab note.*

**Miss.** Lots of research and no tool OR just the tool and no notes to tell
the story.

> *Symmetric-pair pre-mortem. Both ends of a balance failure named. The win
> condition is the middle (both/and), not the avoidance of one risk. Stronger
> than a single-risk pre-mortem.*

**End.** Work ends at 4:30 today. I need to have the discipline to put this
down even though I'm so excited.

> *Two components: temporal (4:30) and dispositional (discipline-to-stop).
> The second component is bingo-fuel in plain language — naming the
> bright-red temptation in advance, while fresh, exactly as the framework
> intends. Strong candidate for a permanent second-line in End.*

**Outcome.** The turn produced (a) the form, (b) the workshop layout, (c)
this research-and-practice document, (d) a worked example (this card),
(e) the foundation for the Debrief and Pilot Check chapters. Bingo time
held. The named Miss was avoided — both research and tool were produced,
with notes that tell the story.

---

## 7. Failure modes

Six common ways Frame breaks. Each has a counter.

**Frame theater.** Filling fields without intent to refer back. Counter:
the mid-Push checkpoint at step 10 of the ritual. If the card isn't being
glanced at during Push, Frame collapsed to ritual.

**Over-detailed Frame.** Writing 200 words per field. Counter: the timing
constraint. The form should run in 5–10 minutes. If it takes 20+, the
fields are absorbing work that belongs in Push.

**Never-referred-to Frame.** Write once, never look at again. Counter: the
card has to be visible during Push for the shielding mechanism to hold.
Workshop drawer staying open is one solution; a printed card on the desk is
another. Out of sight, out of shielding.

**Skipping Frame on small turns.** "This is a quick one, I don't need to
Frame it." Counter: small turns benefit *most* from a 60-second Frame
because the temptation to drift is highest when the perceived stakes are
low. The floor / non-goals discipline costs nothing on a small turn and
prevents the small-turn-becomes-three-hour-turn drift.

**Frame-as-planning-document.** Trying to figure out *how* to do the work
inside the form. Counter: Frame names what to do; Push figures out how. If
the form contains step-by-step plans, the phases are blurred. Push will
take longer because Frame absorbed work that belonged downstream.

**Wishful Must.** Naming a Stretch as a Must. Counter: tell from the verb.
*"Decide / produce / ship / complete"* is Must-shaped. *"Explore / consider
/ look into / continue"* is Stretch-shaped. If the verb won't commit to a
specific output, the item is Stretch.

---

## 8. Open questions and v0.2 candidates

What today's first formal run surfaced.

1. **End as Time + Temptation.** Promote the Director's improvisation from
   today's card to a permanent second line. The form becomes:
   - *Time:* ____
   - *Temptation to resist:* ____
   The temptation line captures the bright-red bingo-fuel pre-commitment
   in plain language. Strong evidence it's load-bearing — it appeared
   unprompted on the first run.

2. **Posture as a separate field.** Creator vs. blogger / commentator is
   a posture, distinct from Approach (mode). Today's card put creator-mode
   in Out (as an anti-goal) because there was no positive-framing field
   for it. A separate Posture line would let the positive choice stand
   on its own. Open question: separate field, or fold into Approach as
   "Mode + Posture"? Lean toward folding for now (form stays at seven
   fields), revisit if a Posture-specific failure mode emerges.

3. **Plan-pointing infrastructure.** Frame should select Must from the
   Backlog Wall, not generate from scratch. Currently free-text. v0.2
   could let the Director click a backlog item ID and auto-populate Must
   with the item's title; Stretch could be multi-select. The free-text
   override stays available for items that don't yet exist in the backlog.

4. **Re-Frame button.** Distinct from Save. Closes the previous card and
   starts a fresh one with a new date+time stamp. Useful when conditions
   change mid-day and a new turn begins.

5. **Mid-Push checkpoint cue.** A 50-minute timer or visual prompt inside
   the workshop, prompting the Director to glance back at the card. Could
   be opt-in. Solves the never-referred-to-Frame failure mode at the
   discipline level.

6. **Wildcat lite.** A short-form variant for partial turns or quick
   re-Frames mid-day. Three fields: Must, In/Out, End. Saves to the same
   history.

7. **Card export to lab note.** A button that promotes the saved card into
   the Archive area's labNotes list, capturing the day's Frame as part of
   the durable record.

---

## 9. Lab notes from today (candidate Archive entries)

- **2026-05-01 — Frame form v0.1 ran end-to-end.** Produced a usable card in
  ~12 minutes. All seven fields had substance. The form is now at "drafted"
  status — no longer a sketch, not yet hardened by repeat runs.
- **2026-05-01 — "Magical workshop" as a quality target.** The Director's
  word for the experience of using the workshop today. Captures the bar for
  v0.2 of the lab itself: the workshop should feel magical to use, not just
  functional.
- **2026-05-01 — End-as-Time+Temptation surfaced unprompted.** The Director
  added *"discipline to put this down even though I'm so excited"* to the
  End field on the first run. This is bingo-fuel in plain language. Strong
  candidate for v0.2 of the form (see open questions §1).
- **2026-05-01 — Symmetric-pair Miss is stronger than single-risk.** The
  Director's Miss named both ends of a balance failure (research vs. tool).
  Worth elevating to chapter material as the Miss-pattern of choice.
