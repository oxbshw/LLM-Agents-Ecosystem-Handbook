---
name: research-summarizer
description: Use when the user asks for a sourced briefing on a topic that spans multiple web sources and requires citations.
version: 0.1.0
---

# Research Summarizer

## When to use
- User asks "research X" / "what's the state of Y" / "summarize the literature on Z"
- The answer requires multiple sources, not one
- The user expects citations

## When NOT to use
- Single-source summarization (use a plain summarize tool)
- Code search (use `repo-auditor` or grep)
- Opinion / recommendation requests (this skill produces neutral briefings)

## Inputs
| Name | Type | Required | Notes |
|---|---|---|---|
| `topic` | string | yes | the question to research |
| `depth` | "shallow" \| "deep" | no | default "shallow" (5–7 sources); "deep" → 10–15 |
| `audience` | string | no | shapes vocabulary level (e.g., "executive", "engineer") |

## Outputs
A Markdown file `briefing.md` following the structure in `references/report-template.md`.

## Workflow
1. **Plan**: produce 3–7 sub-questions covering breadth and depth
2. **Search + fetch**: for each sub-question, run `web_search` then `fetch_url` for top 2–3 hits
3. **Cluster**: group findings by claim; load `references/clustering-rules.md`
4. **Draft**: fill `references/report-template.md` — every claim needs a `[n]` citation
5. **Validate**: every citation resolves; no domain dominates (≥ 3 distinct domains for shallow, ≥ 5 for deep)
6. **Self-review** against success criteria below

## References
- [`references/report-template.md`](references/report-template.md) — the output structure
- (add `clustering-rules.md`, `domain-allowlist.md` as the skill matures)

## Success criteria
- ≥ 5 sources for shallow, ≥ 10 for deep
- ≥ 3 distinct domains
- 0 unsourced claims (or all flagged `(unsourced)`)
- Open Questions section populated

## Failure modes
- Fewer sources available than required → return partial result, flag at top
- All sources from one domain → reject, retry plan with broader scope
- Network error → fail loudly, don't fabricate

## Examples
- See `references/examples/` (TBD) for one shallow and one deep run
