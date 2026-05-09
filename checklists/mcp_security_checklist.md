# MCP security checklist

Walk this for every MCP server before connecting it.

## Source
- [ ] Repo identified, maintainer reputable
- [ ] Pinned to a specific commit / tag (no `latest`)
- [ ] License compatible with your usage
- [ ] No unexpected scripts in the repo (postinstall, etc.)

## Capabilities
- [ ] Every tool listed and risk-tiered (Low / Medium / High / Critical)
- [ ] Every resource URI documented
- [ ] No hidden tools (compare docs vs `tools/list` output)

## Permissions
- [ ] Tokens used by the server minimum-scope
- [ ] Filesystem allow-list (no `/`, no `~`)
- [ ] Network egress allow-list (or denied)
- [ ] Server runs as low-privilege user / sandboxed

## Output handling
- [ ] Output treated as untrusted (sanitization at boundary)
- [ ] Output truncated to a sane size
- [ ] Secret patterns redacted from output

## Approvals
- [ ] High tools gated (approval required)
- [ ] Critical tools gated (approval + 2nd reviewer)
- [ ] Approval mechanism out-of-band

## Observability
- [ ] Every call traced
- [ ] Per-tool cost + latency tracked
- [ ] Error rate alerted
- [ ] Audit log append-only

## Eval
- [ ] Contract evals against pinned version
- [ ] Adversarial output cases (instruction-laced output) covered
- [ ] Re-run on every server bump

## Operational
- [ ] Health check endpoint or process probe
- [ ] Circuit breaker if the server flaps
- [ ] Rollback to previous pinned version documented
