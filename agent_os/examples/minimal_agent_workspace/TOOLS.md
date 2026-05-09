# TOOLS.md — Minimal example

| Tool | Purpose | Risk | Approval |
|---|---|---|---|
| `read_file` | Read project files | Low | none |
| `write_file` | Create / modify files | Medium | none |
| `run_tests` | `pytest -q` | Low | none |
| `run_format` | `ruff format` | Low | none |
| `shell` | Arbitrary shell | High | required |

## Restricted
- No `rm -rf`, `git push --force`, or any network call without approval

## On failure
- Tools must return structured errors; never swallow
- After 2 retries on the same tool, surface the error and stop
