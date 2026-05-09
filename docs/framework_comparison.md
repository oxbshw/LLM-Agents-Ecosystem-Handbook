# Agent framework comparison

Practical, vendor-neutral overview. The agent framework landscape moves monthly — **always verify against current upstream docs before betting a production system on a single framework.**

## At a glance

| Framework | Primary use | Lang | Orchestration | MCP | Tracing | Best for | Avoid when |
|---|---|---|---|---|---|---|---|
| **OpenAI Agents SDK** | Production agents | Py / JS | Loop + handoffs | ✅ | built-in | OpenAI / Anthropic with shim | Strict vendor neutrality |
| **LangGraph** | Stateful graphs | Py / JS | Graph | ✅ | LangSmith | Branching, long-running, checkpointed | Linear simple flows |
| **CrewAI** | Role-based teams | Py | Crew | ✅ | partner | Multi-agent role mental model | Pure single-agent |
| **AutoGen (AG2)** | Conversational MA + HITL | Py | Event-driven | partial | ✅ | Chat-style multi-agent + humans | Pipeline shapes |
| **LlamaIndex Workflows / Agents** | Data-first | Py / TS | Workflow | ✅ | ✅ | RAG-heavy, retrieval-driven | Pure orchestration without retrieval |
| **Pydantic AI** | Type-safe | Py | Loop | ✅ | Logfire | FastAPI-native, schema-first | Heavy dynamic flows |
| **Smolagents** | Code-loop minis | Py | Code-as-action | partial | basic | Quick automation | Complex multi-step orchestration |
| **Semantic Kernel** | Skills/plans, enterprise | C# / Py / Java | Plan | ✅ | ✅ | .NET / Microsoft ecosystem | Pure Python startups |
| **Haystack** | RAG-first | Py | Pipelines | partial | ✅ | NLP / RAG pipelines | Heavy tool-action agents |
| **DSPy** | Prompt optimization | Py | Module compilation | — | ✅ | Compiled prompts, eval-driven | Hand-tuned prompt iteration |
| **Strands Agents** | Provider-agnostic | Py | Loop | ✅ | OTEL native | Multi-provider, OpenTelemetry-first | Single-provider simple use |
| **Vercel AI SDK** | App-layer agents | TS / JS | Stream + tools | ✅ | ✅ | Next.js / app-integrated agents | Backend Python only |
| **Google ADK** | Hierarchical Gemini agents | Py | Tool tree | ✅ | ✅ | Gemini / Vertex first | Multi-vendor |

> Hedging note: framework features change frequently (especially around MCP and tracing). Treat the table as a starting point.

---

## Per-framework notes

### OpenAI Agents SDK
- **Use when**: you want a structured runtime with handoffs, guardrails, tracing, and tool calling out of the box. Anthropic and other providers usable through compatibility layers.
- **Avoid when**: you need provider-neutral abstractions baked in.

### LangGraph
- **Use when**: workflows have branching, loops, checkpoints, or need explicit graph reasoning. Pairs well with LangChain ecosystem.
- **Avoid when**: a linear loop will do — graphs are cognitive overhead.

### CrewAI
- **Use when**: the natural mental model is roles (planner, researcher, writer, reviewer).
- **Avoid when**: the workflow is single-agent; "crew" abstractions add weight.

### AutoGen (AG2)
- **Use when**: event-driven multi-agent conversations, especially with humans in the loop.
- **Avoid when**: pipeline / DAG structure matches better.

### LlamaIndex Workflows / Agents
- **Use when**: retrieval is central — heavy RAG, indexing, multi-source data.
- **Avoid when**: you need orchestration but don't have retrieval.

### Pydantic AI
- **Use when**: strict typed IO and tool signatures matter; FastAPI-native teams.
- **Avoid when**: dynamic, schema-light flows where Pydantic adds friction.

### Smolagents
- **Use when**: a small "agent writes code, executes, observes" loop is exactly the shape you need.
- **Avoid when**: you need durable orchestration, multi-agent, or careful safety primitives.

### Semantic Kernel
- **Use when**: enterprise / Azure / .NET, multilingual SDK matters.
- **Avoid when**: Python-only startups; community is smaller than LangChain/AutoGen.

### Haystack
- **Use when**: search + RAG pipelines are the main thing.
- **Avoid when**: heavy tool-using agents are the focus.

### DSPy
- **Use when**: you want prompts compiled from data and evals; reduces hand-tuning.
- **Avoid when**: simple, fast iteration on prompts is fine.

### Strands Agents
- **Use when**: you genuinely need to swap providers and want OpenTelemetry from day one.
- **Avoid when**: vendor-neutral isn't a real requirement — you'll trade community size.

### Vercel AI SDK
- **Use when**: agent UX lives inside a Next.js or React app.
- **Avoid when**: backend-only, Python-first stacks.

### Google ADK
- **Use when**: Gemini / Vertex first, hierarchical tool trees fit your problem.
- **Avoid when**: heavy multi-vendor needs.

---

## How to choose

```
Need vendor-neutrality?  ─ Yes ─►  Strands · LangGraph · Pydantic AI · OpenAI Agents SDK (with shim)
       │ No
       ▼
Heavy retrieval?          ─ Yes ─►  LlamaIndex Workflows · Haystack
       │ No
       ▼
Multi-agent roles?        ─ Yes ─►  CrewAI · AutoGen · LangGraph
       │ No
       ▼
TypeScript / app layer?   ─ Yes ─►  Vercel AI SDK
       │ No
       ▼
Default                          ►  OpenAI Agents SDK · LangGraph · Pydantic AI
```

## Common tradeoffs

| Tradeoff | Pick |
|---|---|
| Speed of iteration vs. structure | Smolagents / Vercel AI SDK ↔ LangGraph / Semantic Kernel |
| Simplicity vs. flexibility | Pydantic AI ↔ AutoGen |
| Vendor lock vs. ecosystem maturity | Strands ↔ OpenAI Agents SDK |
| Code-centric vs. config-centric | Smolagents ↔ CrewAI |

## What this comparison won't tell you

- Whether a particular framework version has a regression
- Which one is "best" — it depends on your stack and team
- Whether MCP support is *deep* or just *present*

Read upstream changelogs before adopting a major version.
