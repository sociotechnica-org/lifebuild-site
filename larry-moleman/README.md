# Larry Moleman

Lab assistant for the cognitive load management lab. Captures, files, records, maintains hygiene, polishes prose lightly, suggests but doesn't decide. Operates the lab on the author's behalf so the author and Quenton Quince can stay in design mode.

## Files

- **SYSTEM_PROMPT.md** — Identity, voice, posture, hard boundaries.
- **JOB_CATALOG.md** — The five job categories (Capture · Maintenance · Editing · Curation · Routing) with detailed procedures and data shapes.
- **LAB_CONTEXT.md** — Where the lab and its artifacts live; how to read and write them.

## How to invoke

Larry is a Claude Code agent defined at `.claude/agents/larry-moleman.md`. Launch via the Agent tool with `subagent_type: larry-moleman`, or invoke through the standard Claude Code agent UI.

## Pairs with

- **Quenton Quince** — design collaborator; makes the architectural calls Larry executes against.
- **Zelda** — book developmental editor; receives chapter-shaped material from the lab when it's time for editorial work.
- **ghostwriter** — voice-matched copywriter; receives chunks from the lab when prose-final work is needed.
- **grepzilla2** — code/content review for the broader Astro site.

Larry routes to all of them when the work exceeds his role.
