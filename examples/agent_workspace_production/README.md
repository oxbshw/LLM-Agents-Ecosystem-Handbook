# Agent workspace — production

A fuller workspace ready for real users. Adds safety, evals, observability, and MCP wiring on top of the minimal shape.

## Layout

```
.agent/
├── SOUL.md  AGENTS.md  USER.md  MEMORY.md  TOOLS.md
├── GUARDRAILS.md
├── HUMAN_APPROVAL_POLICY.md
├── AGENT_RELEASE_CHECKLIST.md
├── skills/
│   ├── research-summarizer/
│   ├── repo-auditor/
│   └── agent-memory-curator/
├── mcp/
│   ├── servers.json
│   ├── github.md       # filled MCP_SERVER.md
│   └── filesystem.md
├── memory/
│   ├── semantic/
│   ├── decisions/
│   └── episodic/        # gitignored except samples
├── policies/
│   ├── allowed_tools.yaml
│   └── approval_rules.yaml
├── evals/
│   ├── EVAL_PLAN.md
│   ├── datasets/
│   └── rubrics/
└── logs/                # gitignored
    ├── traces/
    ├── approvals/
    └── decisions/
```

## What's added vs minimal

| Added | Why |
|---|---|
| `GUARDRAILS.md` | Risk-tiered behavior in code, not vibes |
| `HUMAN_APPROVAL_POLICY.md` | Explicit gate for High/Critical |
| `skills/` | Repeatable workflows |
| `mcp/` | Standardized integrations + security review |
| `memory/semantic/`, `decisions/` | Per-topic memory and ADRs |
| `evals/` | Regression + safety guardian |
| `logs/traces/` | Debuggability |

## Pre-ship

Walk [/templates/AGENT_RELEASE_CHECKLIST.md](../../templates/AGENT_RELEASE_CHECKLIST.md). Don't skip the safety + memory eval rows.
