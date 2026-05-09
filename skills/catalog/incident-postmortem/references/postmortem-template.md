# Postmortem template

```markdown
# {{Incident ID}} — {{Title}}

**Severity:** {{S0|S1|S2|S3}}
**Date:** {{YYYY-MM-DD}}
**Authors:** {{role / role}}

## Summary
{{1 paragraph}}

## Impact
- Users affected: {{count or %}}
- Duration: {{...}}
- Dollar impact: {{$ if estimable}}
- Trust impact: {{...}}

## Timeline (UTC)
| Time | Event |
|---|---|
| HH:MM | {{...}} |

## Direct cause
{{One sentence.}}

## Contributing factors
- {{factor}}
- {{factor}}

## What went well
- {{...}}

## What didn't go well
- {{...}}

## Action items
| Item | Owner | Due |
|---|---|---|
| {{...}} | @owner | YYYY-MM-DD |

## Lessons (long-term)
{{What we change so this class of incident is rarer next year.}}
```
