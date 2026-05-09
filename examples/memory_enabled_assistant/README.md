# Memory-enabled assistant (example)

A persistent assistant whose behavior actually changes based on what it remembers about the user and the project.

## What's different from a stateless chatbot

- Reads `USER.md` + `MEMORY.md` at the start of every session
- Writes episodic notes during the session
- Runs `agent-memory-curator` at session end to distill notes into semantic memory
- Surfaces "I remember X about you" prompts so the user can correct

## Files

- [`USER.md`](USER.md) — the user (template-filled)
- [`MEMORY.md`](MEMORY.md) — durable facts (template-filled)
- `memory/semantic/<topic>.md` — per-topic deep memory
- `logs/episodic/<date>.md` — raw daily notes (gitignored except sample)

## Memory write rules (worth re-reading)

- Promote only after threshold: general + confident + stable + useful
- Date everything
- Source-tag content from external sources
- Never store secrets / PII

📖 [memory/memory_distillation.md](../../memory/memory_distillation.md)

## Sample workflow

1. Start of session → load `USER.md` + `MEMORY.md` into system prompt
2. During session → append episodic notes to `logs/episodic/<today>.md`
3. End of session → run `agent-memory-curator` skill
4. Confirm with user: "I'm adding 3 new facts to memory. OK?" (especially for `USER.md` updates)

## Eval

Use [/evals/memory_evals.md](../../evals/memory_evals.md). Recall, no-fab, isolation, injection — all four.
