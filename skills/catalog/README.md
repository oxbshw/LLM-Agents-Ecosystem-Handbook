# Skill catalog

The handbook's curated, in-repo skill catalog. Small by design — every entry is something we'd actually use.

## What's here

- [index.md](index.md) — every skill, one line each, with status + risk
- [categories.md](categories.md) — domain → skill mapping
- Per-skill folders below this directory

## Adding a skill to the catalog

1. Walk [skill_quality_checklist.md](../../checklists/skill_quality_checklist.md)
2. Walk [security_checklist.md](../security_checklist.md)
3. Drop the folder under `catalog/<skill-name>/` with `SKILL.md`
4. Update [index.md](index.md) and [categories.md](categories.md)
5. Open a PR

New skills enter as **experimental**. Promote per [skill_maturity_model.md](../skill_maturity_model.md).

## Curation philosophy

We curate, we don't mirror. See [awesome_skills_catalog.md](../awesome_skills_catalog.md). Quality bar:

- Description starts with "Use when" and is specific
- Workflow is numbered, references load progressively
- Success criteria + failure modes both present
- No project-specific paths
- Risk-tiered tools, approvals where needed
