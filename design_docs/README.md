# Design docs

How to write design documents that humans *and* coding agents can act on. Includes:

- Agent-specific design docs
- General technical design docs
- ADRs (Architecture Decision Records)
- Design reviews
- Rollout plans
- A `DESIGN.md` machine-readable format spec for design tokens / specs
- Filled examples

## What's here

| File | Purpose |
|---|---|
| [agent_design_doc.md](agent_design_doc.md) | Designing one agent — scope, components, risks |
| [technical_design_doc.md](technical_design_doc.md) | The classic engineering TDD, adapted for AI systems |
| [adr_guide.md](adr_guide.md) | When to write an ADR, what to include |
| [design_review.md](design_review.md) | Running a design review meeting that matters |
| [rollout_plan.md](rollout_plan.md) | Shipping a design safely |
| [design_md_spec.md](design_md_spec.md) | The `DESIGN.md` format for machine-readable design specs |
| [examples/research_agent_design.md](examples/research_agent_design.md) | Filled example |
| [examples/mcp_agent_design.md](examples/mcp_agent_design.md) | Filled example |
| [examples/memory_agent_design.md](examples/memory_agent_design.md) | Filled example |
| [examples/provider_router_design.md](examples/provider_router_design.md) | Filled example |

## Templates

- [/templates/DESIGN_DOC.md.template](../templates/DESIGN_DOC.md.template)
- [/templates/ADR.md.template](../templates/ADR.md.template)

## When to write a design doc

- Non-trivial change touching ≥ 3 components
- Involves a tradeoff people will revisit later
- Affects users / cost / safety in a measurable way
- Requires alignment across teams

When NOT to:

- Trivial fix
- One-file change with no architectural impact
- Pure cleanup

## Lengths that work

| Doc type | Target |
|---|---|
| ADR | 1 page (≤ 500 words) |
| Agent design doc | 1–3 pages |
| Technical design doc | 2–6 pages |
| Rollout plan | 1 page |

If a doc grows beyond these, split.
