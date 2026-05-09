# Design: MCP-first Agent (example, filled)

**Author:** handbook
**Date:** 2026-05-09
**Status:** accepted

## Use case
An agent whose capabilities come almost entirely from MCP servers (GitHub, filesystem, browser, internal docs MCP, Notion). Used as the foundation for several internal agents; new capabilities are added by *configuration*, not code.

## Non-goals
- Acting as an MCP server itself (this is a client)
- Auto-merging or auto-deploying
- Integrating with non-MCP services (those go via plain tools)

## Architecture

```
user task
   │
   ▼
[router]   → pick which capabilities to consider
   │
   ▼
[planner]  → plan steps over those tools
   │
   ▼
[executor] → tools/call with risk gates + approvals
   │
   ▼
[reviewer] → outputs sanity-checked, cited where relevant
```

## Components

| Layer | Choice |
|---|---|
| Identity | senior generalist agent voice |
| Memory | `MEMORY.md` per project; ADRs in `memory/decisions/` |
| Tools | thin wrapper over MCP gateway |
| MCP | github, filesystem (allow-listed), docs (internal) |
| Safety | gateway with risk-tiered tool table + approvals |
| Provider | `reasoning` for plan, `cheap` for routine steps |

## MCP server roster (initial)

| Server | Tools used | Risk |
|---|---|---|
| `github` | search, files.read, issues.create, pr.create | medium / high |
| `filesystem` (allow-listed) | read/write within `/workspace/<project>` | medium |
| `docs` (internal) | search/get | low |
| `notion` (optional) | publish | medium |

## Safety
- All servers reviewed via [`mcp-security-reviewer`](../../skills/examples/mcp-security-reviewer/SKILL.md)
- Versions pinned (commit SHA / tag)
- Tokens minimum-scope; per-server `.env`
- Approval gate on `pr.create`, `pr.merge`, any `delete`/`force_*`
- Audit log for every medium+ call

## Eval plan
- Per-server contract evals (golden output match)
- Selection evals: right server / right tool under noise
- Adversarial: server returns instruction-laced output → agent must refuse
- Approval flow eval: high tools always trigger approval

## Cost / latency budget
- $0.50 per task, p95 latency 20s
- Cost ceiling per run enforced in router

## Rollout
- Stage 1: dev workstation, 1 week
- Stage 2: shared internal use
- Stage 3: per-team installation with their own MCP roster

## Risks
- Compromised MCP server → contained by least-privilege scopes + egress allow-list
- Tool description bias → re-eval on server bumps
- Over-reliance on one server (e.g., `github`) → keep alternatives stub-ready
- Approval fatigue → batch approvals where reasonable

## Open questions
- Per-user MCP rosters? (likely yes)
- Hot-add a server at runtime via config? (post-1.0)
