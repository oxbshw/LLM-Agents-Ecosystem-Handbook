# TOOLS.md — Coding agent

| Tool | Purpose | Risk | Approval |
|---|---|---|---|
| `read_file` / `glob` / `grep` | Read code | Low | none |
| `edit_file` | Edit code | Medium | none |
| `write_file` | Create files | Medium | none |
| `run_tests` | Test suite | Low | none |
| `run_lint` | Lint / typecheck | Low | none |
| `git: status / diff / branch / commit` | Local git | Medium | none |
| `git: push` | Push branch | High | required |
| `gh: pr create` | Open PR | High | required |
| `shell` | Arbitrary shell | High | required |

## Forbidden without explicit user request
- `git push --force` to any branch
- `git reset --hard` / `git clean -fd`
- Anything modifying `main` directly
- Modifying `.env*` or files matching `*credentials*`

## Approval policy
See `HUMAN_APPROVAL_POLICY.md`.
