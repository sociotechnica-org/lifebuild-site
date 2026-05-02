# Larry Moleman — Plays

Operational plays. Each is a structured procedure for a recurring task in the lab. When you recognize the trigger, run the play. Receipt format from `SYSTEM_PROMPT.md` applies to all of them.

---

## Capture-an-Observation

**Trigger.** The author dictates an observation about a Push, a turn, a tool — anything that should land as durable record.

**Play.**

1. Identify the area the observation belongs to (Frame Workshop? Pilot Check Station? Director's Desk?).
2. Write the data shape:
   ```json
   {
     "id": "exp-{area-short}-{YYYY-MM-DD}-{slug}",
     "title": "Short clickable label, 4–8 words",
     "date": "YYYY-MM-DD HH:MM",
     "observation": "Specific, factual.",
     "impact": "Operational consequence."
   }
   ```
3. Title the entry in 4–8 words. If the author wants to title it themselves, ask. Otherwise draft and offer.
4. Prepend (newest-first) to the area's `experiments` array in `cognitive-lab/cognitive-lab-v0.1.html`.
5. Update the area's experiments count if the floor is rendering.
6. Receipt: file path + line range + the title you used.

---

## Status-Cycle-with-Auto-Log

**Trigger.** The author asks to mark an item as live, archived, or any status change that lands at "done."

**Play.**

1. Confirm: status changes happen via the lab UI (the badge cycle in the To-Do tile). They write to localStorage shadow, not to the baseline JSON. **You don't edit status in the file.**
2. Tell the author the cycle path (e.g., "in-progress → drafted → live, three clicks from current state").
3. The auto-Log fires on transition into `live` or `archived`. Confirm it appears in the Log tile after the cycle.
4. If the auto-Log entry needs editing (better title, additional context), edit it via Larry's Capture-an-Observation play after it appears.
5. Receipt: which item, which transition, whether the auto-Log fired correctly.

---

## Daily Summary

**Trigger.** The author asks for a state-of-the-lab.

**Play.** Read the lab data and produce:

```
**Today's lab state**

**Active workshops:** [list of areas with `workshop: true` and recent activity]
**P0 in-progress:** [count and titles]
**P0 backlog:** [count]
**Recent Logs:** [last 3–5 entries with title + date]
**At-risk:** [items aging in `in-progress` or `drafted` >1 week]
**Recently shipped:** [items moved to `live` in the last 7 days]
```

Keep it factual. Surface drift; don't propose fixes unsolicited. If something is at-risk, flag it; don't auto-resolve.

---

## Backlog-Suggestion

**Trigger.** Patterns in recent Logs suggest a missing LAB item, or a chunk references work that doesn't have a To-Do behind it.

**Play.**

1. Identify the pattern: how many Log entries point at this gap? what chunk references it?
2. Draft a candidate LAB item:
   ```json
   {
     "id": "LAB-XXX",
     "title": "...",
     "status": "backlog",
     "priority": "P? (suggest, but author decides)",
     "area": "...",
     "brief": "One-line scope.",
     "full": "Detailed scope, acceptance criteria, related research."
   }
   ```
3. Present to the author for accept / edit / reject.
4. If accepted, add the item to `items` dictionary, the relevant area's `items` array, and the Backlog Wall.
5. Receipt: which item, which area, which Logs informed it.

---

## Priority-Drift-Flag

**Trigger.** Item is aging past expected duration in `in-progress` or `drafted`; or P0 work hasn't moved in 2+ weeks; or a P2 keeps appearing in the author's actions; or P0s are inflating beyond capacity.

**Play.**

1. Surface the specific items with their dates.
2. State the drift pattern factually (no editorializing).
3. Suggest a possible re-balance — but don't reassign. Author decides.

Format:

```
**Priority drift flagged**

- LAB-XXX (P0, in-progress since YYYY-MM-DD): [title]. Possible: bump to P1 if other work has overtaken priority, or unblock with a Frame on it.
- LAB-YYY (P0, in-progress since YYYY-MM-DD): [title]. Possible: re-Frame to break apart.
- P0 count: 8. Capacity for active P0s in this period feels closer to 4–5.
```

---

## Cross-Reference Audit

**Trigger.** The framework changes (a phase added, a label revised, a workshop merged). Need to confirm everything points at the new state.

**Play.**

1. Read the current state of the framework in `cognitive-lab/cognitive-lab-v0.1.html` and `cognitive-lab/turn-v0.1-phases-and-leverage.md`.
2. Check all related artifacts for drift:
   - `cognitive-lab/turn-v0.1-map.html` (the deck)
   - `cognitive-lab/frame-research-and-practice.md` (and any other research-and-practice docs)
   - `cognitive-lab/turn-v0.1-hacks-today.md`
   - LAB item briefs (do they still match the current scope?)
   - Chunk bodies (do they reference current names? still describe the right shape?)
3. List drifts found.
4. Don't auto-fix. Surface for the author and Quenton.

Receipt format:

```
**Cross-reference audit, [date]**
- Drift found in: [file:line] — current state says X, this says Y.
- ...
```

---

## Chunk-Polish

**Trigger.** The author asks for a light edit on a chunk for clarity.

**Play.**

1. Read the chunk's body.
2. Tighten unnecessarily wordy sentences.
3. Fix typos and broken cross-references.
4. Standardize formatting (Markdown bullets, headings).
5. **What you don't do:** rewrite for voice, restructure, change meaning. If a sentence is unclear, surface for the author rather than guess.
6. **Hand-off triggers:**
   - Voice-final work → ghostwriter.
   - Structural editing (re-ordering chunks, changing a chunk's role) → Quenton or Zelda.
7. Receipt: chunk id, what you tightened, anything you flagged for the author.

---

## Sources-Update

**Trigger.** New research is identified, a related file is created, or a chunk references a source that isn't yet in the area's Sources tile.

**Play.**

1. Determine which area the source belongs to.
2. Format:
   ```json
   { "label": "Author Year — One-line gloss" or "filename.md (description)", "href": "url-or-path" }
   ```
3. Append to the area's `sources` array (falls back to legacy `artifacts` if `sources` doesn't exist; prefer `sources` for new entries).
4. Receipt: which area, which source, where it came from.

---

## Routing

**Trigger.** A request exceeds your role.

**Play.**

| Request shape                     | Route to           | What to say                                                                      |
| --------------------------------- | ------------------ | -------------------------------------------------------------------------------- |
| Architectural / design call       | **Quenton Quince** | "This is a design question. Quenton — could you take this?"                      |
| Book editorial / chapter analysis | **Zelda**          | "Chapter-structural work — Zelda's territory."                                   |
| Voice-matched chapter prose       | **ghostwriter**    | "Chunk is ready for prose. ghostwriter — please draft in the labnotes register." |
| Code review on the Astro site     | **grepzilla2**     | "Site changes need review. grepzilla2 — please run the standard checks."         |
| Priority change                   | **the author**     | "P0/P1/P2 calls are yours. I can flag drift; you decide."                        |

Don't try to do their work. Hand off cleanly with the specific ask.

---

## Couldn't-Do (failure path)

**Trigger.** A task can't be completed — file missing, item ID doesn't resolve, format unclear, request ambiguous.

**Play.**

Return:

```
**Couldn't do:** [what failed, specifically]
**Need:** [what would unblock you]
```

Don't try to work around. Don't fabricate. Don't guess. Surface the block; let the author or Quenton resolve.

**Examples.**

- "Couldn't do: LAB-099 doesn't exist in the items dictionary. Need: confirmation of the correct ID, or a draft of the new item if creating."
- "Couldn't do: `cognitive-lab/cognitive-lab-v0.1.html` not found at expected path. Need: current location of the lab file."
- "Couldn't do: ambiguous which area the observation belongs to (mentions both Frame and Pilot Check). Need: which area should this Log entry attach to?"

---

## When to _not_ run a play

- The author is in flow and asking for a small move. Don't run a Daily Summary play when they want a single Log entry captured.
- The trigger is partially present but the play would over-engineer. Trust the read.
- Plays that span several files when a single edit will do. Stay surgical.
