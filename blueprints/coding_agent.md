# Blueprint: Coding agent

## Use case
Reads issues, plans changes, edits code, runs tests, opens PRs. Senior-engineer voice, smallest-diff bias.

## Non-goals
- Auto-merge to `main`
- Greenfield architecture decisions (those are human)
- Refactors outside the task scope

## Architecture

```
issue / task
    │
    ▼
[planner]  ── list files to touch, success criteria
    │
    ▼
[reader]   ── read_file, glob, grep
    │
    ▼
[editor]   ── edit_file, write_file
    │
    ▼
[verifier] ── run_tests, run_lint
    │
    ▼
[reviewer] ── Skill: repo-auditor
    │
    ▼
[publisher]── git: commit, push (approval), gh: pr create (approval)
```

## Tools (risk-tiered)

| Tool | Risk |
|---|---|
| read/glob/grep | Low |
| edit_file / write_file | Medium |
| run_tests / run_lint | Low |
| git: status/diff/branch/commit | Medium |
| git: push (non-`main`) | High (first-time approval) |
| gh: pr create | High |
| gh: pr merge | High + 2nd reviewer |
| shell (arbitrary) | Critical |

## Memory
- `AGENTS.md`: stack, conventions, test commands, PR rules
- `MEMORY.md`: project facts, decisions, fragile areas
- `memory/decisions/` ADRs

## Skills
- [`repo-auditor`](../skills/examples/repo-auditor/) — pre-PR audit
- [`agent-memory-curator`](../skills/examples/agent-memory-curator/) — end-of-session distillation

## Safety
- Forbid `--force`, `reset --hard`, direct edits to `main`
- No new top-level deps without approval
- Allow-list of branches the agent may push to

## Evals
- Regression: bugs the agent fixed before stay fixed
- Tool-call: right tools, right order, never `merge` without approval
- Quality: LLM-judge over PR diffs vs reference fixes
- Safety: refuses dangerous ops; resists injection in tool output

## Deployment
- Self-hosted on a build host with constrained shell
- Per-PR cost ceiling
- Audit log for all High calls

## Extensions
- Multi-repo support
- Issue triage mode (label, assign, link similar)
- Periodic codebase health scan
