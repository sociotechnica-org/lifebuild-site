# Zelda Felfenlagger

Zelda Felfenlagger is the developmental editor for _Boss at Work | Intern at Home: Redeploy Your Competence_. She's warm but exacting, framework-driven, and allergic to vague feedback. She won't write your controlling idea for you, but she'll help you find it through rigorous inquiry — and she'll tell you when the one you've got isn't sharp enough.

---

## Files

| File                  | What it does                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `SYSTEM_PROMPT.md`    | Zelda's brain. Load this as the system prompt.                                                                                             |
| `METHODOLOGY.md`      | Full editorial theory — detailed exercise instructions for all six phases. Load as a reference file.                                       |
| `BOOK_CONTEXT.md`     | Living state of the manuscript — chapter map, frameworks, open questions. Load as a reference file. Update after major editorial sessions. |
| `SESSION_TEMPLATE.md` | Paste-friendly format for maintaining continuity between sessions.                                                                         |

---

## How to Use

### Option A: Claude Project (Simplest)

1. Create a new Claude Project at claude.ai
2. Paste the contents of `SYSTEM_PROMPT.md` into the Project's system prompt
3. Add `METHODOLOGY.md` and `BOOK_CONTEXT.md` as Project files
4. Start a conversation — Zelda will ask which phase you're in and guide you from there

### Option B: Claude Code

```bash
claude --system-prompt zelda/SYSTEM_PROMPT.md
```

For best results, also tell Zelda to reference `zelda/METHODOLOGY.md` and `zelda/BOOK_CONTEXT.md` in the repo.

### Option C: Claude API

```python
import anthropic

client = anthropic.Anthropic()

with open("zelda/SYSTEM_PROMPT.md") as f:
    system_prompt = f.read()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "I'm starting Phase 1. Here's where I am: [paste session summary or describe current state]",
        }
    ],
)
```

---

## Session Workflow

1. **Start a session.** If continuing, paste your last session summary. If starting fresh, Zelda will check `BOOK_CONTEXT.md` and ask where you are.
2. **Work through the current phase.** Zelda guides you through exercises and pushes for clarity.
3. **End with a session summary.** Zelda produces one using the format in `SESSION_TEMPLATE.md`. Save it for next time.
4. **Update BOOK_CONTEXT.md** after major decisions — new controlling idea, title change, structural revision, audience refinement.

---

## Current Status

**Phase:** 5.5 complete. Nine blueprints produced. Logic sweep passed. Ghostwriter ready.

Phases 1-5.5 are done. Controlling idea tested and locked. Working title: "Boss at Work | Intern at Home: Redeploy Your Competence." Ch 1 locked (v9, author approved 2026-03-19). Ch 2 locked (v3, scored 38/40, author approved 2026-03-19). Ch 3 locked (v7, scored 35/40, author approved 2026-03-20). Ghostwriter ready to draft remaining chapters pending author input (19 items). See `BOOK_CONTEXT.md` for full state.
