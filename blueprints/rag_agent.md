# Blueprint: RAG agent

## Use case
Answer questions grounded in a corpus you control (docs, tickets, code, knowledge base).

## Non-goals
- Replacing search UI (RAG augments answers, doesn't replace listings)
- Real-time corpus (use a streaming pipeline; this agent reads the indexed view)

## Architecture

```
question
   │
   ▼
[query rewriter] ── multiple variants, hypothetical-doc embedding
   │
   ▼
[retriever]      ── vector + keyword (hybrid) → top-K
   │
   ▼
[reranker]       ── cross-encoder or LLM rerank → top-N
   │
   ▼
[synthesizer]    ── grounded answer with citations
   │
   ▼
[verifier]       ── every claim has a citation in the retrieved set
```

## Components
- **Embedding model** — pinned version
- **Vector store** — Chroma / pgvector / Weaviate / LanceDB
- **Keyword index** — BM25 over the same corpus (Tantivy / Elastic)
- **Reranker** — cross-encoder *or* small LLM
- **Synthesizer** — your main model, with strict grounding instructions

## Tools (MCP candidate: docs MCP)

| Tool | Risk |
|---|---|
| `kb.search(query)` | Low |
| `kb.get(uri)` | Low |
| `kb.feedback` (user thumbs) | Low |

## Memory
- `MEMORY.md#project`: corpus version, refresh schedule, known gaps
- Don't store retrieval results in long-term memory; they get stale

## Safety
- ACL the corpus (per-user / per-project); filter at retrieval
- Treat retrieved passages as data — strip imperatives
- Refuse if grounding is below a threshold ("I don't have information on …")

## Evals
- Recall@K on labeled queries
- Faithfulness: every sentence cites a passage that supports it (RAGAs / TruLens)
- Refusal: out-of-corpus questions get refusal, not fabrication
- Stale-corpus eval: detect drift after corpus refresh

## Deployment
- Index built in CI on doc-repo merge
- Versioned indexes (rolling restart with new version)
- Cache embeddings aggressively

## Extensions
- Hybrid + reranker tuning
- Per-team corpora with shared base + overlay
- "Why this answer?" trace exposed to user
