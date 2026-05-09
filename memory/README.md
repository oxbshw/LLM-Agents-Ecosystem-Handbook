# Memory

Memory is the layer that lets an agent **act consistently across runs**. It is *not* the chat history — chat history is ephemeral. Memory is what survives.

## What's here

- [memory_taxonomy.md](memory_taxonomy.md) — short-term, episodic, semantic, user, project
- [memory_distillation.md](memory_distillation.md) — turning runs into durable facts
- [episodic_memory.md](episodic_memory.md) — per-event records and how to use them
- [semantic_memory.md](semantic_memory.md) — distilled, generalized facts
- [user_memory.md](user_memory.md) — user profile, preferences, history
- [project_memory.md](project_memory.md) — project facts, decisions, conventions
- [memory_security.md](memory_security.md) — poisoning, leakage, retention
- [examples/](examples/) — concrete `MEMORY.md`, daily logs, decision logs

## The taxonomy in one diagram

```mermaid
flowchart LR
  IN[New session input] --> WM[Working memory<br/>(context window)]
  WM --> EP[Episodic<br/>logs/episodic/]
  EP -->|distilled by curator| SEM[Semantic<br/>memory/semantic/]
  SEM --> IDX[MEMORY.md<br/>index]
  IDX --> WM
  USR[User signals] --> UM[User memory<br/>USER.md]
  UM --> IDX
```

## Short-term vs long-term

| | Lives in | Lifespan | Trust |
|---|---|---|---|
| **Working** | Context window | One run | High (you wrote it) |
| **Episodic** | `logs/episodic/` | Days–weeks | Medium (raw events) |
| **Semantic** | `memory/semantic/` + `MEMORY.md` | Long-term | High (curated) |
| **User** | `USER.md`, `MEMORY.md#user` | Long-term | High (user-confirmed) |
| **Project** | `MEMORY.md#project` | Long-term | High (decisions/facts) |

## Distillation > accumulation

Raw transcripts are low-signal and expensive. Memory should be **distilled facts**, one line each, dated.

```
✅ - User prefers terse responses with diffs over prose (2026-04-15)
❌ - On 2026-04-15 user asked "can you stop being so verbose" and I said "sure"…
```

📖 [memory_distillation.md](memory_distillation.md)

## Conflicts and expiry

- **Conflict**: new evidence contradicts an existing entry → *update* the entry, move the old one to "Outdated"
- **Expiry**: review entries every {{6 months}}; re-date if still true, else move to Outdated
- **Demotion**: when confidence drops, demote semantic → open question rather than deleting

## Memory poisoning — what to fear

If memory can be written by sources the agent doesn't fully trust (web fetches, MCP tool output, RAG passages), an attacker can plant instructions that the agent later executes.

Mitigations:

1. **Promote, don't auto-write.** Episodic → semantic is a curator step, not automatic.
2. **Source-tag every entry.** Every memory line knows where it came from.
3. **Sanitize at boundaries.** Strip executable-style instructions from external content before storing.
4. **Eval.** Run memory recall + injection evals each release.

📖 [memory_security.md](memory_security.md)

## What does NOT belong in memory

- 🚫 Secrets, tokens, credentials
- 🚫 PII without a documented retention policy
- 🚫 Full chat transcripts (those go to `logs/`)
- 🚫 Anything derivable from `git log` or current code
- 🚫 Vague impressions or judgments
