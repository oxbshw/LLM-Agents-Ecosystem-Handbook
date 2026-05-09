# MEMORY.md — Minimal example

> Index of durable, distilled facts. One line per entry. Add `(YYYY-MM-DD)` so we can expire stale entries.

## Project
- Repo ships a single `csv2md` CLI; no library API yet (2026-04-12)
- Reports must be single-file Markdown; no images (2026-04-12)

## User
- Prefers terse responses with diffs over prose explanations (2026-04-15)

## Decisions
- We use `ruff` (not black + flake8) for one-tool simplicity (2026-04-10)

## Open questions
- Do we want a JSON output mode? — pending user decision
