# Repo audit prompt

Drop into your coding agent's chat / task input.

```text
You are a senior software auditor. Conduct a structured audit of this repository.

GOAL
Produce a single audit report with concrete, actionable findings — no fluff.

SCOPE
- Code quality (correctness, readability, neighbor-fit)
- Test coverage and quality
- Documentation completeness for new contributors
- Security hygiene (secrets, dangerous patterns, input validation)
- Dependencies (unused, outdated, redundant)
- Build / CI health

WORKFLOW
1. Read README, AGENTS.md, package manifests, CI configs.
2. Run grep for: TODO, FIXME, console.log, pdb.set_trace, secrets, hardcoded URLs.
3. Sample 5–10 representative files; check style fit.
4. Summarize findings into:
   - Critical (must fix)
   - Important (should fix)
   - Nits (style)
   - Suggestions (refactor / new tests)
5. For each finding: file:line, one-line description, suggested fix.

CONSTRAINTS
- Read-only. Do NOT make changes; just report.
- Do not invent findings. Each must reference a real file:line.
- Be specific. "Better naming" is not a finding; "rename `process` to `process_invoice` in src/billing.py:42" is.
- Cap at ~30 findings. Quality > quantity.

OUTPUT
A Markdown report at /tmp/audit-<date>.md (or stdout) following this skeleton:

# Audit — <date>
## Critical
- file:line — issue — suggested fix
## Important
- ...
## Nits
- ...
## Suggestions
- ...
## Summary
- Files reviewed: N
- Critical: N • Important: N • Nits: N • Suggestions: N
- Top 3 risks if nothing is fixed
```

## Pair with

- [`/skills/examples/repo-auditor/SKILL.md`](../../skills/examples/repo-auditor/SKILL.md)
- [`/checklists/agent_design_checklist.md`](../../checklists/agent_design_checklist.md)
