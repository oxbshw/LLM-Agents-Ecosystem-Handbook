# Skill Design Guide

A field guide for writing Skills the model actually uses well.

## 1. The description line is the entire game

The `description:` in YAML frontmatter is what the model sees when deciding whether to load the skill. Bad descriptions hide good skills.

| ❌ Bad | ✅ Good |
|---|---|
| "Research things on the web" | "Use when the user asks for a sourced briefing that spans multiple web sources and needs citations" |
| "Helps with code" | "Use before opening a PR to audit changed files for stale comments, unused imports, and missing tests" |
| "Does memory stuff" | "Use after a session to promote useful episodic notes from `logs/episodic/` to `memory/semantic/`" |

The pattern: **"Use when {{specific trigger}}"**, not "this skill does X."

## 2. Progressive disclosure

`SKILL.md` should fit in a screen. Long content goes into `references/`, loaded only at the step that needs it.

Bad shape:
```
SKILL.md (1500 lines: workflow + every reference + every example inline)
```

Good shape:
```
SKILL.md (80 lines)
references/
  citation-style.md
  report-template.md
  domain-allowlist.md
```

The workflow says: "Step 4: load `references/report-template.md` and follow the structure."

## 3. Specify inputs and outputs explicitly

Tables beat prose. The model reads tables more reliably:

```markdown
## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| topic | string | yes | the research question |
| depth | "shallow" \| "deep" | no | default "shallow" |
```

## 4. Workflow as numbered steps

Numbered steps are easier to follow than prose. Reference files at the step where they're needed:

```markdown
1. Plan sub-questions (3–7)
2. For each sub-question, run web_search + fetch_url
3. Cluster findings; load `references/clustering-rules.md`
4. Draft report against `references/report-template.md`
5. Validate citations resolve
6. Run `scripts/citation_check.py`
```

## 5. Define success and failure

Without success criteria, the model declares any output a success.

```markdown
## Success criteria
- Every claim has a citation
- ≥ 5 distinct domains
- No source from `references/blocklist.md`

## Failure modes
- Fewer than 3 sources → return partial result + flag
- All citations from one domain → reject and retry plan step
```

## 6. Compose, don't bundle

One Skill, one purpose. If a skill has two `## Mode A` / `## Mode B` sections, it's actually two skills. Split them — the descriptions will be more specific and the model will pick better.

## 7. Test the skill

Add at least:
- One golden input → expected output pair in `references/examples.md`
- A way to run a smoke test (`scripts/smoke_test.py` or a manual checklist)

## 8. Version it

Bump `version:` in frontmatter when the workflow changes. Older traces will reference the old version, which makes regressions debuggable.

## Anti-patterns

- 🚫 "All-purpose" skills (description longer than the workflow)
- 🚫 Skills that hard-code a project path
- 🚫 Skills that silently fall back to a default when inputs are missing
- 🚫 Skills with no failure mode documented
- 🚫 Skills with executable scripts but no security review
