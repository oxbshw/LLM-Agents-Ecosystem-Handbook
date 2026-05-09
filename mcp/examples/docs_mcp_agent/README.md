# Docs MCP agent (skeleton)

A small custom MCP server that exposes your team's curated docs as resources + a search tool. The pattern most teams under-build.

## Why
Loading "all our docs" via RAG is noisy and stale. A curated docs MCP gives the model:

- Up-to-date docs (you control freshness)
- A query interface (`docs.search`)
- Resource URIs the agent can pull (`docs://onboarding`, `docs://playbooks/incident`)

## Capabilities

| Tool | Purpose | Risk |
|---|---|---|
| `docs.search(query)` | top-K relevant snippets | Low |
| `docs.get(uri)` | fetch a full doc | Low |

| Resource | Notes |
|---|---|
| `docs://<slug>` | one resource per published doc |
| `docs://index` | enumerable list |

## Build sketch (Python, ~50 lines)

1. Index docs into a small vector store (Chroma or even SQLite + BM25)
2. Implement `docs.search(query)` over the index
3. Wrap with the Python MCP SDK (`mcp` package)
4. Run via stdio for local use, or HTTP for team use

## Why this is high-leverage

- Replaces three patterns at once: doc RAG, internal Q&A bot, "where is X documented?"
- Easy to keep fresh (rebuild on doc-repo CI)
- Reusable across every agent the team builds
