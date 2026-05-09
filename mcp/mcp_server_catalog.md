# MCP server catalog

A starter list of widely useful MCP servers. **Verify each against current upstream docs before adopting** — the ecosystem moves fast.

> ⚠️ Inclusion ≠ endorsement of security posture. Always run [`mcp-security-reviewer`](../skills/examples/mcp-security-reviewer/SKILL.md) before connecting a new server.

## Code & repos

| Server | What it exposes | Risk | Notes |
|---|---|---|---|
| `github` | repos, issues, PRs, files, search | Medium–High | Scope PAT carefully (`repo:read` vs `repo`) |
| `gitlab` | similar to github | Medium–High | Same scoping advice |
| `git` | local git operations | Medium | Read-only mode is much safer |

## Local environment

| Server | What it exposes | Risk | Notes |
|---|---|---|---|
| `filesystem` | read/write within allow-listed roots | Medium–High | Allow-list is critical; never grant `/` |
| `shell` (varies) | run commands | Critical | Almost always wants approval gates |
| `sqlite` / `postgres` | query (and sometimes write) | Medium–High | Read-only DSN strongly preferred |

## Web & data

| Server | What it exposes | Risk | Notes |
|---|---|---|---|
| `fetch` | HTTP GET of arbitrary URLs | Medium | Treat output as untrusted |
| `playwright` / `browser` | drive a real browser | High | Big attack surface; sandbox |
| `tavily` / `serpapi` | web search | Low–Medium | Mostly read-only |

## Productivity

| Server | What it exposes | Risk | Notes |
|---|---|---|---|
| `notion` | pages, databases | Medium | Workspace scoping matters |
| `slack` | channels, DMs, posts | Medium–High | Posting is high risk |
| `gmail` / `email` | read + send | High | Send must be gated |
| `gcal` / `calendar` | read + write events | Medium | Decline auto-creates |

## Knowledge / RAG

| Server | What it exposes | Risk | Notes |
|---|---|---|---|
| `docs` (custom) | curated doc index | Low | Build your own for internal docs |
| `chroma` / `pgvector` | vector store | Low–Medium | Sanitize queries |

## How to add to this catalog

PR welcome. Each entry must include:

- Name + canonical source URL
- Capabilities (tool list)
- Risk assessment (with reasoning)
- Notes on scoping / least-privilege
- Whether you've actually used it in production
