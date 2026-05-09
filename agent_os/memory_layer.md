# Memory Layer

Memory is **durable state that survives the run**. It is not chat history — chat history is ephemeral; memory is distilled.

## What goes where

| Type | Lives in | Lifespan | Example |
|---|---|---|---|
| **Working** | Context window | One run | Current task, immediate scratchpad |
| **Episodic** | `logs/episodic/` or DB | Days–weeks | "On 2026-04-12 we tried X, it failed because Y" |
| **Semantic** | `memory/semantic/*.md` | Long-term | "The auth service is owned by team Iris" |
| **User** | `MEMORY.md` (user-scoped) | Long-term | "User prefers terse responses" |
| **Project** | `MEMORY.md` (project-scoped) | Long-term | "Merge freezes start every Thursday at 5pm" |

## Distillation > accumulation

The most common memory mistake: appending raw turns. The result is a dense, low-signal blob that costs tokens and confuses the model.

**Distill.** After a session, write the *learnings* — not the *transcript* — into the appropriate file. A good memory entry is:

- **One fact per entry**
- **Dated** (so you can expire it)
- **Sourced** (why do we believe this?)
- **Categorized** (`#user`, `#project`, `#decision`, `#feedback`)

See [memory/memory_distillation.md](../memory/memory_distillation.md) for a full protocol.

## What to never store

- 🚫 Secrets, tokens, credentials
- 🚫 PII unless you have a clear retention policy
- 🚫 Information from prompt-injectable sources without sanitization
- 🚫 Vague impressions ("user seemed annoyed") — judgments age badly
- 🚫 Things derivable from `git log` or the codebase

## Memory poisoning

If your agent reads memory written by past *agent runs*, an attacker who can inject content via tools (web fetches, MCP, RAG) can plant malicious "memories." Mitigations:

- Sanitize and review before promoting episodic → semantic memory
- Tag the *source* of every memory entry
- Have an explicit *promotion* step (memory curator skill or human review)
- Periodically run a [memory eval](../evals/memory_evals.md)

See [memory/memory_security.md](../memory/memory_security.md).
