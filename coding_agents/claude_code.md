# Claude Code

Anthropic's Claude Code CLI is a coding-agent harness with a strong production track record. The patterns below apply broadly; specifics may evolve — verify against current docs.

## Files Claude Code reads

| File | Purpose |
|---|---|
| `CLAUDE.md` (or `AGENTS.md`) | Repo conventions, conventions, test commands |
| `.claude/settings.json` | Permissions, env vars, MCP servers |
| `.claude/skills/<name>/SKILL.md` | Loadable skills |
| `.claude/commands/*.md` | Slash commands |
| `.claude/agents/*.md` | Sub-agent definitions |
| `.claude/hooks/*` | Pre/post event hooks |

The handbook's `AGENTS.md` ([template](../templates/AGENTS.md.template)) doubles as `CLAUDE.md` — the content is identical. Many users symlink one to the other.

## What works well

- **Plan-then-act**: a one-shot prompt saying "plan first, ask before editing" reduces surprise.
- **Permissioned tools**: declare allowlists in `.claude/settings.json` so the agent doesn't request approval for every read.
- **Skills with progressive disclosure**: dropping a `references/` folder beats a giant prompt.
- **Sub-agents** for specialized roles (planner / worker / reviewer split).

## What to be careful with

- **Auto-merging**: gate behind explicit approval; the model is opinionated about scope.
- **Force operations**: `git push --force`, `reset --hard` should be in the never-without-approval list.
- **Long sessions**: memory grows; periodically distil with [agent-memory-curator](../skills/examples/agent-memory-curator/SKILL.md).

## Mapping to this handbook

| Need | Where |
|---|---|
| Repo instructions | `AGENTS.md` (filled from [/templates/AGENTS.md.template](../templates/AGENTS.md.template)) |
| Identity | `SOUL.md` ([template](../templates/SOUL.md.template)) |
| Memory | `MEMORY.md` ([template](../templates/MEMORY.md.template)) |
| Tools registry | `TOOLS.md` ([template](../templates/TOOLS.md.template)) |
| Skills | `.claude/skills/<name>/SKILL.md` ([template](../templates/SKILL.md.template)) |
| MCP servers | `.claude/settings.json` + [`mcp/`](../mcp/) docs |
| Approval policy | [`HUMAN_APPROVAL_POLICY.md`](../templates/HUMAN_APPROVAL_POLICY.md.template) |

## Patterns we recommend

### "Plan first, ask before editing"

In your `AGENTS.md`:
```
WORKFLOW
1. When given a task, restate it in one paragraph.
2. List files you plan to read or modify.
3. Ask before any write or shell command beyond the allowlist.
```

### Allowlists, not approvals-for-everything

Whitelist common reads (`grep`, `glob`, `cat` analogs) so the agent isn't constantly interrupted. Reserve approvals for High/Critical tools.

### Skills > long system prompts

If a workflow recurs, capture it as a Skill. Smaller system prompt = more headroom for actual work.

### Hooks for guardrails

Pre-commit hooks that block forbidden patterns (secrets, large binaries, force-pushes) are cheap insurance.

## What this section is NOT

- A reference for current Claude Code commands or settings — those evolve. Check current docs.
- A claim that Claude Code is "best." Pick what fits your team.
