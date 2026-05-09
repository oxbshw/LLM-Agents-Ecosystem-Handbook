# Skill maturity model

A skill's stage tells the agent (and the human reviewer) how much to trust it.

## Stages

### 🔬 Experimental
- Built recently, behavior may change between sessions
- Smoke-tested, no regression eval yet
- Loaded **only when explicitly enabled**
- May call tools at any risk tier (gated by approvals)
- File header: `version: 0.x.y`, `status: experimental`

### 🟡 Beta
- Used in real work for at least a few sessions
- Has at least one example + one failure-mode documented
- Some eval coverage (golden case + 1–2 edge cases)
- Loaded by default, with caveats in description
- File header: `status: beta`

### ✅ Production
- Regression-eval'd against [`evals/`](../evals/) suites
- Security-reviewed (per [security_checklist.md](security_checklist.md))
- All references stable; no hard-coded paths
- Risk-tiered tool calls; approvals wired
- File header: `status: production`

### 🪦 Deprecated
- Replaced by a newer skill OR no longer maintained
- Marked with `superseded_by:` pointing to the replacement
- Not loaded by default
- Removed in next major after a deprecation window

## Promotion checklist (experimental → beta)

- [ ] Description starts with "Use when …" and is specific
- [ ] At least one golden input → expected output
- [ ] Failure modes documented
- [ ] No project-specific paths

## Promotion checklist (beta → production)

- [ ] All experimental criteria
- [ ] Regression eval added to `evals/datasets/`
- [ ] Eval threshold met for ≥ 2 weeks
- [ ] Walked [skill_quality_checklist.md](../checklists/skill_quality_checklist.md)
- [ ] Walked [security_checklist.md](security_checklist.md)
- [ ] Reviewed by a second human if it calls High-risk tools

## Demotion / deprecation

A production skill should be demoted (or deprecated) if:

- Regression eval fails for two consecutive runs without a fix
- Security review surfaces an issue
- A dependency it relies on is end-of-life
- A better skill supersedes its purpose

## Frontmatter shape

```yaml
---
name: research-summarizer
description: Use when ...
version: 0.3.1
status: beta            # experimental | beta | production | deprecated
risk: low               # low | medium | high | critical
tags: [research, read-only, network-required]
maintainer: <github-handle or team>
superseded_by: <name>   # if deprecated
---
```

Tools that load skills can read these fields to filter (e.g., "load production-only" in a high-stakes session).
