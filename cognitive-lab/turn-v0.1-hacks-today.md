# The Turn · Hacks for Today (v0.1, satisficing mode)

Companion to `turn-v0.1-phases-and-leverage.md`. That document describes what each phase
will look like once Alexandria is live and the AI-native operating system exists. **This
document is the hack guide for surviving without it.**

The framework holds. The Substrate, Cockpit, Ledger, and Playbook the framework leans on
do not yet exist as live systems. So you're hand-rolling each phase from primitive tools:
files, folders, git, AI windows, voice memos, Cowork, the capacity-check-in PoC, SnapTool,
calendar.

Satisficing rule: crappy first version that works > nothing. Every hack below is at the
"just enough to get through the day" tier.

---

## What you already have

- **A capacity check-in PoC** that works in localStorage. Withdraw, replenish, color
  verdict, morning-after grading. This is your Ledger today. It just needs to be used.
- **Conductor workspaces** that let you run parallel AI sessions on different branches.
  Janky, but it's a real cockpit if you treat it like one.
- **Cowork** with one scheduled task (morning capacity check-in). One slot already wired.
- **A git repo with `.context/` directories** that act as a poor-man's Library — every
  workspace has a place to drop intent, plans, briefs.
- **`~/.claude/projects/` memory files** — auto-memory across conversations. This is
  poor-man's persistent agent context.
- **SnapTool** for screen capture.
- **Voice memos** + transcription on your phone.
- **Yourself, working with Jess** — two-person sync is mostly a text channel and the
  occasional call.

That's the kit. Now the phase-by-phase hacks.

---

## Match: pre-flight capacity check (above the cycle)

**The principle, in your words: matching activity to capacity.** Before any phase fires,
read the gauge. The Ledger is a *gate*, not just a measurement — its first job is to set
the day's mode, not to record the day's outcome.

**Three modes the cycle can run in:**

- **Full turn.** Reserves high, the six phases run as designed. AI in play. Decision
  work in Push.
- **Partial turn.** Reserves mid. Low-load work only. No AI, or AI for narrow,
  low-stakes tasks. Personal stuff, errands, simple work, social. The day produces
  something but doesn't tax decision capacity.
- **Recovery day.** Reserves low. No turn. Active recovery — blue activities,
  detachment, master/relax mode. The job today is to make tomorrow possible.

**The "ready" signal.** The transition from partial → full has a subjective feel that's
worth training to recognize. Caffeine landed, social engagement closed, body settled, a
specific "okay, I'm in" moment. Worth logging in the debrief: *what did "ready" feel like
today?* Over time, this builds an early-detection skill for both directions — when ready
arrives, and when it has not.

**Hacks today:**

1. **Read the capacity check-in before deciding what kind of day to run.** That's the
   gate move. Don't open the first AI window until the gauge has been read.
2. **Reframe the morning Cowork prompt to ask "full / partial / recovery?"** instead of
   only nudging the check-in. Make Cowork the gate-keeper.
3. **Keep a pre-defined low-load list** — errands, personal admin, a manual chore, a
   walk, a friend you've been meaning to text. Partial days need a place to point energy
   that isn't the laptop.
4. **Honor the gauge even when it's inconvenient.** This is the Whole-Man Rule applied
   at the start of the day: don't open a turn you're not ready for. The cost of forcing
   a full turn on empty reserves is bigger than the cost of a half-day of low-load work.

**Cost:** five minutes of honesty. **Saves:** the difference between a 0–2 productive
hour day with a damaged tomorrow, and a full evening session today.

---

## Frame  (5–15 min) — hacks today

**The pain:** no Substrate to lean on. Every morning starts cold. You can either drift
into the first AI window of the day (high cost) or you can spend 5 minutes deciding what
this turn is *for*.

**Hacks that work today:**

1. **A `today.md` file in `.context/` of whichever workspace you're starting in.** Five
   prompts, overwritten daily:
   - The single decision this turn must produce
   - What I am *not* doing today (named)
   - What I'm leaning on (which prior conversation, which doc, which file)
   - Bright-red trap to watch for
   - Stop condition (when do I close the laptop?)
2. **Re-purpose the Cowork morning task** to literally ask these five questions instead
   of just nudging. Make Cowork the Frame interrogator.
3. **Read yesterday's debrief before framing today.** If you don't have a debrief yet,
   you're starting the discipline today.
4. **Pre-mortem in two lines.** "What would make this turn a waste? Avoid that
   specifically." That's the whole exercise.

**Cost:** five minutes. **Saves:** typically the first two hours of bad scope.

---

## Comprehend  (30–60 min) — hacks today

**The pain:** ten open windows, no idea which agent is doing what. You said this is the
acute one.

