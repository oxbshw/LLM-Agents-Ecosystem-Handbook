# Skill vs Tool vs MCP — when to use which

Three building blocks, often confused. Pick the wrong one and you'll fight it forever.

## Quick decision

| If the thing is… | Use |
|---|---|
| A single function call | **Tool** |
| A multi-step *workflow* the agent runs internally | **Skill** |
| An external system you want exposed to many agents | **MCP** server |
| Durable state across runs | **Memory** (not on this list, but worth mentioning) |

## Side-by-side

| Dimension | Tool | Skill | MCP server |
|---|---|---|---|
| Unit of work | One function | Workflow (multiple steps) | Set of tools + resources |
| Loaded by | Always available | On-demand by description match | Connected at session start |
| Reusable across agents? | Per-codebase | Per-codebase (copy folder) | Yes — that's the point |
| Standardized? | Vendor-specific | Convention | Open protocol (MCP) |
| Where it lives | Your code | `skills/<name>/` | Separate process / repo |
| Best for | Atomic actions (`get_weather`) | Repeatable processes (`research-summarizer`) | Cross-cutting integrations (`github`, `filesystem`) |

## Worked examples

**Get current weather** → Tool. Atomic, single call, no workflow.

**Produce a sourced research briefing on a topic** → Skill. Multiple steps, references, validation, output format.

**Read/write GitHub issues, PRs, files** → MCP server. Want this in many agents (coding assistant, triage bot, research bot) without re-implementing per project.

**Curate user memory at the end of each session** → Skill. A workflow that calls tools (read logs, write memory file) but the orchestration itself is the value.

## Common mismatches

- ❌ Building a giant tool that does 5 things → make it a Skill that calls 5 small tools
- ❌ Building an MCP server for one agent → just write a tool unless you'll reuse
- ❌ Putting "what to do" inside a tool's docstring → that's a Skill description
- ❌ Embedding domain knowledge in a system prompt → put it in `references/` of a Skill

## Together

Real systems use all three:

```
Agent (SOUL.md, AGENTS.md, MEMORY.md)
├── Tools: write_file, run_tests
├── Skills: research-summarizer, repo-auditor
└── MCP servers: github, filesystem, browser
```

The skill *uses* tools and MCP capabilities; it doesn't replace them.
