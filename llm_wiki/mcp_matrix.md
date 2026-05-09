# MCP matrix

Quick view of common MCP servers and their risk profile. **Verify against current upstream docs.**

| Server | Capability | Risk | Notes |
|---|---|---|---|
| `github` | repos, issues, PRs, files | Medium–High | PAT scope critical |
| `gitlab` | repos, issues, MRs | Medium–High | Same scoping advice |
| `git` | local git ops | Medium | Read-only mode safer |
| `filesystem` | FS read/write | Medium–High | Allow-list roots |
| `shell` (varies) | run commands | Critical | Always gate |
| `sqlite` / `postgres` | DB query / write | Medium–High | Read-only DSN preferred |
| `fetch` | HTTP GET | Medium | Untrusted output |
| `playwright` / `browser` | drive a browser | High | Sandbox |
| `tavily` / `serpapi` | web search | Low–Medium | Read-only |
| `notion` | pages, DBs | Medium | Workspace scope matters |
| `slack` | channels, posts | Medium–High | Posting risky |
| `gmail` / `email` | read + send | High | Send must be gated |
| `gcal` / `calendar` | events | Medium | Auto-create risky |
| `chroma` / `pgvector` | vector store | Low–Medium | Sanitize queries |

## Pre-connection workflow

1. Run [`mcp-security-reviewer`](../skills/examples/mcp-security-reviewer/SKILL.md)
2. Pin version
3. Configure least-privilege scopes
4. Walk [checklists/mcp_security_checklist.md](../checklists/mcp_security_checklist.md)
5. Wire approval gates per [tool risk levels](../safety/tool_risk_levels.md)
6. Add to [evals/mcp_evals.md](../evals/mcp_evals.md)

## Local vs remote

| | Local (stdio) | Remote (HTTP/SSE) |
|---|---|---|
| Latency | low | network |
| Auth | local user | needs real auth |
| Sensitive data | safer (process-local) | careful — server sees context |
| Multi-user | one-per-process | natural |
