# Workspace Layout

The canonical layout for an Agent OS workspace. Adapt as needed — the principles matter more than the directory names.

```
your-project/
├── .agent/                       ← agent workspace (sometimes lives at repo root)
│   ├── AGENTS.md                 ← repo-specific instructions (every coding agent reads this)
│   ├── SOUL.md                   ← identity, voice, mission, refusal style
│   ├── USER.md                   ← user profile + preferences
│   ├── MEMORY.md                 ← durable distilled memory (index)
│   ├── TOOLS.md                  ← tool inventory + risk levels + approval gates
│   ├── GUARDRAILS.md             ← safety policy
│   ├── HUMAN_APPROVAL_POLICY.md  ← who approves what
│   │
│   ├── skills/                   ← progressive-loading workflows
│   │   ├── research-summarizer/
│   │   │   ├── SKILL.md          ← spec (model loads first)
│   │   │   ├── references/       ← loaded only when needed
│   │   │   └── scripts/          ← optional helper scripts
│   │   └── …
│   │
│   ├── memory/                   ← memory storage (when not in MEMORY.md)
│   │   ├── episodic/             ← per-run logs
│   │   ├── semantic/             ← distilled facts (one file per topic)
│   │   ├── decisions/            ← decision log (ADR-style)
│   │   └── user_*.md             ← per-user memory files
│   │
│   ├── mcp/                      ← MCP server configs + docs
│   │   ├── servers.json          ← which MCP servers this agent uses
│   │   └── <server>.md           ← per-server doc using MCP_SERVER.md.template
│   │
│   ├── policies/                 ← machine-readable policy files
│   │   ├── allowed_tools.yaml
│   │   └── approval_rules.yaml
│   │
│   ├── evals/                    ← regression evals owned by this agent
│   │   ├── EVAL_PLAN.md
│   │   ├── datasets/*.jsonl
│   │   └── rubrics/*.md
│   │
│   ├── logs/                     ← runtime artifacts (gitignored except samples)
│   │   ├── traces/
│   │   ├── daily/
│   │   └── decisions/
│   │
│   └── AGENT_RELEASE_CHECKLIST.md
│
├── src/                          ← your application code
├── .env.example
└── README.md
```

## Layout principles

1. **One responsibility per file.** `SOUL.md` is *not* `AGENTS.md` is *not* `MEMORY.md`. Keep them small and focused.
2. **Progressive disclosure.** Top-level files are short; details live in `references/` and load only when needed.
3. **Index, don't dump.** `MEMORY.md` is an index pointing at per-topic files — not a giant scroll.
4. **Gitignore the runtime.** `logs/` and any secret-bearing files are gitignored; templates and samples are committed.
5. **Same files everywhere.** The same `AGENTS.md` should work in Claude Code, Cursor, Codex, Aider, Cline. Don't fork per tool.

## Minimal vs full

You don't need every file on day one. A reasonable graduation:

| Stage | Add |
|---|---|
| Day 1 | `AGENTS.md`, `SOUL.md` |
| When patterns repeat | `MEMORY.md`, `TOOLS.md` |
| When tasks repeat | `skills/<name>/SKILL.md` |
| When integrating external systems | `mcp/` |
| Before first user touches it | `GUARDRAILS.md`, `HUMAN_APPROVAL_POLICY.md`, `evals/` |
| Before production | `AGENT_RELEASE_CHECKLIST.md` |

See [examples/minimal_agent_workspace](examples/minimal_agent_workspace) for the smallest viable workspace and [examples/coding_agent_workspace](examples/coding_agent_workspace) for a fuller one.
