# Agent OS

> An **Agent OS** is the set of structured files, conventions, and runtime layers that make an LLM agent reliable, observable, and safe across runs. It is to agents what a project skeleton is to web apps.

This directory is the conceptual core of the handbook. Everything else (templates, blueprints, examples) is an instantiation of the ideas here.

## The problem

A naive agent is a prompt + a tool loop. That works for demos, but in production you need answers to:

- *Who* is the agent? (identity, voice, refusal style)
- *What does it know* about this user / this project across runs? (memory)
- *What can it do* and *what is gated*? (tools, risk levels, approvals)
- *How does it do non-trivial tasks repeatably*? (skills)
- *How does it integrate* with external systems? (MCP)
- *How do we know* it works and didn't regress? (evals, traces)
- *How do we ship it* and roll back? (deployment, release checklist)

The Agent OS answers each of these with a small, named, version-controlled file or layer.

## The layers

| Layer | Owns | File(s) | Read |
|---|---|---|---|
| **Identity** | Personality, mission, refusal style | `SOUL.md`, `USER.md`, `AGENTS.md` | [agent_identity.md](agent_identity.md) |
| **Memory** | Durable facts across runs | `MEMORY.md`, vector store, logs | [memory_layer.md](memory_layer.md) |
| **Skills** | Reusable workflows | `skills/<name>/SKILL.md` | [skills_layer.md](skills_layer.md) |
| **Tools / MCP** | External actions and context | `TOOLS.md`, MCP servers | [mcp_layer.md](mcp_layer.md) |
| **Safety** | Guardrails, approvals, policies | `GUARDRAILS.md`, `HUMAN_APPROVAL_POLICY.md` | [safety_layer.md](safety_layer.md) |
| **Observability** | Traces, spans, costs, evals | traces/, evals/ | [observability_layer.md](observability_layer.md) |

## Why files, not just prompts?

Prompts are ephemeral. Files are:

- **Versioned** — diffable in git, reviewable in PRs
- **Composable** — load only what's needed (progressive disclosure)
- **Auditable** — humans *and* coding agents can read them
- **Portable** — same `AGENTS.md` works across IDEs and harnesses

This pattern is now an emerging community convention (Cursor, Claude Code, Aider, OpenAI Codex, Cline) — different tools, same files.

## Recommended workspace layout

See [workspace_layout.md](workspace_layout.md) for the canonical tree, and the [examples/](examples/) folder for three filled-in workspaces (minimal / research / coding).

## Workflow

1. **Initialize** — copy templates from [`/templates`](../templates) into your project's `.agent/` (or root)
2. **Fill** `SOUL.md`, `AGENTS.md`, `USER.md` first — they shape every later decision
3. **Add** memory and skills as patterns emerge from real runs
4. **Wire** tools and MCP servers with explicit risk levels in `TOOLS.md`
5. **Trace + eval** before shipping ([observability_layer.md](observability_layer.md))
6. **Use** the [release checklist](../templates/AGENT_RELEASE_CHECKLIST.md) before each deploy

## Common mistakes

- ❌ Treating `MEMORY.md` as a chat log → it should be *distilled* facts, not transcripts
- ❌ Putting secrets in `TOOLS.md` → use `.env`
- ❌ Conflating `SOUL.md` (identity) with `AGENTS.md` (repo rules) — keep them separate
- ❌ Letting MCP tools auto-execute critical actions — gate behind approvals
- ❌ Shipping without traces — you cannot debug what you cannot see
