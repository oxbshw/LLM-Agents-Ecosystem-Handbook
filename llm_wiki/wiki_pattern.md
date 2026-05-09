# The personal-wiki pattern for agents

A self-maintaining knowledge base built from the user's own documents — the pattern behind tools like Karpathy's "wiki of you," `llm_wiki`, and the broader trend of personal RAG. This is **not** an implementation guide for any specific tool; it's a description of the pattern so you can apply it in whatever stack you use.

## The pattern in three sentences

1. Ingest documents (notes, PDFs, web clips) and let an LLM extract structured *atoms* (facts, decisions, references, tasks).
2. Cluster those atoms into *topics* using semantic similarity + graph community detection.
3. Render each topic as a wiki page that links to its source atoms, regenerates when sources change, and supports human edits that win on conflict.

## Why agents care

Agents need durable knowledge that's:

- **Curated** (signal, not transcripts)
- **Source-tracked** (every fact knows where it came from)
- **Topic-organized** (not a flat dump)
- **Refresh-aware** (regenerates when inputs change)
- **Human-correctable** (edits don't get blown away)

Personal wikis hit all five.

## Architecture

```
[ingest queue]                    [topic graph]            [wiki pages]
docs / notes / clippings  ─►  atoms ─► clustering ─►  pages with atom citations
                                ▲                              │
                              edits ◄──── human override ◄────┘
```

## Key building blocks

| Block | Notes |
|---|---|
| **Ingest pipeline** | Persistent queue, idempotent re-ingest, content-addressed storage |
| **Atom extraction** | LLM extracts facts/decisions/refs as small structured items |
| **Embedding + clustering** | Cosine over an embedding model + a community-detection algorithm (Louvain, Leiden) |
| **Page rendering** | Each topic = one Markdown page; atoms cited inline |
| **Edit reconciliation** | Human edits stored as overrides; auto-regen merges, doesn't overwrite |
| **Source linking** | Page → atom → source doc; one-click drill-down |

## Why this is hard to do well

- **Atom granularity.** Too small → wiki pages full of trivia. Too big → no genuine clustering signal.
- **Cluster stability.** Without anchoring, a single new doc can re-shuffle the whole graph.
- **Source freshness.** Source docs can be deleted, edited, or replaced; the wiki must follow without losing human edits.
- **Multi-tenant.** A team wiki has access controls per source — must enforce at retrieval, not display.

## How agents use a personal wiki

- **Read** — wiki is a curated retrieval surface (better than raw doc RAG)
- **Cite** — every claim in an agent output points to a wiki atom, which points to the source
- **Update** — agent can propose new atoms; promotion is gated like any [memory promotion](../memory/memory_distillation.md)
- **Diff** — over time, a wiki *diff* across weeks tells you "what's new in domain X"

## When to build one

- You have ≥ ~500 documents to navigate
- You re-ingest sources on a real cadence
- You want agents to ground answers in *your* corpus, not the open web
- You can afford to maintain it (it does need maintenance)

## When NOT to build one

- The corpus is small enough for raw RAG
- Documents are short-lived (the wiki goes stale before it's useful)
- You don't have a way to gate / version source access

## Prior art and inspirations

The pattern shows up across several projects in the ecosystem (open-source desktop apps, hosted personal-KB tools, internal corporate-wiki revamps powered by LLMs). They differ in storage, UI, and graph algorithms — but share the *atoms → cluster → page → reconcile* shape.

## Pairing with this handbook

- The wiki is part of the [memory layer](../memory/) — it's a *backend* for semantic memory
- Pages can be MCP resources for agents — see [mcp/examples/docs_mcp_agent](../mcp/examples/docs_mcp_agent/)
- Wiki edit history feeds the [agent-memory-curator skill](../skills/examples/agent-memory-curator/SKILL.md)
- Ground LLM-readable docs in the wiki via [docs/llm_readable_docs.md](../docs/llm_readable_docs.md)
