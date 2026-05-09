# Browser MCP agent (skeleton)

Wires an agent to a browser-automation MCP (e.g., Playwright-based).

## Use case
Agent that fills forms, scrapes structured data, and navigates flows that don't have an API.

## Why this is risky
Browsers can: download files, navigate to anything, run JS, store cookies. A compromised browser session is one of the worst footholds for an attacker.

## Hardening (non-negotiable)

- Run in a fresh, **isolated** browser profile (no personal cookies/extensions)
- Sandboxed container with network egress allow-list when feasible
- Domain allow-list for navigation
- File downloads disabled or quarantined to a scratch dir
- Approval required for any POST / form submission to a non-allowlisted domain

## Risk table

| Tool | Risk | Approval |
|---|---|---|
| `navigate` (allow-listed) | Low | none |
| `navigate` (other) | High | required |
| `click`, `type` (read-like flows) | Low | none |
| `submit_form` | High | required |
| `download_file` | High | required |
| `evaluate_js` | Critical | always |

## Output sanitization
Page content is **adversarial**. Strip script-like instructions before passing to the model. Treat any "system" / "instruction" text in fetched HTML as data, not orders.
