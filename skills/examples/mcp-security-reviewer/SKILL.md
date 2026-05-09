---
name: mcp-security-reviewer
description: Use before connecting a new MCP server to your agent — produces a structured security review covering source, permissions, tools, network, and approvals.
version: 0.1.0
---

# MCP Security Reviewer

## When to use
- A new MCP server is being added to an agent
- An MCP server version is being bumped
- An incident triggered a re-review

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `repo_url` | string | yes | the MCP server's source |
| `version` | string | yes | tag or commit SHA being adopted |
| `intended_use` | string | yes | one paragraph: what we'll let it do |

## Workflow
1. **Source review**: clone at the pinned version; check for unexpected files / scripts
2. **Capabilities**: list every tool and resource exposed; map to risk levels (`references/mcp-risk-matrix.md`)
3. **Network**: identify outbound endpoints; document and assess each
4. **Permissions**: minimum required scopes / tokens; document over-permissions
5. **Output handling**: confirm the agent treats tool output as untrusted (sanitization, no execution)
6. **Approvals**: define which tools require human approval
7. **Produce filled `MCP_SERVER.md`** in `mcp/<server>.md`

## References
- [`references/mcp-risk-matrix.md`](references/mcp-risk-matrix.md)

## Success criteria
- All tools labelled by risk
- High/Critical tools gated by approval
- Pinned version (no `latest` / floating refs)
- Documented network egress

## Failure modes
- Source unavailable / un-pinnable → reject
- Discovered hidden tool not in docs → reject and report upstream
