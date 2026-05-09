# OpenAI Codex (CLI / cloud)

OpenAI's Codex agent, available as a CLI and a cloud-task surface. Reads `AGENTS.md` natively.

## What Codex reads

- `AGENTS.md` at repo root (and per-folder, hierarchically)
- Codex-specific config files (vary across CLI / cloud variants)

The hierarchical `AGENTS.md` is useful: a top-level file with global rules, and per-package files with local conventions.

## Mapping

| Handbook file | Codex location |
|---|---|
| `AGENTS.md` | reused directly; place at repo root |
| Per-package conventions | `packages/<x>/AGENTS.md` |
| `SOUL.md` | inline a short voice/identity section into `AGENTS.md` if Codex doesn't load it standalone |
| Skills | adapt to Codex's instruction model; or include workflow text inside `AGENTS.md` for tasks the agent will see |

## Patterns

### Hierarchical instructions

```
AGENTS.md                        ← repo-wide rules
packages/api/AGENTS.md           ← API-specific (testing, schemas)
packages/web/AGENTS.md           ← frontend-specific (style, accessibility)
```

This is one of the cleanest patterns when monorepo concerns differ.

### Cloud vs CLI

- **CLI**: long-running local sessions; gates and approvals are interactive
- **Cloud tasks**: assigned a task, runs autonomously to a PR. Higher autonomy = stricter pre-task spec.

Cloud tasks especially benefit from:
- A precise [`CODING_AGENT_TASK.md.template`](../templates/CODING_AGENT_TASK.md.template)
- A short, complete `AGENTS.md`
- A working test suite the agent can rely on

## Caveats

- Codex's command surface evolves; check current docs
- Cloud tasks operate in sandboxed environments — install commands matter
- Approval semantics differ across CLI and cloud
