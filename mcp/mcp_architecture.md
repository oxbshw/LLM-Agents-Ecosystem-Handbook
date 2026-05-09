# MCP architecture

## Components

```
┌────────────┐   JSON-RPC over stdio/SSE/HTTP    ┌─────────────┐
│   Client   │ <───────────────────────────────> │   Server    │
│ (agent)    │                                   │  (tools/    │
│            │                                   │   resources)│
└────────────┘                                   └─────────────┘
      │                                                 │
      ▼                                                 ▼
   model loop                                    real implementation
                                                  (FS, API, browser, …)
```

The protocol is a thin RPC layer — most of the work lives in your tool implementations.

## Message types

- `initialize` / `initialized` — handshake, capabilities
- `tools/list`, `tools/call`
- `resources/list`, `resources/read`, `resources/subscribe`
- `prompts/list`, `prompts/get`
- `notifications/*` — push events from server to client

## Transports

| Transport | Process model | When to use |
|---|---|---|
| **stdio** | Child of client | Local tools, dev loops |
| **HTTP streaming / SSE** | Separate process / hosted | Multi-user / remote services |

Both are full-duplex (the server can push notifications).

## Capabilities and discovery

A client should *always* gate on capabilities reported during `initialize`. Don't assume a server supports tool subscriptions or resource updates — check.

## State

Servers can be:

- **Stateless** (every call independent — easiest, safest)
- **Stateful** (sessions, subscriptions, long-running ops)

Prefer stateless when possible. Stateful adds complexity and a state-leak surface.

## Auth

The protocol itself doesn't mandate auth. Common patterns:

- **Local stdio** — trust the local user; pass tokens via env vars
- **Remote HTTP** — bearer tokens, OAuth, mTLS — implement at the transport layer

For per-user multi-tenant servers, build user identity into the auth handshake and scope every call.

## Versioning

The protocol is versioned. Pin both:
- The protocol version your client supports
- The server *implementation* version (commit SHA or tag)

Floating to "latest" is how supply-chain incidents start.
