# Coding agent workflows

Four shapes that cover ~90% of what coding agents do. Pick the one closest to your task; reach for a [prompt template](prompts/) to drive it.

## 1. Feature implementation

```
Read issue → restate task → list files to read → read → plan files to edit
→ edit → run tests → fix → run tests → self-review → open PR → request review
```

**Key controls:**
- "Plan first; ask before editing" rule in `AGENTS.md`
- Smallest-diff bias documented in `SOUL.md`
- Test commands authoritative

📖 [`prompts/feature_implementation_prompt.md`](prompts/feature_implementation_prompt.md)

## 2. Bug fix

```
Reproduce → write failing test → fix → confirm test passes → check for similar bugs
→ open PR with the failing-test-first commit
```

**Key controls:**
- Reproduction step is non-negotiable — the agent doesn't fix what it can't reproduce
- "Failing test first" pattern means the bug can't regress silently

📖 [`prompts/bugfix_prompt.md`](prompts/bugfix_prompt.md)

## 3. Repo audit

```
Scan changed files → walk audit checklist → group findings by severity
→ produce a structured report → propose fixes (do not apply)
```

**Key controls:**
- Read-only by default
- Findings are *suggestions*; the human decides
- Severity tiers are explicit

📖 [`prompts/repo_audit_prompt.md`](prompts/repo_audit_prompt.md), [skills/examples/repo-auditor](../skills/examples/repo-auditor/SKILL.md)

## 4. Modernization

```
Inspect baseline → write modernization plan (in repo) → implement in phases
→ run tests + evals after each phase → CHANGELOG entry → release notes
```

**Key controls:**
- A *written plan* before any change (this very handbook used the pattern)
- Phases are small enough to revert
- Each phase has a smoke test

📖 [`prompts/modernization_prompt.md`](prompts/modernization_prompt.md), [`/templates/REPO_MODERNIZATION_PROMPT.md.template`](../templates/REPO_MODERNIZATION_PROMPT.md.template)

## Cross-cutting practices

### Smallest diff bias
A 200-line diff is reviewable; a 2,000-line diff is not. The agent should *prefer* small.

### One concept per PR
A "fix bug + refactor + add feature" PR is three PRs in a trench coat. Push back.

### No silent fixes
If the agent encounters a failing test it didn't expect, it stops and surfaces. Working around the failure is worse than reporting it.

### Resume-able sessions
Long tasks fail mid-flight. Save state (plan, partial diffs, scratchpad notes) so the next session resumes rather than restarts.

### After-task distillation
End every session with a memory-curator pass ([agent-memory-curator](../skills/examples/agent-memory-curator/SKILL.md)) so learnings survive.

## Anti-patterns

- ❌ "Just figure it out" prompts on a 100-file PR
- ❌ Wide-open `shell` access without gates
- ❌ Auto-merging
- ❌ Asking for a feature without a definition of "done"
- ❌ Letting the agent extend its own scope mid-PR
