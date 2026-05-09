# System prompt design

The system prompt is the constitution. Short, dense, dated.

## Goals

1. **Identity stable across runs** (voice, refusal style, quality bar)
2. **Behavior predictable across users** (no persona drift)
3. **Composable with per-session context** (user message + tools)
4. **Cheap to load** (it ships every request)

## Anatomy

| Block | Purpose | Approx length |
|---|---|---|
| Role + mission | Identity | 2–3 lines |
| Values | Conflict resolution | 4–6 lines |
| Output contract | Format + success | 5–10 lines |
| Tool discipline | When/how to call tools | 5–10 lines |
| Refusal style | Consistent decline shape | 3–5 lines |
| Loop discipline | Max steps, repeat detection | 3–5 lines |
| Memory hooks | What facts to trust | varies |

Total target: under 1,500 tokens. Above that, you're paying for hot air.

## When to put something in the system prompt

| If… | Goes in… |
|---|---|
| Always true regardless of session | system prompt |
| Per-user / per-session preference | user message / `USER.md` payload |
| Per-task hint | per-call user message |
| Reusable workflow | a Skill, not the system prompt |
| External data | a tool / RAG, not the system prompt |

A *small* system prompt + Skills + memory beats a *large* system prompt every time.

## Common mistakes

- ❌ Pasting the entire style guide into the system prompt. Put it in `references/` of a Skill.
- ❌ Hard-coding model names. Models change; identity shouldn't.
- ❌ Listing every tool with its full schema. The harness already does that.
- ❌ "You will be tipped $1000" / "you will be unplugged" tricks. They don't work in 2026 evals; they pollute the prompt.
- ❌ Anti-instructions stacked deep. ("Don't do X. Don't do Y. Don't do Z.") Replace with positive guidance + a refusal scaffold.

## Versioning

System prompts are dependencies. Treat them like one:

- File-versioned (`SOUL.md` in repo)
- Bump on substantive change
- Re-run regression eval on bump
- Keep a one-version rollback

## Dating context

Add a single line near the top:

```
Today's date is 2026-XX-XX.
```

This anchors "today" / "tomorrow" / "this week" — small change, big quality lift on time-sensitive tasks.

## Adapt to the model family

Different model families respond to different cues. A prompt that excels on one provider may underperform on another. **Eval, don't assume.** When you swap providers, re-run [evals/regression_evals.md](../evals/regression_evals.md) and adjust the prompt.

## Cross-references

- [`templates/SYSTEM_PROMPT.md.template`](../templates/SYSTEM_PROMPT.md.template)
- [`agent_os/agent_identity.md`](../agent_os/agent_identity.md) — `SOUL.md` is the file form of the system prompt
- [`prompt_eval_methods.md`](prompt_eval_methods.md) — measuring changes
