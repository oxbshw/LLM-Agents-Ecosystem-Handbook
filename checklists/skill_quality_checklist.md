# Skill quality checklist

Before merging a new Skill.

## Frontmatter
- [ ] `name:` matches the folder name
- [ ] `description:` starts with "Use when …" and is specific
- [ ] `version:` set; bumped if behavior changed

## Content
- [ ] When to use + when NOT to use, both present
- [ ] Inputs table (name, type, required, notes)
- [ ] Outputs spec
- [ ] Workflow as numbered steps
- [ ] References listed and actually loaded by steps that need them
- [ ] Success criteria explicit
- [ ] Failure modes explicit

## Quality
- [ ] At least one example
- [ ] No project-specific paths hard-coded
- [ ] Composable (one purpose, doesn't bundle)
- [ ] Validates output before declaring success

## Security
- [ ] No secrets in scripts
- [ ] No outbound calls without need
- [ ] No destructive ops without approval gating
- [ ] Reviewed by a 2nd person if the Skill calls High-risk tools

## Test
- [ ] At least one golden input → expected output pair
- [ ] Smoke-tested manually or via script

📖 [skills/security_checklist.md](../skills/security_checklist.md)
