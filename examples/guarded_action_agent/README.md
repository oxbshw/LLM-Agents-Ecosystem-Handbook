# Guarded action agent (example)

An agent whose every tool call passes through a single gateway that:

1. Validates the args against schema
2. Looks up the risk level
3. Asks for human approval if needed
4. Logs the call and outcome

## Files

- `TOOLS.md` — risk table
- `GUARDRAILS.md` — guardrail policy
- `HUMAN_APPROVAL_POLICY.md` — approval mechanics
- `runtime/guard.py` — the gateway (sketch below)
- `tests/eval_safety.jsonl` — adversarial cases

## Gateway (sketch, ~30 lines)

```python
RISK = {
    "search": "low",
    "read_file": "low",
    "write_file": "medium",
    "send_email": "high",
    "delete_repo": "critical",
}

def call(name: str, args: dict, ctx) -> dict:
    schema_validate(name, args)
    risk = RISK.get(name, "high")  # default-deny: unknown tools are high
    if risk in ("high", "critical"):
        approval = request_approval(name, args, dry_run=preview(name, args))
        if not approval.granted:
            log("denied", name, args, approval, ctx)
            return {"error": "denied"}
        if risk == "critical" and not approval.second_reviewer:
            log("denied_2nd", name, args, approval, ctx)
            return {"error": "denied (2nd reviewer)"}
    result = invoke(name, args)
    log("ok", name, args, result, ctx)
    return result
```

## Why "default-deny"

Unknown tools (added later, or names that look like tools but aren't registered) get treated as High. This prevents the model from inventing tool names that bypass the table.

## Eval

[`evals/safety_evals.md`](../../evals/safety_evals.md) — refusals, approvals, injection.

A passing safety suite must include cases where the model is *coerced* (via injection) into requesting Critical actions, and the gate refuses.
