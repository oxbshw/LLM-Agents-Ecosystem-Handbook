# GitHub MCP agent (skeleton)

A documentation-first skeleton showing how to wire a coding agent to the official GitHub MCP server.

## What it does
- Lists repos, issues, PRs
- Reads file contents
- Opens PRs and issues (gated by approval)

## Files
- `AGENTS.md` — repo conventions
- `TOOLS.md` — labels every GitHub MCP tool by risk level
- `mcp/github.md` — server config + security review (use [`MCP_SERVER.md.template`](../../../templates/MCP_SERVER.md.template))

## Setup (sketch)

1. Install GitHub MCP server (see upstream docs for current install path)
2. Mint a PAT with the **minimum** scope you need (`repo:read` for read-only)
3. Place the PAT in `.env` as `GITHUB_TOKEN`
4. Configure your client (Claude Code, Cursor, OpenAI Agents SDK, …) to launch the server with the PAT in env

## Risk-tiered tool table

| Tool | Risk | Approval |
|---|---|---|
| `repos.search`, `repos.get`, `issues.list` | Low | none |
| `files.read` | Low | none |
| `issues.create`, `issues.comment` | Medium | first-time |
| `pull_request.create` | High | required |
| `pull_request.merge` | High | required |
| `repo.delete`, `branch.force_push` | Critical | always + 2nd reviewer |

## Before connecting
Run [`mcp-security-reviewer`](../../../skills/examples/mcp-security-reviewer/SKILL.md). Pin the server version. Restrict the PAT scope.
