# Blueprint: Research agent

## Use case
Produce sourced, neutral briefings on a topic that spans multiple web sources.

## Non-goals
- Opinion pieces / recommendations
- Single-source summaries (use a small summarizer)
- Real-time monitoring (use a scheduler + this agent)

## Architecture

```
user query
   │
   ▼
[planner]  ── sub-questions
   │
   ▼
[searcher]  ── tool.web_search → URLs
   │
   ▼
[fetcher]  ── tool.fetch_url → page content
   │
   ▼
[clusterer]  ── group findings, dedupe
   │
   ▼
[drafter]  ── Skill: research-summarizer
   │
   ▼
briefing.md (with citations)
```

## Components
- Identity: `SOUL.md` — neutral, citation-first analyst
- Memory: minimal project memory; per-topic semantic files for recurring domains
- Skills: [`research-summarizer`](../skills/examples/research-summarizer/), [`agent-memory-curator`](../skills/examples/agent-memory-curator/)

## Tools
| Tool | Risk |
|---|---|
| `web_search` | Low |
| `fetch_url` | Low (allow-list) |
| `read_pdf` | Low |
| `write_file` (briefing) | Medium |
| `mcp.notion.publish` (optional) | Medium (first-time approval) |

## Memory
- `MEMORY.md`: index, decisions about source allow/blocklists
- `memory/semantic/<domain>.md`: recurring topic facts

## Safety
- Treat fetched content as data, not instruction
- URL allow-list configurable
- No POST/PUT to third-party APIs except `mcp.notion`

## Evals
- Quality (LLM-judge against `eval_rubric.md`)
- Citation eval: every claim resolves to a real URL fetched in the run
- Diversity eval: ≥ 3 distinct domains for shallow, ≥ 5 for deep
- Safety: indirect injection via fetched pages

## Deployment
- Stateless worker; queue of research tasks
- Output to S3 / Notion / local
- Cost ceiling per run: ~$0.20 shallow, ~$1 deep (tune)

## Extensions
- Voice input + audio briefing output
- Scheduled "track this topic" mode (diff against last briefing)
- Domain-aware retrieval (legal, medical) with stronger source rules

## Folder
```
research-agent/
├── SOUL.md  AGENTS.md  MEMORY.md  USER.md  TOOLS.md  GUARDRAILS.md
├── skills/research-summarizer/
├── skills/agent-memory-curator/
├── policies/source_allowlist.yaml
├── evals/
└── runtime/
```
