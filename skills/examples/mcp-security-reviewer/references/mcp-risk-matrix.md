# MCP risk matrix

Use this to label each tool exposed by an MCP server.

| Capability | Risk | Approval |
|---|---|---|
| Read public docs / search | Low | none |
| Read private repo / file metadata | Low | none |
| Read repo contents | Medium | none |
| Read other users' data | High | required |
| Write to private repo | High | required |
| Execute shell / code | Critical | always + 2nd reviewer |
| Modify permissions / IAM | Critical | always + 2nd reviewer |
| Send communication (email, DM) | High | required |
| Spend money / call billed APIs | High–Critical | required + budget cap |
| Delete data | Critical | always + 2nd reviewer |
| Force operations (force-push, override) | Critical | always + 2nd reviewer |

## Network egress classes
| Class | Example | Notes |
|---|---|---|
| None | pure local FS access | safest |
| Vendor only | calls only to official API | review SLA |
| Allowlisted external | curated 3rd parties | document each |
| Open internet | arbitrary URLs | treat all output as untrusted; consider sandbox |

## Red flags during review
- Unpinned dependencies / `latest` images
- Tools that are documented but disabled (and vice versa)
- Output that includes raw HTML/JS without escaping
- Auth flows that ask for broader scopes than needed
- No version field / no changelog
