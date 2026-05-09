# Framework matrix

Cross-cutting view. **Verify against current upstream docs** — the ecosystem moves fast.

| Framework | Primary use | Lang | Orchestration | Tools | Memory | MCP | Tracing/Evals | Best for | Avoid when |
|---|---|---|---|---|---|---|---|---|---|
| OpenAI Agents SDK | Production agents | Py / JS | Loop + handoffs | ✅ | basic | ✅ | ✅ built-in | Production with OpenAI/Anthropic shim | Vendor-neutral hard reqs |
| LangGraph | Stateful graphs | Py / JS | Graph | ✅ | checkpointers | ✅ | ✅ LangSmith | Branching/long-running | Simple linear flows |
| CrewAI | Role-based teams | Py | Crew | ✅ | built-in | ✅ | ⚠️ via partners | Multi-agent, role mental model | Single-agent simplicity |
| AutoGen (AG2) | Conversational multi-agent | Py | Event-driven | ✅ | session | ⚠️ partial | ✅ | HITL, group conversations | Pure pipeline shapes |
| LlamaIndex Workflows | Data-first agents | Py / TS | Workflow | ✅ | ✅ | ✅ | ✅ | RAG-heavy | Pure orchestration without retrieval |
| Pydantic AI | Type-safe agents | Py | Loop | ✅ | basic | ✅ | ✅ Logfire | FastAPI-native, schema-first | Heavy dynamic flows |
| Smolagents | Code-loop mini agents | Py | Code-as-action | ✅ | basic | ⚠️ | basic | Quick automation | Complex multi-step orchestration |
| Semantic Kernel | Skills/plans, enterprise | C# / Py / Java | Plan | ✅ | ✅ | ✅ | ✅ | Microsoft / .NET stacks | Pure Python startups |
| Haystack | RAG-first apps | Py | Pipelines | ✅ | retrievers | partial | ✅ | NLP/RAG pipelines | Heavy tool-action agents |
| DSPy | Prompt optimization | Py | Module compilation | ✅ | — | — | ✅ | Compiled prompts, eval-driven | Hand-tuned prompt iteration |
| Strands Agents | Provider-agnostic | Py | Loop | ✅ | basic | ✅ | ✅ OTEL | Multi-provider, OpenTelemetry-native | Single-provider simplicity |
| Vercel AI SDK | App-layer agents | TS / JS | Stream + tools | ✅ | session | ✅ | ✅ | Next.js / app integrations | Backend-only Python stacks |
| Google ADK | Gemini hierarchical agents | Py | Tool tree | ✅ | basic | ✅ | ✅ | Gemini/Vertex first | Multi-vendor |

## How to choose

```
Need vendor-neutral?  ── Yes ──> Strands · LangGraph · Pydantic AI · OpenAI Agents SDK (with Anthropic shim)
            │ No
            ▼
Heavy retrieval?  ── Yes ──> LlamaIndex Workflows · Haystack
            │ No
            ▼
Multi-agent roles?  ── Yes ──> CrewAI · AutoGen · LangGraph
            │ No
            ▼
App integration?  ── Yes (TS) ──> Vercel AI SDK
            │ No
            ▼
Default ──> OpenAI Agents SDK · LangGraph · Pydantic AI
```

## Caveats

- "MCP support" varies by depth; many frameworks added it during 2025 — check current.
- "Tracing" varies from OTEL emit to integrated UI; many require a paid tier for full features.
- Production-readiness is a moving target. Verify version stability on the framework's release notes.
