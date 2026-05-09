# Coding agents

Practical guidance for using and *building* agents that read repos, edit code, and open PRs. Tool-neutral by default — Claude Code, Cursor, Codex CLI, Aider, Cline, and custom runtimes all read the same files when configured well.

## What's here

- [claude_code.md](claude_code.md)
- [cursor.md](cursor.md)
- [codex.md](codex.md)
- [repo_instructions.md](repo_instructions.md) — what `AGENTS.md` should contain (and what to leave out)
- [coding_agent_workflows.md](coding_agent_workflows.md) — feature, bugfix, refactor, modernization
- [safe_refactoring.md](safe_refactoring.md) — staged, reversible
- [review_checklist.md](review_checklist.md) — what a coding-agent reviewer should check
- [prompts/](prompts/) — copy-paste task prompts

## How to use this with your existing tool

Most modern coding agents read a small set of files:

| File | Read by |
|---|---|
| `AGENTS.md` (or variants) | Cursor, Claude Code, Codex, Aider, Cline, Continue, Windsurf — broadly |
| `SOUL.md` | Custom runtimes; can be inlined into `AGENTS.md` for tools that don't load it directly |
| `MEMORY.md` | Conventions; some tools auto-load if mentioned in `AGENTS.md` |
| `TOOLS.md` | Documented surface; not auto-loaded everywhere |
| `.cursorrules` / `.cursor/*` | Cursor-specific |
| `.aider.conf.yml` | Aider |
| `CLAUDE.md` (repo) | Claude Code |

The handbook's recommendation: **write `AGENTS.md` first**, then tool-specific files only as thin pointers to the same content.

## The four big workflows

| Workflow | Doc |
|---|---|
| Feature implementation | [`prompts/feature_implementation_prompt.md`](prompts/feature_implementation_prompt.md) |
| Bug fix | [`prompts/bugfix_prompt.md`](prompts/bugfix_prompt.md) |
| Repo audit | [`prompts/repo_audit_prompt.md`](prompts/repo_audit_prompt.md) |
| Modernization | [`prompts/modernization_prompt.md`](prompts/modernization_prompt.md) |

Plus:
- [`prompts/provider_expansion_prompt.md`](prompts/provider_expansion_prompt.md) (specific to this handbook's pattern)
- [`prompts/docs_update_prompt.md`](prompts/docs_update_prompt.md)
- [`prompts/release_review_prompt.md`](prompts/release_review_prompt.md)

## Templates

- [`/templates/CODING_AGENT_TASK.md.template`](../templates/CODING_AGENT_TASK.md.template) — generic task prompt
- [`/templates/REPO_MODERNIZATION_PROMPT.md.template`](../templates/REPO_MODERNIZATION_PROMPT.md.template) — multi-phase modernization

## Stance

Coding agents are powerful when given:

- A small, dense `AGENTS.md`
- A clear task contract
- Tools at appropriate risk tiers
- Approval gates on the dangerous ones
- Memory of past decisions

They are *dangerous* when given:

- "Just figure it out" prompts on a 100-file PR
- Wide-open shell access without gates
- Unclear definition of "done"
- No traces / no eval

This section is the practical antidote.
