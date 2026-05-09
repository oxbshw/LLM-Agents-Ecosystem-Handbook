# Repo instructions (`AGENTS.md`)

What every coding agent should be able to read at the top of your repo. Tool-neutral.

## What goes in

- One paragraph: what the project is, who uses it
- Stack (language, package manager, frameworks, test runner)
- Setup commands
- Conventions (style, naming, commits, branch names)
- Required checks before commit (lint, typecheck, tests)
- Tool-usage rules (preferred CLIs, forbidden ones)
- PR expectations (title format, description shape)
- Safety rules (forbidden destructive operations, secret-bearing files)
- Pointers to deeper docs (`SOUL.md`, `MEMORY.md`, `TOOLS.md`)

## What stays out

- Long architecture documentation (use `docs/` and link)
- Style guide examples (use a Skill `references/`)
- Anything tool-specific (Claude Code-only, Cursor-only) — keep `AGENTS.md` portable
- Secrets / env values (use `.env.example`)
- Per-feature prompts (use prompt templates per task)

## Length

Aim for ≤ 150 lines. If you're past that, you're describing the project too much. The agent will read code; trust it.

## Hierarchy in monorepos

Use per-package `AGENTS.md` files for local conventions:

```
AGENTS.md                            ← repo-wide
packages/api/AGENTS.md               ← API conventions
packages/web/AGENTS.md               ← frontend conventions
infra/AGENTS.md                      ← infra conventions
```

Some agents merge them; some pick the most specific. Either is fine — keep each file small.

## Test commands ARE the contract

Most agents will run your test commands as the success signal. Make sure:

- They actually pass on a clean checkout
- They run reasonably fast
- They fail loudly (not silently) on real issues

A coding agent paired with a green-but-meaningless test suite is dangerous.

## Recommended template

Use [`/templates/AGENTS.md.template`](../templates/AGENTS.md.template). It's the same template every section of this handbook recommends.

## Common mistakes

- ❌ Writing `AGENTS.md` as a brain-dump of the team's tribal knowledge — distill to rules
- ❌ Including legacy conventions you've moved away from
- ❌ Pasting build error logs as a "known issues" section — fix them or document the workaround upstream
- ❌ Forgetting to update when stack changes
- ❌ "PRs require approval from @me" — bottlenecks the agent. Make policies impersonal.
