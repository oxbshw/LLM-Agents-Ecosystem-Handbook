# Guarded tool agent (skeleton)

A documentation-first example of an agent with risk-gated tools.

## Idea
The same `gh` MCP tools, but every call goes through a guardrail layer.

## Pseudocode

```python
RISK = {
    "gh.repo.search": "low",
    "gh.issue.create": "medium",
    "gh.pull_request.create": "high",
    "gh.pull_request.merge": "high",
    "gh.repo.delete": "critical",
}

def call_tool(name, args, ctx):
    risk = RISK[name]
    validate_schema(name, args)
    if risk in ("high", "critical"):
        if not request_approval(name, args, dry_run=preview(name, args)):
            return refusal("denied")
    if risk == "critical":
        if not second_reviewer(name, args):
            return refusal("denied (2nd reviewer)")
    log_call(name, args, ctx)
    return mcp_invoke(name, args)
```

## Files in a real version

- `TOOLS.md` — risk table
- `GUARDRAILS.md` — guardrail policy
- `HUMAN_APPROVAL_POLICY.md` — approval mechanics
- `runtime/guard.py` — the wrapper above
- `runtime/approval.py` — out-of-band approval queue
- `tests/eval_safety.jsonl` — adversarial cases
