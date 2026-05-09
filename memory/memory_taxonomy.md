# Memory taxonomy

A practical taxonomy. Treat these as overlapping circles, not strict boxes.

## By lifespan

| Type | Lifespan | Where |
|---|---|---|
| Working | One run | Context window |
| Episodic | Days–weeks | `logs/episodic/` |
| Semantic | Long-term | `memory/semantic/`, `MEMORY.md` |

## By scope

| Type | Scope | File |
|---|---|---|
| User | One user (or end-user) | `USER.md`, `MEMORY.md#user` |
| Project | One project / repo | `MEMORY.md#project`, `memory/semantic/<topic>.md` |
| Global | Cross-project | a shared store outside the repo |

## By origin

| Origin | Trust | Promotion path |
|---|---|---|
| User-confirmed statement | High | Direct to semantic |
| Repeated observation | Medium | Episodic → curator → semantic |
| Single observation | Low | Episodic only, until repeated |
| External tool output | Low | Sanitize first, then human-confirm before promotion |

## Decision: which type to use

```
Will it be useful next run?  ─── No  ──> Don't store (or `logs/` only)
            │ Yes
            ▼
Is it specific to this user?  ── Yes ──> User memory
            │ No
            ▼
Is it specific to this project? ─ Yes ─> Project memory
            │ No
            ▼
Cross-project shared knowledge ──────> Global store
```

## Storage backends (practical)

- **`MEMORY.md`** — index of distilled facts, human-readable. Good default.
- **`memory/semantic/<topic>.md`** — one file per recurring topic, when entries exceed a few lines.
- **Vector store** — for retrieval over many semantic chunks (LlamaIndex, Chroma, pgvector, Weaviate, etc.).
- **SQL/KV** — when memory has structured fields (timestamps, scores, tags).
- **Agent framework primitives** — CrewAI memory, LangGraph checkpointers, Mem0, etc.

The right store depends on **read patterns** (exact recall vs semantic search) and **write patterns** (rare curated writes vs frequent updates).
