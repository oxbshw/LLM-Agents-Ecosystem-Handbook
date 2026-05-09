# MCP — Model Context Protocol

The Model Context Protocol is an open standard for connecting agents to external tools, resources, and prompts. One server, many clients. Build it once, use it everywhere.

## What's here

- [mcp_basics.md](mcp_basics.md) — what MCP is and what it gives you
- [mcp_architecture.md](mcp_architecture.md) — clients, servers, transports
- [mcp_server_catalog.md](mcp_server_catalog.md) — useful servers we've vetted
- [mcp_security.md](mcp_security.md) — the threat model and mitigations
- [mcp_approval_flows.md](mcp_approval_flows.md) — gating risky tools
- [mcp_vs_function_calling.md](mcp_vs_function_calling.md) — when to use each
- [examples/](examples/) — agent skeletons that wire up real MCP servers

## In one paragraph

A function-calling integration is private to one app. An **MCP server** packages the same capabilities behind a standard schema, transports (stdio / SSE / HTTP), and a discovery mechanism, so any compliant client (Claude Code, Cursor, OpenAI Agents SDK, etc.) can use it. That's the entire pitch.

## When to use MCP

| Use MCP when… | Use plain function calling when… |
|---|---|
| The integration is reused across agents/tools | One agent, one app |
| You want the integration outside your repo | The integration is throwaway |
| External users (or contributors) want to wire it themselves | Internal-only, tightly coupled |
| There's already a good server (GitHub, filesystem, browser, …) | The function is one line |

## Local vs remote

| | Local (stdio) | Remote (SSE / HTTP) |
|---|---|---|
| Latency | Lowest | Network-bound |
| Auth | Local user identity | Real auth flow needed |
| Risk | Server runs in your process tree | External party can see your queries |
| Best for | Filesystem, local tools, dev | Hosted services, multi-user |

## Security: read [mcp_security.md](mcp_security.md) before connecting anything

Short version:
- Treat all MCP **output** as untrusted (potential prompt injection)
- Treat all MCP **tool descriptions** as untrusted too
- Pin versions; review source for new servers
- Apply least privilege; gate high-risk tools behind approvals
- Log every call

## Example agents in this repo

- [agents/github_mcp_agent](../agents/github_mcp_agent/) — GitHub via MCP
- [agents/notion_mcp_agent](../agents/notion_mcp_agent/) — Notion via MCP
- [agents/browser_mcp_agent](../agents/browser_mcp_agent/) — browser automation
- [agents/travel_planner_mcp_agent_team](../agents/travel_planner_mcp_agent_team/) — multi-agent over MCP
