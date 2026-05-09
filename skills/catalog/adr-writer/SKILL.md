---
name: adr-writer
description: Use when capturing an architecture decision so it survives turnover — produces an ADR-NNNN.md from context, options considered, and the chosen path.
version: 0.1.0
status: experimental
risk: low
tags: [design, writes-files]
---

# ADR Writer

## When to use
- A non-trivial architecture decision was just made
- Reverse-documenting a decision that wasn't recorded but should have been
- Preparing for a design review

## When NOT to use
- Trivial choices (naming, formatting)
- Operational runbooks (those go to `runbooks/`)
- Product decisions without architectural impact

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `context` | string | yes | The problem being solved, in 2–4 sentences |
| `options` | list | yes | Alternatives considered |
| `decision` | string | yes | Chosen path |
| `number` | int | no | If omitted, finds next ADR number from `memory/decisions/` |

## Outputs
A file at `memory/decisions/ADR-NNNN-<slug>.md` matching the [ADR template](../../../templates/ADR.md.template).

## Workflow
1. Find the next ADR number (or use `number` input)
2. Slugify the decision's main subject
3. Fill the template:
   - Context, Decision, Alternatives, Consequences (positive + negative)
   - Status: `accepted` (default), `proposed`, `superseded by ADR-XXXX`
4. Write to `memory/decisions/ADR-NNNN-<slug>.md`
5. Add a one-line entry to `MEMORY.md#decisions`

## References
- [`../../../templates/ADR.md.template`](../../../templates/ADR.md.template)
- [`../../../design_docs/adr_guide.md`](../../../design_docs/adr_guide.md)

## Success criteria
- Each alternative has a one-line "why not"
- Consequences include at least one negative
- File name matches `ADR-\d{4}-[a-z0-9-]+\.md`

## Failure modes
- Decision is actually a bundle of decisions → split into multiple ADRs
- Context is unclear → ask user for clarification, don't fabricate
