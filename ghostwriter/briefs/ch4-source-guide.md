# Source Material Guide: Ch 4 v4 -- See the Board

**For:** Ghostwriter (new tab, fresh context)
**Prepared by:** Zelda Felfenlagger
**Date:** 2026-03-19

---

## What This Document Is

You are drafting Ch 4 v4 -- a fresh rewrite to fix a voice problem that contaminated v1 through v3. This guide tells you exactly what to read, what to carry forward, and what to ignore.

---

## Files to Read (In This Order)

### 1. The Updated Brief

**File:** `ghostwriter/briefs/ch4-see-the-board-v4.md`
**Why:** This is your contract. It contains the voice directive, beat-by-beat instructions, kill list, thread checklist, and voice standard examples from the locked chapters. Read every word.

### 2. Locked Chapter 1 (Voice Standard)

**File:** `src/content/book/chapter-1.md`
**Why:** This is the voice standard. Study the dishrag scene (Beat 2), the intern confession (Beat 3), the infrastructure comparison (Beat 3), and the death spiral (Beat 5). These show what the target register sounds like -- in narrative AND teaching AND implementation beats. Pay special attention to how Beat 3's professional/personal infrastructure comparison works: the FORMAT is the joke. The professional side is formatted like an org chart; the personal side descends into chaos. Beat 1 of Ch 4 should use the same structural move.

### 3. Locked Chapter 2 (Voice Standard for Teaching)

**File:** `src/content/book/chapter-2.md`
**Why:** This is the voice standard for teaching beats specifically. Ch 4 Beats 2 and 3 are teaching beats. Study how Ch 2 teaches bronze/silver/gold through the mold on the porch and the college-readiness conversations. Study how it teaches red/gray/blue through the strategy game night. Every framework is taught through a specific personal failure. Ch 4's teaching beats must do the same.

### 4. Voice Profile

**File:** `ghostwriter/SYSTEM_PROMPT.md` (the patched version)
**Why:** The system prompt has been patched to close the "teaching register" loophole. Read the Voice Gate section, the expanded Moves to Avoid, and the WARNING about teaching register.

### 5. Voice Samples

**File:** `ghostwriter/VOICE_SAMPLES.md`
**Why:** These are the author's actual labnotes. The anti-patterns at the bottom show what to avoid.

### 6. Old Ch 6 (Source Material for Content Only)

**File:** `src/content/book/chapter-6.md`
**Why:** This is the original prose that Ch 4 is built from. Use it for CONTENT reference only -- the research citations, the spectrum structure, the bidirectional loop concept, the failure modes. DO NOT use it for voice. The old Ch 6 is in manuscript voice (academic, third-person generalizing). Every sentence you carry from it needs voice surgery.

### 7. Blueprint

**File:** `zelda/BLUEPRINTS.md` (Ch 4 section, starts at line 1133)
**Why:** The architectural contract. The brief overrides the blueprint where they conflict (the brief is newer and incorporates three rounds of revision learning).

### 8. Book Context

**File:** `zelda/BOOK_CONTEXT.md`
**Why:** Full book context, thread map, key frameworks. Reference as needed.

---

## Files to IGNORE

### DO NOT READ: `ghostwriter/drafts/ch4-see-the-board-v1.md`

**Why:** First draft. Contaminated with depersonalized instructional voice throughout. No salvageable prose beyond what is quoted in this guide.

### DO NOT READ: `ghostwriter/drafts/ch4-see-the-board-v2.md`

**Why:** Second draft. Same voice contamination as v1, slightly improved. Superseded by v3.

### DO NOT READ: `ghostwriter/drafts/ch4-see-the-board-v3.md` (as a whole)

**Why:** Third draft. 60% of prose is in the wrong voice. However, specific passages from v3 are carried forward -- they are quoted directly in the beat-by-beat verdicts below. Read ONLY the quoted passages, not the full draft. If you read the full draft, you will absorb the wrong voice.

