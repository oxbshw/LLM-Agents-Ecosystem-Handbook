# MCP evals

Treat MCP servers like external dependencies: pin them, eval them, and re-eval on bumps.

## Layers

### 1. Server contract evals
Does the server itself behave deterministically given the same inputs? Run against a recorded fixture or a sandbox.

```
GIVEN server github @ <SHA>
WHEN tools/call repos.get(owner=X, repo=Y)
THEN response matches schema vN
AND response.id == <expected>
```

### 2. Agent + server integration evals
Does the agent use the server correctly in realistic flows?

```jsonl
{"id":"mcp-gh-1",
 "input":{"task":"Open issue 'flaky test' in org/app"},
 "expected":{"must_call":["mcp.github.issues.create"],
             "args_match":{"repo":"org/app","title":"flaky test"},
             "approval_requested":true}}
```

### 3. Adversarial evals
Does the agent resist a misbehaving server?

- Server returns content trying to instruct the agent
- Server returns oversized output (truncation handling)
- Server returns ambiguous schema
- Server fails — agent should retry or surface, not fabricate

## On server bump

- Re-run all three layers
- Diff schemas; flag breaking changes
- Compare cost / latency vs previous version

## Don't skip

A passing server today is a compromised server tomorrow if you stop testing it.
