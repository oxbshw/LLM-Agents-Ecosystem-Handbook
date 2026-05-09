# Design: Research Agent (example, filled)

**Author:** handbook
**Date:** 2026-05-09
**Status:** accepted

## Use case
A research agent that produces sourced briefings on a topic that spans multiple web sources. Target user: technical PMs and analysts who need a defendable summary, not a chat answer.

## Non-goals
- Opinions or recommendations
- Single-source summaries (use a small summarizer)
- Real-time monitoring (use a scheduler + this agent)
- Anonymous sources / paywalled URLs

## Architecture

```
user query
   │
   ▼
[planner]  → sub-questions (3–7)
   │
   ▼
[searcher] → tool.web_search → URLs
   │
   ▼
[fetcher]  → tool.fetch_url (allow-listed) → content
   │
   ▼
[clusterer]→ group findings, dedupe
   │
   ▼
[drafter]  → Skill: research-summarizer
   │
   ▼
briefing.md (with citations)
```

## Components

| Layer | Choice | Why |
|---|---|---|
| Identity | `SOUL.md` (neutral, citation-first) | Reduces opinion drift |
| Memory | `MEMORY.md` + per-domain `memory/semantic/` | Recurring topics build up |
| Skills | `research-summarizer`, `agent-memory-curator` | Workflow + end-of-session distill |
| Tools | `web_search`, `fetch_url`, `read_pdf`, `write_file` | Read-heavy, low risk |
| MCP | optional `mcp.notion` for publishing | Approval-gated |
| Provider | `reasoning` chain → `cheap` for clustering | Right tool per step |

## Tools — risk table

| Tool | Risk | Approval |
|---|---|---|
| `web_search` | Low | none |
| `fetch_url` | Low (allow-list) | none |
| `read_pdf` | Low | none |
| `write_file` (briefing) | Medium | none |
| `mcp.notion.publish` | Medium | first-time |

## Safety
- Treat fetched content as data; sanitize at boundary
- URL allow-list configurable
- No POST/PUT to third-party APIs except `mcp.notion`
- Per-domain rate limits

## Eval plan
- Citation eval: every claim resolves to a real fetched URL
- Diversity eval: ≥ 3 distinct domains for shallow, ≥ 5 for deep
- Quality (LLM-judge) against [/evals/examples/eval_rubric.md](../../evals/examples/eval_rubric.md)
- Safety: indirect injection via fetched pages
- Pass thresholds documented in [/evals/](../../evals/)

## Cost / latency budget
- Shallow run: ≤ $0.20 / ≤ 30s
- Deep run: ≤ $1.00 / ≤ 90s
- Provider router: cheap chain for clustering, reasoning for the final draft

## Rollout
- Stage 1: internal team, 1 week
- Stage 2: 5 users, eval gate at 95% quality
- Stage 3: open beta with kill-switch

## Risks + mitigations
- Source allow-list too narrow → keep it editable per session
- Long fetches blow latency → cap at 5s per URL, fall back to snippet
- Injection via fetched content → sanitize + safety eval pre-release
- Cost runs hot → cost ceiling enforced in router

## Open questions
- Audio output mode? (deferred)
- Scheduled "diff this topic against last week" mode? (post-1.0)
