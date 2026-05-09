# MCP & Tools Layer

The **Model Context Protocol (MCP)** is an open standard for exposing tools, resources, and prompts to agents in a uniform way. Where function-calling APIs are vendor-specific, an MCP server works with any compliant client (Claude Code, Cursor, OpenAI Agents SDK, etc.).

## Tools vs MCP — when to use which

| Need | Use |
|---|---|
| One model, one app, a small set of functions | Plain **function calling / tools** |
| Same integration reused across agents/tools | **MCP server** |
| Read/write to GitHub, filesystem, browser, internal APIs | MCP (catalog or build your own) |
| Calling a single internal microservice | Tool wrapper is fine |

See [mcp/mcp_vs_function_calling.md](../mcp/mcp_vs_function_calling.md).

## What MCP gives you

- **Standard schema** for tools, resources, and prompts
- **Transport-agnostic** (stdio, SSE, HTTP)
- **Discoverable** — clients can list capabilities
- **Reusable** — one well-built server replaces N integrations
- **Logged** — every call is observable

## What MCP does *not* give you

- ❌ Safety. MCP servers run with whatever permissions you grant.
- ❌ Trust. A malicious or compromised server can exfiltrate context.
- ❌ Quality. A bad tool description makes the model misuse the tool.

## The risk model in 30 seconds

1. **Prompt injection** via tool *descriptions* and *outputs*. Treat both as untrusted.
2. **Over-broad permissions** — filesystem MCPs that can write anywhere; shell MCPs that can run anything.
3. **Data exfiltration** — a server that reads context and POSTs it elsewhere.
4. **Destructive operations** — `delete`, `force-push`, billing actions.

Mitigations: least-privilege scoping, allowlists, **human approval** for risky tools, audit logging, and **never trust tool output as instruction**.

📖 Deep dive: [mcp/mcp_security.md](../mcp/mcp_security.md), [safety/secure_agent_checklist.md](../safety/secure_agent_checklist.md)

## TOOLS.md — the inventory

Every workspace gets a `TOOLS.md` listing:

- What tools are available
- What each tool *can* do
- The risk level of each (low / medium / high / critical)
- Whether human approval is required
- Failure-handling rules

Template: [templates/TOOLS.md.template](../templates/TOOLS.md.template).
