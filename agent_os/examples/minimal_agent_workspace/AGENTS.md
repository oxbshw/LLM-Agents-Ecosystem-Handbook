# AGENTS.md — Minimal example

This is a minimal, repo-rules file. Drop it at the root of any project; coding agents will read it.

## Project

A small CLI that converts CSV to formatted Markdown reports.

## Conventions

- Python 3.11+, type hints required
- Format with `ruff format`, lint with `ruff check`
- One public function per module, internal helpers prefixed with `_`

## Testing

- `pytest -q` must pass before any commit
- Add a test for every new public function

## Don'ts

- Don't add new top-level dependencies without updating `requirements.txt`
- Don't commit anything in `data/`
- Don't run shell commands beyond formatting/testing without asking

## PRs

- Title: `[scope] short description`
- Squash on merge
