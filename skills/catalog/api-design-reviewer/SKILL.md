---
name: api-design-reviewer
description: Use when reviewing a proposed REST or GraphQL API change before merge — checks contract clarity, backwards compatibility, errors, pagination, auth, and naming.
version: 0.1.0
status: experimental
risk: low
tags: [engineering, read-only, writes-files]
---

# API Design Reviewer

## When to use
- A new endpoint / mutation / schema is being proposed
- A breaking change is on the table
- An API draft needs a second pair of eyes before stakeholder review

## When NOT to use
- Pure implementation details (use `repo-auditor`)
- UI / UX feedback
- Cost / SLA tradeoffs (those need product discussion)

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `spec` | path or text | yes | OpenAPI / GraphQL SDL / Markdown design doc |
| `mode` | `"public"` \| `"internal"` | no | Default `internal`. `public` raises the bar on backwards-compat. |

## Outputs
A Markdown review with sections: Critical, Important, Nits, Open questions.

## Workflow
1. Parse the spec; list the operations / types touched
2. For each operation, walk `references/api-review-checklist.md`:
   - Naming consistent with neighbors?
   - Resource model coherent?
   - Errors enumerated and typed?
   - Pagination present (where lists are returned)?
   - Auth + authz documented?
   - Idempotency on writes?
   - Versioning strategy?
3. For breaking changes, surface the contract delta explicitly
4. Group findings into **Critical** (blockers), **Important** (should fix), **Nits** (style)
5. Append **Open questions** for the author

## References
- [`references/api-review-checklist.md`](references/api-review-checklist.md)

## Success criteria
- 0 fabricated findings (every finding cites a section of the spec)
- Critical/Important findings have a concrete suggested fix
- Tone is collegial, not pedantic

## Failure modes
- Spec too large (> 200 ops) → split into modules and ask the author which to focus on
- Internal jargon in the spec without definitions → list as Open questions, don't guess

## Examples
- Good: "Critical — `GET /users` returns an unbounded list. Add cursor pagination (suggested: `?cursor=...&limit=...`)."
- Bad: "I think pagination might be useful here."
