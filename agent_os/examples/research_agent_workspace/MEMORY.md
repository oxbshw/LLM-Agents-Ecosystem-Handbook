# MEMORY.md — Research agent

## Project
- Output format is `briefing.md` with sections: Question, Findings, Open Questions, Sources (2026-04-01)
- Source allowlist controlled via `policies/source_allowlist.yaml`

## Recurring topics (semantic)
- See `memory/semantic/` for one file per recurring research domain

## Decisions
- Use `tavily` + `firecrawl` for fetch; fall back to direct HTTP only if both fail (2026-03-22)
