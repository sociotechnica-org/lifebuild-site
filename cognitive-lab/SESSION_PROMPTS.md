# Cognitive Lab — Session Prompts

How to start (and close) a session in the cognitive lab. Sibling to `PROCESS.md` (how the lab works) and `DECISIONS.md` (what's been decided).

Last meaningful update: 2026-05-02. Update this file when:

- The state-of-play summary in the long form goes stale
- The current "urgent priority" example shifts
- A new agent joins the system
- The session-close prompt becomes optional (after Debrief Workshop ships, integration moves into Debrief itself)

---

## Standing invocation (any session, short)

The default. Use this once you've oriented Quenton at least once on the current state of the lab.

```
Launch Quenton Quince. We're working in the cognitive lab on
The 7 Turn Work Week framework. Pick up where we left off.

Today: [WHAT YOU WANT TO DO]
```

Quenton's load-brain procedure runs automatically: he reads `quenton-quince/SYSTEM_PROMPT.md`, `METHODOLOGY.md`, `LAB_CONTEXT.md`, `PLAYS.md`, and `PRINCIPLES.md`. He'll orient on the lab state himself.

---

## Pick-up-where-we-left-off (longer, first session on a new branch)

Use this when starting fresh on a new branch (or returning after a gap), so Quenton picks up the right state-of-play without you having to re-explain.

```
Launch Quenton Quince to pick up cognitive-lab work.

Orient by reading:
- cognitive-lab/DECISIONS.md (decisions log)
- cognitive-lab/PROCESS.md (agent composition, two central images,
  daily/weekly rhythm)
- quenton-quince/PLAYS.md and PRINCIPLES.md (your playbook + heuristics)
- The Log tile (experiments array) of frame-workshop, pilot-check-station,
  debrief-booth, the-gauge, transition-hallway in
  cognitive-lab/cognitive-lab-v0.1.html

State of play (update this section as the framework evolves):
- Frame Workshop is shipped (v0.2 four-batch form: Scope / Outcome /
  Approach / Safety; lived-tested 2026-05-01).
- Pilot Check Station is shipped (three-dimension rule-out:
  cognitive king / emotional / physical, threshold ≤3 = grounded).
- Two central images: cache-game (Frame's organizing metaphor) and
  heartbeat (Gauge↔Recovery rhythm).
- Capacity check-in PoC and Pilot Check converge into a unified Gauge
  instrument (LAB-025, queued).
- Quenton (you) and Larry Moleman are project-resident agents (PR #123).
- grepzilla2 covers cognitive-lab/ now (PR #126); use for markdown-heavy
  PRs that Devin skips.

Urgent priority (update as priorities shift):
- LAB-032 (P0): Bootstrap Debrief Workshop. Its absence creates
  session-end integration debt. Until it ships, Larry's
  Session-Integration play substitutes.

Today: [WHAT YOU WANT TO DO]
```

After Quenton orients in that first session, drop back to the standing short form for subsequent ones.

---

## Session-close (Larry's Session-Integration play)

Important. Run at the end of every session **until the Debrief Workshop is shipped (LAB-032)**. After that, Debrief invokes integration as part of its closing procedure, and this standalone call becomes optional.

```
Larry, run the Session-Integration play.

Audit today's session outputs against the lab state. Add missing Log
entries on the affected areas. Draft any chunks or To-Do items that
should be added. Run a cross-reference check for drift between
DECISIONS.md / PROCESS.md and the lab data. Write a master Log entry
on director-desk capturing what was integrated and what's queued.
```

Larry's Session-Integration play (in `larry-moleman/PLAYS.md`) walks through the procedure step-by-step. He'll return a receipt of what he touched.

---

## Larry-only operational asks

Smaller asks that don't need a full Quenton design session. Examples:

```
Launch Larry Moleman. Daily summary of lab state.
```

```
Launch Larry Moleman. Capture this observation as a Log entry on
[area]: [text]. Title it briefly.
```

```
Launch Larry Moleman. Audit DECISIONS.md against the lab data.
Flag any LAB-XXX, area, or chunk references that don't resolve.
```

Larry returns a receipt: what he touched, what he flagged, what's queued.

---

## Concrete example (current top priority — keep this current)

For the very next session, the natural move is bootstrapping the Debrief Workshop. Update this example as priorities shift.

```
Launch Quenton Quince to pick up cognitive-lab work.

Orient by reading cognitive-lab/DECISIONS.md, cognitive-lab/PROCESS.md,
quenton-quince/PLAYS.md, and the Log tiles of frame-workshop,
pilot-check-station, and debrief-booth in
cognitive-lab/cognitive-lab-v0.1.html.

Today: bootstrap the Debrief Workshop (LAB-032). This is the URGENT
priority — Debrief's absence creates the session-end integration debt
Larry's Session-Integration play has been substituting for. Apply the
Bootstrap-a-Workshop play:

1. Wildcat the Debrief on a recent turn (5 min, no template, just
   talk it through).
2. Design the form from the lived data — same four-batch chunking
   thinking we used for Frame.
3. Build the workshop prototype: mark debrief-booth area
   workshop:true; build the form as the resting/editing/viewing
   mode-state machine; wire save handler to auto-Log each Debrief.
4. Seed Chapter chunks from After-Action Review (US Army),
   reflection theory (Kolb, Schön), and surgical post-op debriefs.
5. Update LAB-003 (Debrief form) and LAB-004 (Debrief chapter)
   status as you go.

End the session by running Larry's Session-Integration play.
```

---

## What's automatic — don't bother specifying

Quenton on launch:

- Reads SYSTEM_PROMPT, METHODOLOGY, LAB_CONTEXT, PLAYS, PRINCIPLES
- Reads the relevant area's recent Log entries before proposing
- Won't relitigate decisions in DECISIONS.md
- Leads with opinionated proposals + tradeoff tables
- Cites specific research (Sweller, Hobfoll, Sonnentag, Hockey, Leroy, Klein, Wickens, Risko & Gilbert)
- Pushes back on weak ideas (acronym-driven structure, forced metaphors, duplicate tools)
- Hands operational follow-up to Larry without being asked
- Closes sessions with what was decided / what's queued / next step

Larry on launch:

- Reads SYSTEM_PROMPT, JOB_CATALOG, PLAYS, LAB_CONTEXT
- Returns receipts in the standard format (Did / Noticed / Queued)
- Routes work that exceeds his role to the right agent
- Won't fabricate state — surfaces "Couldn't do" with what would unblock

---

## When to use which form

| Situation | Form |
|---|---|
| First session on a new branch, or returning after a gap | Pick-up-where-we-left-off (long) |
| Subsequent sessions on the same branch | Standing invocation (short) |
| Quick operational ask (no design work) | Larry-only |
| End of any design session | Session-close (Larry) |
| Fresh start on a specific high-priority workshop | Concrete example (current top priority) |

---

## Notes on evolution

This file is meant to stay current. Edit it when the state-of-play summary goes stale or the urgent-priority example shifts. The framework is being built while being used; the prompts that kick off sessions need to keep up.

When the Debrief Workshop ships, the session-close section becomes optional — Debrief itself invokes the integration as part of its closing procedure. Update the section header at that point.

When new agents join the system (e.g., a "Cookie" agent for some specialized role), add their invocation patterns here.
