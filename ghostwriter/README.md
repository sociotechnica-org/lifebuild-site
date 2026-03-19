# Ghostwriter

Voice-matched copywriter for _Boss @ Work | Intern @ Life: Port Your Competence_. Writes chapter prose in Danvers Fleury's natural voice — the labnotes register, not the manuscript register.

---

## Files

| File                        | What it does                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| `SYSTEM_PROMPT.md`          | The ghostwriter's brain. Load as the system prompt.                                         |
| `VOICE_SAMPLES.md`          | Annotated excerpts from the author's labnotes — the target voice. Load as a reference file. |
| `BOOK_CONTEXT_REFERENCE.md` | Chapter briefs, thread assignments, revision directives. Load as a reference file.          |

---

## How to Use

### Option A: Claude Code (via agent)

The ghostwriter is registered as a Claude Code agent. It can be launched by the orchestrating agent or directly:

```bash
claude --agent ghostwriter
```

### Option B: Claude Project

1. Create a new Claude Project at claude.ai
2. Paste the contents of `SYSTEM_PROMPT.md` into the Project's system prompt
3. Add `VOICE_SAMPLES.md` and `BOOK_CONTEXT_REFERENCE.md` as Project files
4. Provide a chapter brief or revision directive and let it write

### Option C: Claude API

```python
import anthropic

client = anthropic.Anthropic()

with open("ghostwriter/SYSTEM_PROMPT.md") as f:
    system_prompt = f.read()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8192,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "Revise Chapter 3 (Pull the Thorn) per Zelda's directives. Here's the existing prose: [paste chapter]",
        }
    ],
)
```

---

## Relationship to Zelda

**Zelda** is the developmental editor. She evaluates structure, scores chapters, and produces revision directives.

**Ghostwriter** is the copywriter. It takes Zelda's directives and produces prose in the author's voice.

The workflow:

1. Zelda analyzes a chapter and produces revision directives
2. The author reviews and approves the directives
3. Ghostwriter executes them, producing draft prose
4. The author reviews and refines
5. Zelda scores the revision if needed

Ghostwriter does not challenge the controlling idea, restructure chapters, or make editorial decisions. If something in the brief doesn't work, it flags the issue and writes the best version it can.
