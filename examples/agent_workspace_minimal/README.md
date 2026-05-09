# Agent workspace — minimal

The smallest viable Agent OS workspace. Five files. Fits in your head.

## Files

The five workspace files live as a filled example under [agent_os/examples/minimal_agent_workspace/](../../agent_os/examples/minimal_agent_workspace/):

- [`AGENTS.md`](../../agent_os/examples/minimal_agent_workspace/AGENTS.md) — repo conventions
- [`SOUL.md`](../../agent_os/examples/minimal_agent_workspace/SOUL.md) — identity, voice
- [`USER.md`](../../agent_os/examples/minimal_agent_workspace/USER.md) — user profile
- [`MEMORY.md`](../../agent_os/examples/minimal_agent_workspace/MEMORY.md) — distilled facts
- [`TOOLS.md`](../../agent_os/examples/minimal_agent_workspace/TOOLS.md) — tool inventory + risk

Copy that folder as a starting point.

## When to use this shape

- Solo / small project
- Single user
- Low-risk tools only
- No external integrations beyond a few function calls

## When to upgrade

When you find yourself wanting any of:
- Repeatable workflows → add Skills
- External integrations reused → add MCP
- High-risk tools → add `GUARDRAILS.md` + `HUMAN_APPROVAL_POLICY.md`
- Multi-user → switch to per-user memory isolation
- Production traffic → see [agent_workspace_production](../agent_workspace_production/)
