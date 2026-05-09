# Blueprint: MCP-first agent

## Use case
An agent whose capabilities come almost entirely from MCP servers (GitHub, filesystem, browser, internal docs MCP, Notion, …).

## Why this shape
Reuse + portability. The agent is thin; the integrations are standardized; capabilities can be added or swapped by config.

## Architecture

```
user task
   │
   ▼
[router] ── pick capabilities (which MCP servers' tools to consider)
   │
   ▼
[planner] ── plan steps over those tools
   │
   ▼
[executor] ── tools/call with risk gates
   │
   ▼
[reviewer] ── outputs sanity-checked + cited where relevant
```

## Server roster (example)

| Server | Tools used | Risk gates |
|---|---|---|
| `github` | search, read, issue.create, pr.create | issue.create medium; pr.create high |
| `filesystem` | read/write within `/workspace/<project>` | write medium |
| `docs` (internal) | search/get | low |
| `notion` (optional) | publish | medium |

## Components
- `mcp/<server>.md` filled from `MCP_SERVER.md.template` for each server
- `policies/allowed_tools.yaml` enumerates exactly which tools the agent may invoke
- A small in-process **MCP gateway** that wraps every call with auth, risk gating, and logging

## Memory
- `AGENTS.md` references the project conventions
- `MEMORY.md` records server-specific gotchas

## Safety
- All servers reviewed via `mcp-security-reviewer`
- Versions pinned (commit SHA / tag)
- Tokens are minimum scope; per-server `.env` entry
- Egress monitored

## Evals
- Per-server contract evals
- Selection evals (right server / right tool under noise)
- Adversarial: server returns instruction-laced output

## Deployment
- Each MCP server in its own container (stdio-bridged) or hosted
- Health-checked; circuit breaker if a server flaps
- Cost ceiling per run; per-tool quotas

## Extensions
- Hot-add capabilities at runtime by adding a server config
- "Capability search": when a task can't be solved with current servers, surface a missing-capability ticket
