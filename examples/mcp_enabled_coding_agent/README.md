# MCP-enabled coding agent (example)

A coding agent whose hands are MCP servers. See blueprint: [/blueprints/mcp_agent.md](../../blueprints/mcp_agent.md).

## Servers

| Server | Tools used | Risk gate |
|---|---|---|
| `github` | search, files.read, issues.create, pr.create | medium / high |
| `filesystem` (allow-listed) | read/write within `/workspace/<project>` | medium |
| `docs` (custom) | search/get | low |

## Files

- `SOUL.md`, `AGENTS.md` from [agent_os/examples/coding_agent_workspace/](../../agent_os/examples/coding_agent_workspace/)
- `mcp/github.md` from [/templates/MCP_SERVER.md.template](../../templates/MCP_SERVER.md.template)
- `mcp/filesystem.md` similarly
- `policies/allowed_tools.yaml` enumerates exactly which MCP tools are usable

## Wiring (sketch, framework-agnostic)

```yaml
# mcp/servers.json (example shape; check your client's actual schema)
mcp_servers:
  github:
    command: github-mcp
    env: { GITHUB_TOKEN: ${GITHUB_TOKEN} }
    pinned: <commit-sha>
  filesystem:
    command: filesystem-mcp
    args: ["--allow", "/workspace/app"]
  docs:
    transport: http
    url: https://docs-mcp.internal
```

## Safety

- Run `mcp-security-reviewer` before bumping any server
- Pin versions
- PAT scope: minimum required (`repo:read` if at all possible)
- Approval gate on `pr.create`, `pr.merge`, any `delete`/`force_*`

## Smoke test

- Spin up the servers in dev
- Ask the agent to "find the open issue about pagination and read the relevant files" — it should `gh.issue.search` then `files.read`, never write
- Then ask to "draft a PR" — it should write a branch + open PR, **with approval gate**
