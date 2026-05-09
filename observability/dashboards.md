# Dashboards

What to put on the wall (or the daily Slack post).

## Reliability

- Success rate by task type (last 24h, 7d)
- Error rate by class
- Refusal rate (and which categories)
- Guardrail trip rate (which guardrails)

## Cost

- Cost per run p50 / p95 / max
- Cost per task type
- Daily total cost vs budget
- Top 10 most expensive runs

## Latency

- p50 / p95 / p99 total
- p95 model wait vs tool wait
- Slowest 10 runs in last 24h

## Approval / safety

- Approval requests per day by tool
- Approval grant / deny ratio
- Time-to-decision (human latency)
- Approvals per user (UX signal — too many = friction problem)

## Quality (eval-driven)

- Regression eval pass rate (per release)
- Tool-call eval pass rate
- Memory eval pass rate
- Safety eval pass rate

## Health rule of thumb

If any of these moves > 2σ from rolling average, page. If you don't have an alert for it, write one before shipping the next change.