**Hacks that work today:**

1. **A manual agent table.** A small markdown table you maintain by hand at the start of
   each turn. Three columns: window, status (1 line from each agent), what it needs from
   you. Update once per turn.
2. **SnapTool composite.** Capture each window in a known order, paste into one image.
   That image is your cockpit-of-the-day. Cheap, visual, low effort.
3. **`git log --oneline -20`** as a ground-truth ledger. What actually shipped is in the
   repo, not in the chat. Read it before reading any agent thread.
4. **One-line status request.** A prompt you paste into every active window first thing:
   "One sentence: where are you, what do you need from me to continue, what should I know
   that I might miss." Aggregate the answers.
5. **Skim-read, don't audio.** Per the modality answer: 5× scan-reading beats 2× audio
   for technical agent output. Read transcripts; don't dictate them aloud.

**Cost:** 15–30 minutes. **Saves:** the entire first hour of "wait, where was I?"

---

## Sync  (30–60 min) — hacks today

**The pain:** you and Jess. You and yesterday-you. No team-wide artifacts.

**Hacks that work today:**

1. **A daily message to Jess at the same time** with the SBAR shape: situation,
   background, assessment, recommendation. Even just three lines.
2. **A "solo sync" pass** — read yesterday's debrief, write three priorities, push back
   on them once before locking in. This is sync with prior-you.
3. **A shared `team.md` doc somewhere** (or just a Slack DM thread used as one). Where
   things you both need to know go. Async sync is sync.

**Cost:** 5–15 minutes. **Saves:** decision collisions that would cost both of you a
half-day to untangle.

---

## Push  (2–3 hr) — hacks today

**The pain:** the 85→100% trap, latency tab-switching, multi-window thrashing.

**Hacks that work today:**

1. **Single-window rule during push.** Minimize every other Claude tab. Cmd-Tab cost is a
   feature, not a bug — friction is what you want here.
2. **Hardest decision first, written at the top of the push file.** Sequential decision
   degradation is real; you want first-fresh-best.
3. **Phone in another room. Notifications off.** Standard but matters.
4. **Voice memo for "park this."** When a thought from another thread surfaces during
   push, capture it in 10 seconds via voice memo so you don't context-switch to type it.
5. **Pomodoro timer at 50 min for mid-push self-check.** One question: "Reserves still
   high?" If no, transition.
6. **The Whole-Man stop signal.** Pre-commit to a stop time. Tell Jess. Tell the calendar.
   Tell the agent. The decision to stop has to happen *before* you're tempted to push
   past it, because in-the-moment-you doesn't have the leverage.

**Cost:** 0–5 min of setup. **Saves:** the catatonic next-day six hours.

---

## Debrief  (10–20 min) — hacks today

**The pain:** the cycle doesn't close. You don't know what just happened. No compounding.

**Hacks that work today:**

1. **2-minute voice memo at end of push.** "What happened, what surprised, what to carry
   forward." Transcribe later if you want; the memo is the artifact.
2. **Append to `.context/lab-notes.md`** with date-stamped entry. Bullet-form, even
   sparse. The compounding lives in the file existing, not in the entries being polished.
3. **Use the capacity check-in PoC's evening tab.** It's already a debrief tool. Withdraw
   score, what did the withdrawing, what's on the recovery menu.
4. **Open-question parking lot.** Things you didn't answer this turn. They become input
   to tomorrow's Frame.

**Cost:** 10 minutes max. **Saves:** the loss of every insight you had today that you'd
otherwise re-invent next week.

---

## Recover  (until next turn) — hacks today

**The pain:** "rest" is undifferentiated and most of what you call rest probably isn't.

**Hacks that work today:**

1. **Pick a recovery mode before the period starts.** Detach (no work signals at all),
   relax (low arousal, parasympathetic), master (a hard new thing — language, music,
   cooking, climbing), control (do what you choose, when). Picking one is the work.
2. **A no-laptop time enforced by physical position.** Laptop closes; goes in a drawer or
   another room. The friction of retrieval is what makes the rule hold.
3. **One detection question at end of day:** "Did what I called rest leave me better, or
   did it just feel like rest?" Captures the bright-red-rest pattern (scrolling, half-TV,
   half-present family time).
4. **Use the morning-after capacity check-in to grade it.** This is what closes the loop.
   The PoC already does this — actually use it daily.

**Cost:** 0 minutes — you're going to "rest" anyway. **Saves:** the next day's reserves.

---

## Transition (meta) — hacks today

**The pain:** every window switch leaks attention residue. You're doing this all day.

**Hacks that work today:**

