# Tool risk levels

The canonical risk taxonomy used across the handbook. Use these labels in `TOOLS.md`.

## Levels

| Level | Definition | Examples | Approval | Logging |
|---|---|---|---|---|
| **Low** | Read-only, no side effects | search, summarization, format conversion, file read | none | sampled |
| **Medium** | Reversible writes, low blast radius | drafting files, creating tickets, posting to staging, DB read+upsert | sometimes (first-time per scope) | full |
| **High** | Reversible but high blast radius, OR irreversible-but-recoverable | sending email, modifying repos, running shell, calling production APIs, paid API calls | required | full + alert |
| **Critical** | Irreversible or high-cost | deleting data, force-pushing, spending money, changing IAM, transferring funds | always + 2nd reviewer | full + immutable |

## How to assign a level

Ask in order:

1. **Reversible?** No → at least High.
2. **Costs money or scarce resource?** Yes → at least High.
3. **Affects users beyond the requester?** Yes → bump one level.
4. **Touches secrets / IAM / billing?** Yes → Critical.

When in doubt, label higher and downgrade later with evidence.

## Common mistakes

- ❌ Labelling `gh.pr.create` as Low because "the PR can be closed"  → still High (notifies people, runs CI, may auto-merge)
- ❌ Labelling `shell` as Medium because "we're careful" → Critical, because the model isn't
- ❌ Labelling `db.query` as Low without checking the DSN — read-only DSN is Low; read-write is Medium–High depending on table

## Mapping to `TOOLS.md`

```markdown
| Tool | Purpose | Risk | Approval |
|---|---|---|---|
| `gh.repo.search` | search repos | Low | none |
| `gh.issue.create` | open issue | Medium | first-time |
| `gh.pr.create` | open PR | High | required |
| `gh.pr.merge` | merge PR | High | required |
| `gh.repo.delete` | delete repo | Critical | always + 2nd |
```
