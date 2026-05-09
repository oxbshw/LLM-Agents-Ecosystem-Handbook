# Memory matrix

Pick by *read pattern* and *write pattern*.

| Need | Default choice | Notes |
|---|---|---|
| Per-project conventions, decisions | `MEMORY.md` (file) | Index-style, in git |
| Per-topic deep memory | `memory/semantic/<topic>.md` | One file per topic |
| Per-user profile + prefs | `USER.md` + per-user store | Strict isolation |
| Per-event raw record | `logs/episodic/` | Append-only |
| Decision records | `memory/decisions/` ADRs | Long-lived |
| Semantic search over many chunks | Vector store (Chroma / pgvector / Weaviate / LanceDB) | Add reranker |
| Structured / time-bound | SQL / KV (Postgres / Redis) | When fields matter |
| Long-running agent state | Framework checkpointer (LangGraph) | Survives restarts |
| Multi-user, hosted | Mem0 / Letta / cloud memory APIs | Verify privacy |

## Read patterns

| Pattern | Best store |
|---|---|
| Exact recall by key | KV / SQL / file |
| Semantic similarity | Vector store + reranker |
| Time-range queries | SQL with index on time |
| Top-K relevant facts | Hybrid (BM25 + vector) |

## Write patterns

| Pattern | Best store |
|---|---|
| Rare curated writes | Files in git |
| Frequent updates | DB (SQL / KV) |
| Append-only events | Log files / event store |

## Hard rules

- 🚫 Never store secrets / tokens
- 🚫 Don't mix tenants without isolation
- ✅ Always source-tag external content
- ✅ Always date entries
