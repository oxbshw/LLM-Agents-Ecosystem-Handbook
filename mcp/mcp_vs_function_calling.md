# MCP vs function calling

Both let the model invoke external code. The difference is *who else can use it*.

## Side by side

| | Function calling | MCP |
|---|---|---|
| Standard | Vendor-specific JSON schema | Open protocol (JSON-RPC) |
| Reuse across agents | Copy code | Connect a server |
| Reuse across vendors | Rewrite | Same server |
| Discovery | App-defined | `tools/list` over the wire |
| Transport | In-process | stdio / SSE / HTTP |
| Distribution | Inside your repo | Separate package / server |
| Auth | App handles | Transport handles |
| Best for | One-app-only integrations | Reused integrations |

## Picking

- **One app, one model, a few functions** → function calling. Don't over-engineer.
- **Same integration across multiple agents/tools** → MCP server. Pays back fast.
- **External users want to wire your integration to *their* agents** → MCP server.
- **You want vendor-neutrality** → MCP server.

## Hybrid

Real systems use both:

```
Agent
├── Tools (function calling)        # repo-private, fast
│    ├── parse_invoice(...)
│    └── format_report(...)
└── MCP servers (reusable)
     ├── github
     ├── filesystem
     └── docs (your internal one)
```

Tools are the agent's *internal* hands; MCP is the agent's *interoperable* hands.

## Don't conflate these

- **Tool description ≠ Skill description.** A tool description tells the model how to *call* a function. A Skill describes *when* and *how* to do a multi-step workflow. → [skills/skill_vs_tool_vs_mcp.md](../skills/skill_vs_tool_vs_mcp.md)
- **MCP server ≠ Agent.** An MCP server is dumb (in the good sense) — it does the action. The agent decides whether and how.
