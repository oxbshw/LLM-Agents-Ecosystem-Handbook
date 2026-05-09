# AGENTS.md — Coding agent

## Project
A senior coding agent that reads issues, proposes plans, edits code, runs tests, and opens PRs.

## Conventions
- Read existing code before editing; match style
- Smallest diff that solves the problem
- Comments only where the *why* is non-obvious

## Workflow
1. Restate the task in one paragraph
2. Plan: list files to touch
3. Edit
4. Run tests + lint
5. Self-review against `checklists/agent_design_checklist.md`
6. Open PR with the standard template

## Don'ts
- Don't add new dependencies without approval
- Don't refactor outside the task scope
- Don't push to `main`; always work on a branch

## Test commands
- `pytest -q`
- `ruff check && ruff format --check`
- `mypy src`
