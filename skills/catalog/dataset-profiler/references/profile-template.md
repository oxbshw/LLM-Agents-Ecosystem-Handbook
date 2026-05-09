# Dataset profile template

```markdown
# Dataset profile — {{filename}}

**Source:** {{path / origin}}
**Profiled:** {{YYYY-MM-DD}}
**Rows:** {{N}} • **Columns:** {{N}} • **Size:** {{MB}}

## Schema
| Column | Dtype | Nullable | Example |
|---|---|---|---|
| {{...}} | {{...}} | yes/no | {{...}} |

## Missingness
| Column | % missing |
|---|---|
| {{...}} | {{N%}} |

## Distributions
### Numeric
| Column | min | p50 | p95 | max | std |
|---|---|---|---|---|---|

### Categorical
| Column | Cardinality | Top-5 |
|---|---|---|

## Outliers
- {{column}}: {{rule}} flagged {{N}} rows. Example: {{row excerpt}}.

## Keys & joins
- Likely keys: {{...}}
- Likely join columns: {{...}}

## Gotchas
- {{...}}

## Open questions
- {{ambiguous column / value — needs owner input}}
```