### DO NOT READ: `ghostwriter/briefs/ch4-see-the-board.md` (the old brief)

**Why:** Superseded by the v4 brief. The old brief did not include the voice directive or the voice standard examples.

### DO NOT READ: `ghostwriter/briefs/ch4-v2-revision-directives.md`

**Why:** Superseded. These were structural fixes for v1->v2. No longer relevant.

---

## Beat-by-Beat Verdict

For each beat: what to carry forward, from where, and what to write fresh.

### Beat 1: The Professional/Personal Contrast

**Verdict: REWRITE FROM SCRATCH**

Nothing from v3 survives as prose. The entire beat was written using the "Consider how much..." TED talk pivot and narrated the reader's professional life instead of the author's. The CONTENT is correct (professional/personal contrast, Part III transition, old playbook callback, OS metaphor touch, micro-skill callback). The PROSE is wrong.

**One line to carry forward (reposition as needed):**

- "Your head ran out of room three chapters ago."

**Voice model:** Ch 1, Beat 3 -- the professional/personal infrastructure comparison. Use format-as-punchline: the author's professional visibility infrastructure vs. the author's personal visibility infrastructure.

---

### Beat 2: The Spectrum of Visibility

**Verdict: REWRITE FROM SCRATCH with specific carried-forward sentences**

The structure is correct (four subsections: head, lists, spatial, navigable). The research deployment was mostly fixed in v3. But every subsection opens with depersonalized instruction, not the author's experience. That is the v4 fix: every subsection opens in first person.

**Specific lines to carry forward from v3 (these passed voice audit):**

- "This is where I started and where I stayed for years: everything held in working memory."
- "Four. If you have a dentist appointment, a work deadline, an overdue email, and a grocery list, you are at capacity. Everything else is either gone or costing you."
- "Your brain identifies images in 13 milliseconds -- faster than a single eye blink."
- "Lists flatten what the mind naturally organizes spatially."
- "Your brain wants to put things in places. Lists refuse to let it."
- "The hippocampus -- the brain's memory center -- runs on spatial processing. Place cells fire when you're in a specific location. Grid cells provide a coordinate system for navigation. This architecture is so fundamental it earned its discoverers the 2014 Nobel Prize."
- "Your brain won a Nobel Prize's worth of spatial architecture, and you've been feeding it bullet points."
- "But if you have ever stared at a kanban board and still felt like you could not see your life -- columns on a flat screen, cards floating in abstract space -- that is because you are looking at a diagram of a space, not moving through one."
- "The spectrum runs from head (weakest) to lists to spatial organization to navigable environments (strongest)."

**Lines from v3 that must NOT reappear:**

- "Most productivity advice treats visibility as binary: either you have a system or you don't."
- "The reality is a spectrum, and where you land on it affects how well your brain can work with the information."
- "So you write things down. That's the advice, right?"
- "Todoist, a notes app, a paper notebook -- the medium matters less than the act of getting things out of your head."

---

### Beat 3: The Bidirectional Loop

**Verdict: REVISE from v3 -- 60% correct, needs first-person anchoring**

v3 improved this beat significantly. The opening third narrates the loop through the author's experience. The middle drifts back to second-person instruction. The Zhang & Norman quote and the closing bridge are both correct.

**Carry forward from v3:**

- "Here is what actually happens. You sit down to build the board, and your existing mental model does the work -- you already know that fixing the roof goes under Home..."
- "I put sixty-odd items on a digital whiteboard and the first thing I saw was that one territory was packed while two others were nearly empty."
- "The system isn't just in your head. It's not just on the screen. It's in the interaction between them."
- Zhang & Norman quote and surrounding context
- "That is the theory. Here is what it looked like in practice."

**Rewrite from v3:**