1. **Stand up at every phase boundary.** Physical move forces a cognitive move.
2. **Drink water at every transition.** Easy anchor, also hydrates.
3. **Verbal close-and-open.** Out loud: "Closing Frame. Opening Comprehend." Sounds
   silly, has weight. Saying it out loud commits the brain.
4. **A 60-second pause between AI windows.** Not productive time, deliberate decompression.
   Walk to the kitchen. Look out the window. Don't pick up the phone (that's a
   different task, not a decompression).
5. **Inter-turn ritual.** Same closing move at the end of each turn — a specific gesture
   that means "this turn is closed, the next one starts later." Coffee mug rinsed and
   inverted. Whatever.

**Cost:** 60 seconds × n boundaries. **Saves:** the residue tax that's currently silent.

---

## Ledger (telemetry) — hack today

**The pain:** none, actually. You built this already.

**The hack:**

1. **Use the capacity check-in PoC daily.** Both tabs. Without exception. Even if the
   entry is sparse.
2. **Wire the URL into the existing Cowork morning task** (per the build plan).
3. **Export the JSON weekly to `.context/`.** Backup hedge against the localStorage
   bus-factor problem.

That's it. The Ledger is the most-built piece you have. It just needs daily use.

---

## Substrate (your poor-man's Library)

Until Alexandria is live, your durable knowledge sources are:

- `.context/` directories in workspaces (intent, plans, briefs)
- `~/.claude/projects/.../memory/` files (auto-memory across conversations)
- Past conductor conversations (re-openable, search by branch name)
- The book repo itself (the writing IS the documentation)
- Notes app / Bear / Obsidian for off-repo material

**Hack:** at end of each turn, ask: "Did anything from this turn deserve to live longer
than this conversation?" If yes, write it to a file before the conversation gets
compressed. The compression bus-factor problem is real — chat history is *not* substrate.

---

## Reconsidered leverage (satisficing mode)

The strategic answer (Alexandria-live mode) was: **Frame is highest leverage** because of
multiplicative downstream effect.

The hack answer (today) is: **Frame is still highest leverage**, but for a different
reason — *because there's no Substrate to fall back on, what you don't decide at Frame
you'll re-decide ad hoc all day, badly*. Without Alexandria, every cognitive cycle that
isn't framed pays for the absence of substrate.

But for **acute pain relief this week**, the highest-yield single move is probably the
Comprehend hack — the manual agent table + SnapTool composite + git log discipline. That's
the "ten open windows" problem you named, and a 30-minute hack reduces it materially.

So:

- **Strategic priority:** invest in Frame discipline. Build a `today.md` template. Run it
  for a week.
- **Acute relief priority:** Comprehend hack. Build a 30-second cockpit ritual using the
  tools you have.
- **Daily anchor:** Ledger usage. The PoC works; just use it.
- **Stop signal:** Whole-Man pre-commit. Calendar block + Jess + the agent itself know
  when you stop.

These four together are the "make it through the day" minimum viable practice.

---

## What this changes about the book

The book has TWO present-tenses: the future-state world where the AI-native operating
system is live, and the satisficing world where it isn't. Both readers exist. The
research and the phase structure are stable across both, but the practice section of
each chapter probably needs both columns:

- "What this looks like with the substrate live" (the strategic version)
- "What you can do today, in the world that exists" (the hack version)

Most readers will live in the second column for years. Writing only the first column
risks the whole book reading like vaporware advice.

---

## Lab notes (live)

Date-stamped. The compounding lives in the file existing, not in the entries being
polished.

### 2026-04-30 — The morning gauge worked

Opened the capacity check-in PoC at the start of the day. Filled it out honestly and
landed on: **on empty.** Did not start the phase order. Did personal stuff and simple
errands instead, no AI until noon. Lunch with a friend. Late cup of coffee. Sat back down
and named the threshold out loud: **"okay, I'm ready."** Started the design session, and
it produced real work.

Three takeaways:

1. **Matching activity to capacity is real.** Forcing a full turn on empty reserves
   would have produced a damaged morning AND a damaged tomorrow. By honoring the gauge
   for half a day, the second half of the day became fully productive.
2. **The Ledger is a gate, not just a gauge.** Reading the capacity number was the
   *input* to the day's mode decision. This generalizes: the framework should treat
   capacity reading as a control signal upstream of every phase, not just as
   measurement after the fact.
3. **The "ready" signal has a recognizable feel.** Coffee landed, lunch did its
   detachment work, the sit-back-down ritual was real. Worth logging the specifics over
   time so the threshold becomes detectable earlier and earlier.

This is also lived proof of the controlling idea: *the team that rests strategically —
including from 9 to noon — outperforms.* The full evening session would not have existed
if the morning had been forced.
