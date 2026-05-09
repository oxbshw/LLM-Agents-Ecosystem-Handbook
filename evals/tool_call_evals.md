# Tool-call evals

Tests that the agent picks the right tool, with the right args, in the right order.

## Why this is hard

- The model can return *plausible-looking* tool calls that are wrong
- Order matters (search before fetch; validate before commit)
- Sometimes "no tool" is correct
- Tool *descriptions* affect selection — quietly tweaking one can shift behavior

## What to assert

| Assertion | Example |
|---|---|
| Specific tool was called | `assert any(span.name == "tool.web_search")` |
| Tool called with arg matching | `query` contains "alembic NOT NULL backfill" |
| Tool **not** called | `gh.pr.merge` never appears |
| Order constraint | `tool.web_search` precedes `tool.fetch_url` |
| Step count cap | `len(spans) <= 12` |
| Cost cap | `total_cost_usd <= 0.10` |

## Case shape

```jsonl
{"id":"tc-2026-04-12-001",
 "input":{"task":"Find current pnpm-vs-npm benchmarks"},
 "expected":{"must_call":["tool.web_search","tool.fetch_url"],
             "forbidden":["tool.write_file"],
             "order":[["tool.web_search","tool.fetch_url"]],
             "max_steps":8}}
```

## Building the dataset

Mine your traces. Successful real runs are great regression cases. Failed real runs (after fix) are great regression cases too.

## Tool-description tests

Run a "selection eval" where similar tools compete for selection:

- Two tools with overlapping purposes → ensure the model picks the more specific one
- A renamed tool → ensure traces still pick correctly post-rename
- An adversarial description → ensure the model resists biased descriptions