- "You already have a mental model of your life." (second person opening, needs first-person rewrite)
- "Right now, without any tool, you can think spatially..." (sustained second person, needs anchoring)
- "That changes what you know. What felt like one overwhelming project turns out to be three separate things..." (drifts to generic second person)

---

### Beat 4: Seeing My Life

**Verdict: CARRY FORWARD from v3 -- 90% correct**

This is v3's strongest beat. It was always in first person, so the voice contamination barely touched it. The emotional reweight around the empty domain is done correctly. The essentialist connection lands.

**Carry forward the entire beat from v3.** Minor adjustments only:

- Placeholders remain as author dependencies
- The closing line "I did not add a habit. I built a structure, and the structure showed me where to look." is the beat's capstone -- preserve it exactly

---

### Beat 5: Three Levels

**Verdict: REWRITE FROM SCRATCH with carried-forward structure and key lines**

The structure is correct (Light, Medium, Full). The content is correct. The voice is wrong -- every paragraph reads like a product manual. Each level needs the author's personal experience woven in.

**Carry forward from v3:**

- The weekly review emphasis: "And then the practice that makes the rest of it work: **Weekly review. Twenty minutes. Same time each week.**" and "This is not an administrative chore. This is the twenty minutes where you stop being inside your life and start looking at it from above."
- "The goal isn't the tool. The goal is engaging spatial cognition -- whether that's a digital environment, a wall of sticky notes, or a whiteboard in your kitchen."

**Everything else in this beat needs rewriting** with first-person anchoring.

---

### Beat 6: What Goes Wrong

**Verdict: CARRY FORWARD from v3 -- 85% correct, minor voice fix**

The four failure modes are well-written. The household member briefing is clean. The only issue is the opening sentence.

**Carry forward the entire beat from v3.** One fix:

- Replace "Every capability has failure modes -- ways that well-intentioned efforts go sideways." with something personal: "I made every one of these mistakes. Some of them twice." or similar.
- Add one "I" sentence to each failure mode if possible.

---

### Beat 7: The Foundation / Forward Pivot

**Verdict: REVISE from v3 -- 75% correct, needs personal opening**

The essentialist connection is strong. The forward pivot is strong. The opening is generic.

**Carry forward from v3:**

- "That's the pattern I keep finding: the system does the work that willpower can't sustain. The empty domain on my board didn't need motivation. It needed two experiments and permission to explore. The board made that obvious. I never would have seen it from inside my own head."
- "You can see the board now. The next question is obvious: who's going to handle all of this?"

**Rewrite from v3:**

- "Visibility is the first capability you've installed as a boss." (generic opening, needs the author's specific experience)
- "Start with the light implementation if that's where you are." (instruction without anchoring)

---

## Summary Table

| Beat | Verdict                                   | Source                      | % Usable from v3 |
| ---- | ----------------------------------------- | --------------------------- | ---------------- |
| 1    | REWRITE FROM SCRATCH                      | One line from v3            | 5%               |
| 2    | REWRITE FROM SCRATCH (with carried lines) | 9 specific lines from v3    | 30%              |
| 3    | REVISE from v3                            | Specific passages from v3   | 60%              |
| 4    | CARRY FORWARD from v3                     | Entire beat                 | 90%              |
| 5    | REWRITE FROM SCRATCH (with carried lines) | 2 specific passages from v3 | 15%              |
| 6    | CARRY FORWARD from v3                     | Entire beat, minor fix      | 85%              |
| 7    | REVISE from v3                            | Specific passages from v3   | 75%              |

**Overall:** Roughly 50% of v3 survives into v4. The other 50% is rewritten in the correct voice. The carried-forward passages are quoted in this guide so you do not need to read the full v3 draft.

---

## The One Thing to Remember

The locked chapters (Ch 1, Ch 2) are the voice standard. Not just for narrative beats -- for ALL beats. If you are writing a teaching paragraph and it could appear in any productivity book, stop and rewrite it so it could only appear in THIS book, written by THIS person.
