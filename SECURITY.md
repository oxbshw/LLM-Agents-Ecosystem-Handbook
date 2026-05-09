# Security policy

## Reporting a vulnerability

If you find a security issue in this handbook (e.g., an example that exposes a secret, a Skill that runs untrusted code without isolation, an MCP integration doc that recommends an unsafe configuration), please **do not** open a public issue.

Instead, email the maintainer or open a private security advisory via GitHub.

We aim to acknowledge reports within **5 business days** and ship a fix within **30 days** for high-severity issues, faster for actively exploitable ones.

## What counts as a security issue

This is a documentation repo, so the threats are mostly *guidance threats*:

- Examples that hardcode secrets
- Templates / Skills that recommend unsafe defaults
- MCP integration docs missing critical risk warnings
- Code samples vulnerable to injection / SSRF / arbitrary execution
- Outdated guidance that is now actively unsafe

## What's out of scope

- Vulnerabilities in third-party frameworks linked from the handbook (report upstream)
- Vulnerabilities in upstream MCP servers (report upstream)
- Personal preference about safety strictness (open a discussion instead)

## Scope of guidance

The handbook's safety guidance ([safety/](safety/), [checklists/](checklists/)) is intentionally **strict by default**. If you ship a system that follows it and still has an incident, please tell us — we'll fold the lesson back in.
