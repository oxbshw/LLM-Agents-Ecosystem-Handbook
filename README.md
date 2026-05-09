<div align="center">

# LLM Agents Ecosystem Handbook

**A practical operating manual for building, evaluating, securing, and shipping modern LLM agent systems.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![LLM-Friendly](https://img.shields.io/badge/llms.txt-ready-blue.svg)](llms.txt)
[![Providers](https://img.shields.io/badge/providers-24%2B-blueviolet)](providers/README.md)

</div>

---

> Modern agents are not "a prompt + a tool." They are **systems** — with identity, memory, skills, tools, MCP integrations, guardrails, observability, evals, and a provider strategy. This handbook teaches the whole stack and ships templates, blueprints, runnable adapters, and curated examples you can adopt today.

## What's in this repo

A curated, opinionated, **production-oriented** handbook in seven parts:

1. **Concepts** — Agent OS, identity, memory, skills, MCP, safety, observability — every layer of the modern agent stack
2. **Provider ecosystem** — adapters + docs for **24+ LLM providers** (frontier APIs, fast inference, marketplaces, enterprise clouds, specialty, local runtimes), with a router for fallback chains
3. **Skills ecosystem** — design guide, taxonomy, maturity model, security checklist, and a curated skill catalog
4. **Prompt engineering** — agent prompt patterns, instruction hierarchy, context engineering, prompt-injection defense
5. **Coding-agent workflows** — for Claude Code, Cursor, Codex, Aider, Cline, and custom runtimes — repo instructions, prompts, review checklist, safe refactoring
6. **Design docs** — agent / technical design docs, ADR guide, design reviews, rollout plans, the `DESIGN.md` machine-readable spec
7. **Curated catalog** — 100+ existing agent skeletons, framework comparisons, evaluation tools, tutorials — preserved and improved

## Who this is for

| You are… | Start at |
|---|---|
| New to agents | [docs/beginners_guide.md](docs/beginners_guide.md) → [agent_os/README.md](agent_os/README.md) |
| Building a production agent | [blueprints/](blueprints/) → [checklists/production_readiness_checklist.md](checklists/production_readiness_checklist.md) |
| Picking / wiring providers | [providers/README.md](providers/README.md) → [providers/provider_matrix.md](providers/provider_matrix.md) |
| Comparing frameworks | [docs/framework_comparison.md](docs/framework_comparison.md) |
| Adding memory / RAG | [memory/](memory/) → [tutorials/rag_tutorials](tutorials/rag_tutorials) |
| Adding MCP | [mcp/](mcp/) → [mcp/mcp_security.md](mcp/mcp_security.md) |
| Designing Skills | [skills/](skills/) → [skills/skill_design_guide.md](skills/skill_design_guide.md) |
| Working with coding agents | [coding_agents/](coding_agents/) → [coding_agents/prompts/](coding_agents/prompts/) |
| Writing better prompts | [prompt_engineering/](prompt_engineering/) |
| Designing & rolling out | [design_docs/](design_docs/) |
| Hardening safety/evals | [safety/](safety/) → [evals/](evals/) |
| Coding agent reading this repo | [llms.txt](llms.txt) → [llm_wiki/index.md](llm_wiki/index.md) |

---

## Modern Agent Stack

| Layer | Purpose | Where in this repo |
|---|---|---|
| **Model / Provider** | LLM choice + abstraction + routing | [providers/](providers/) |
| **Orchestration** | Agent loops, planning, handoffs | [docs/framework_comparison.md](docs/framework_comparison.md), [blueprints/](blueprints/) |
| **Tool** | Function calling and external actions | [agent_os/mcp_layer.md](agent_os/mcp_layer.md) |
| **MCP** | Standardized external context and tools | [mcp/](mcp/) |
| **Memory** | Durable user/project/semantic memory | [memory/](memory/) |
| **Skills** | Reusable, progressive-loading workflows | [skills/](skills/) |
| **Identity** | Personality, mission, refusal style | [agent_os/agent_identity.md](agent_os/agent_identity.md), [templates/](templates/) |
| **Prompt** | System prompt design, instruction hierarchy, defenses | [prompt_engineering/](prompt_engineering/) |
| **Safety** | Guardrails, approvals, policy | [safety/](safety/) |
| **Observability** | Tracing, spans, cost, latency, evals | [observability/](observability/), [evals/](evals/) |
| **Deployment** | Shipping agents to production | [design_docs/rollout_plan.md](design_docs/rollout_plan.md) |
| **Coding-agent harness** | Claude Code, Cursor, Codex, Aider, Cline | [coding_agents/](coding_agents/) |

📖 Deep dive: [agent_os/README.md](agent_os/README.md)

---

## Provider ecosystem

The handbook ships an `LLMProvider` abstraction with **24+ providers** across six families. Most providers go through a single OpenAI-compatible code path; specialty / local providers are first-class.

| Provider type | Examples | Best for |
|---|---|---|
| **Frontier APIs** | OpenAI, Anthropic, Google Gemini | Reasoning, tool use, production agents |
| **Fast inference** | Groq, Cerebras, SambaNova | Low-latency workloads |
| **Marketplaces** | OpenRouter, Together, Fireworks, DeepInfra | Model choice and routing |
| **Enterprise clouds** | Azure OpenAI, AWS Bedrock, Vertex AI | Compliance, governance |
| **Specialty** | xAI, Perplexity, Mistral, Cohere, DeepSeek, Hugging Face, Replicate, NVIDIA NIM, MiniMax | Domain-specific |
| **Local runtimes** | Ollama, LM Studio, vLLM, llama.cpp | Privacy, cost control, offline dev |

Quick start:

```python
from utilities import get_provider
from utilities.provider_router import ProviderRouter

# Use any single provider
out = get_provider("groq").chat(
    [{"role": "user", "content": "Summarize MCP."}],
    model="llama-3.1-8b-instant",
)

# Or route by task class with fallback
router = ProviderRouter()
out = router.chat(messages, task_class="cheap")  # Groq → DeepSeek → Together → OpenRouter
```

📖 [providers/README.md](providers/README.md) • [providers/provider_matrix.md](providers/provider_matrix.md) • [providers/router_patterns.md](providers/router_patterns.md) • [providers/local_models.md](providers/local_models.md)

---

## Repository map

```
.
├── README.md • llms.txt • llms-full.txt
├── agent_os/                ← the Agent OS concept, layers, workspace examples
├── providers/               ← 24+ provider docs + adapters + router patterns
├── templates/               ← AGENTS.md / SOUL.md / MEMORY.md / SKILL.md / DESIGN_DOC / ADR / …
├── skills/                  ← design guide + taxonomy + maturity model + curated catalog + 4 examples
├── memory/                  ← memory taxonomy, distillation, security, examples
├── mcp/                     ← MCP basics, architecture, security, server catalog, examples
├── prompt_engineering/      ← agent prompt patterns, instruction hierarchy, defenses
├── coding_agents/           ← Claude Code, Cursor, Codex, workflows, prompts, review
├── design_docs/             ← agent + technical design docs, ADR guide, design.md spec
├── safety/                  ← guardrails, approvals, prompt injection, secure checklist
├── observability/           ← tracing, spans, cost/latency, dashboards
├── evals/                   ← eval design, regression / tool / memory / MCP / safety / prompt
├── blueprints/              ← production architectures by use case
├── examples/                ← end-to-end runnable agent workspaces
├── checklists/              ← agent design, prod readiness, MCP security, …
├── llm_wiki/                ← LLM-friendly index, glossary, matrices, wiki pattern
├── docs/                    ← framework comparison, best practices, beginners' guide
├── tutorials/               ← RAG, memory, fine-tuning, chat-with-X
├── utilities/               ← LLMProvider + router + provider_config
├── agents/                  ← 100+ curated agent skeletons (preserved)
├── complete_apps/, web_apps/, notebooks/, datasets/, design/, resources/, scripts/, tests/, ecosystem/
└── .github/                 ← issue / PR templates
```

---

## Skills ecosystem

A curated, in-repo catalog plus a clear taxonomy and maturity model:

- [skills/skill_design_guide.md](skills/skill_design_guide.md) — write triggers the model picks
- [skills/skill_vs_tool_vs_mcp.md](skills/skill_vs_tool_vs_mcp.md) — when to use which
- [skills/skill_taxonomy.md](skills/skill_taxonomy.md) — domains, tags, risk
- [skills/skill_maturity_model.md](skills/skill_maturity_model.md) — experimental → production
- [skills/skill_packaging.md](skills/skill_packaging.md) — ship a portable skill
- [skills/skill_validation.md](skills/skill_validation.md) — lint / smoke / eval
- [skills/awesome_skills_catalog.md](skills/awesome_skills_catalog.md) — broader ecosystem map
- [skills/catalog/](skills/catalog/) — index + per-domain skills
- [skills/examples/](skills/examples/) — four full reference skills

Curated skills shipped: research-summarizer, repo-auditor, mcp-security-reviewer, agent-memory-curator, api-design-reviewer, pr-summarizer, adr-writer, incident-postmortem, sprint-planner, dataset-profiler.

---

## Prompt engineering

A dedicated section, agent-focused:

- [prompt_engineering/agent_prompt_patterns.md](prompt_engineering/agent_prompt_patterns.md)
- [prompt_engineering/system_prompt_design.md](prompt_engineering/system_prompt_design.md)
- [prompt_engineering/instruction_hierarchy.md](prompt_engineering/instruction_hierarchy.md)
- [prompt_engineering/context_engineering.md](prompt_engineering/context_engineering.md)
- [prompt_engineering/tool_use_prompting.md](prompt_engineering/tool_use_prompting.md)
- [prompt_engineering/planning_and_reflection.md](prompt_engineering/planning_and_reflection.md)
- [prompt_engineering/memory_prompting.md](prompt_engineering/memory_prompting.md)
- [prompt_engineering/prompt_injection_defense.md](prompt_engineering/prompt_injection_defense.md)
- [prompt_engineering/prompt_eval_methods.md](prompt_engineering/prompt_eval_methods.md)
- [prompt_engineering/anti_patterns.md](prompt_engineering/anti_patterns.md)

Templates: [SYSTEM_PROMPT](templates/SYSTEM_PROMPT.md.template), [AGENT_PROMPT](templates/AGENT_PROMPT.md.template). Checklist: [agent_prompt_checklist](checklists/agent_prompt_checklist.md).

---

## Use this repo with coding agents

The handbook is *itself* a great surface for coding agents. Drop your favorite tool (Claude Code, Cursor, Codex, Aider, Cline) into the repo:

- [llms.txt](llms.txt) gives the agent an index in 30 seconds
- [coding_agents/](coding_agents/) has tool-specific notes + prompts
- [coding_agents/prompts/](coding_agents/prompts/) — repo audit, modernization, feature, bugfix, provider expansion, docs update, release review
- [templates/CODING_AGENT_TASK.md.template](templates/CODING_AGENT_TASK.md.template) — task contract template
- [templates/REPO_MODERNIZATION_PROMPT.md.template](templates/REPO_MODERNIZATION_PROMPT.md.template) — multi-phase modernization

The guidance is **tool-neutral**: same `AGENTS.md`, same workflows, regardless of harness.

---

## Design docs

Agent + technical design docs, ADRs, reviews, rollouts, and the `DESIGN.md` machine-readable spec for design tokens:

- [design_docs/agent_design_doc.md](design_docs/agent_design_doc.md)
- [design_docs/technical_design_doc.md](design_docs/technical_design_doc.md)
- [design_docs/adr_guide.md](design_docs/adr_guide.md)
- [design_docs/design_review.md](design_docs/design_review.md)
- [design_docs/rollout_plan.md](design_docs/rollout_plan.md)
- [design_docs/design_md_spec.md](design_docs/design_md_spec.md)
- [design_docs/examples/](design_docs/examples/) — research / MCP / memory / provider-router worked examples

Templates: [DESIGN_DOC](templates/DESIGN_DOC.md.template), [ADR](templates/ADR.md.template).

---

## Frameworks at a glance

| Framework | Best for | Lang | MCP | Tracing |
|---|---|---|---|---|
| OpenAI Agents SDK | Production agents | Py / JS | ✅ | ✅ built-in |
| LangGraph | Stateful, branching graphs | Py / JS | ✅ | ✅ LangSmith |
| CrewAI | Role-based teams | Py | ✅ | ⚠️ via partners |
| AutoGen (AG2) | Event-driven multi-agent + HITL | Py | ⚠️ partial | ✅ |
| LlamaIndex Workflows | Data-heavy / RAG-first | Py / TS | ✅ | ✅ |
| Pydantic AI | Type-safe, FastAPI-native | Py | ✅ | ✅ Logfire |
| Smolagents | Code-execution mini-agents | Py | ⚠️ | basic |
| Semantic Kernel | .NET / enterprise / Azure | C# / Py / Java | ✅ | ✅ |
| DSPy | Programmatic prompt optimization | Py | — | ✅ |
| Strands Agents | Provider-agnostic, OpenTelemetry | Py | ✅ | ✅ OTEL |
| Vercel AI SDK | App-layer agents in Next.js | TS / JS | ✅ | ✅ |
| Google ADK | Gemini / Vertex hierarchical tools | Py | ✅ | ✅ |

📖 Full comparison + decision tree: [docs/framework_comparison.md](docs/framework_comparison.md). Capability tags hedged: verify against current upstream docs.

---

## Skills, MCP, and Memory in one minute

- **Skills** are reusable, model-loaded *workflows* (`SKILL.md` + scripts + references). Use when a task is repeatable, multi-step, and benefits from progressive disclosure. → [skills/](skills/)
- **MCP** (Model Context Protocol) is a *standard* for exposing tools/context to any agent. Use when integrations should be reusable (GitHub, filesystem, browser, internal APIs). → [mcp/](mcp/)
- **Memory** is *durable state* across runs (`MEMORY.md`, vector stores, decision logs). → [memory/](memory/)

A useful rule of thumb:

| If the thing is… | Use |
|---|---|
| A repeatable workflow with steps and references | **Skill** |
| An external system with tools to call | **MCP** server |
| State that should outlive the current run | **Memory** |
| A single function the model needs once | Plain **tool** |

📖 Decision matrix: [skills/skill_vs_tool_vs_mcp.md](skills/skill_vs_tool_vs_mcp.md)

---

## Guardrails & safety

Production agents need risk-tiered tool controls and human approval gates for high-impact actions.

| Risk level | Examples | Approval |
|---|---|---|
| **Low** | read-only search, summarization | none |
| **Medium** | drafting files, creating tickets | sometimes |
| **High** | sending email, modifying repos, running shell | required |
| **Critical** | deleting data, spending money, changing permissions | always + audit |

📖 [safety/README.md](safety/README.md) • [safety/prompt_injection.md](safety/prompt_injection.md) • [safety/secure_agent_checklist.md](safety/secure_agent_checklist.md)

---

## Observability & evals

You cannot ship what you cannot measure. The handbook ships:

- A tracing primer ([observability/tracing.md](observability/tracing.md)) and span model ([observability/spans.md](observability/spans.md))
- Cost / latency / failure analysis playbooks
- Eval design + datasets ([evals/](evals/)): regression, tool-call, memory, MCP, safety, **prompt** evals
- A curated guide to [evaluation_frameworks](evaluation_frameworks/) — Promptfoo, DeepEval, RAGAs, Langfuse, Phoenix, TruLens, LangSmith, MLflow

---

## Templates (copy-paste ready)

| File | Purpose |
|---|---|
| [AGENTS.md](templates/AGENTS.md.template) | Repo-specific agent instructions |
| [SOUL.md](templates/SOUL.md.template) | Identity, voice, values, refusal style |
| [MEMORY.md](templates/MEMORY.md.template) | Durable project + user memory index |
| [USER.md](templates/USER.md.template) | User profile and preferences |
| [TOOLS.md](templates/TOOLS.md.template) | Allowed/restricted/approval-gated tools |
| [SKILL.md](templates/SKILL.md.template) | Skill spec with progressive loading |
| [MCP_SERVER.md](templates/MCP_SERVER.md.template) | Documenting an MCP integration |
| [SYSTEM_PROMPT.md](templates/SYSTEM_PROMPT.md.template) | Long-lived system prompt |
| [AGENT_PROMPT.md](templates/AGENT_PROMPT.md.template) | Per-task / per-session prompt |
| [DESIGN_DOC.md](templates/DESIGN_DOC.md.template) | Agent / technical design doc |
| [ADR.md](templates/ADR.md.template) | Architecture Decision Record |
| [EVAL_PLAN.md](templates/EVAL_PLAN.md.template) | What you'll evaluate and how |
| [GUARDRAILS.md](templates/GUARDRAILS.md.template) | Policy, refusals, escalation |
| [HUMAN_APPROVAL_POLICY.md](templates/HUMAN_APPROVAL_POLICY.md.template) | Who approves what |
| [CODING_AGENT_TASK.md](templates/CODING_AGENT_TASK.md.template) | Task contract for coding agents |
| [REPO_MODERNIZATION_PROMPT.md](templates/REPO_MODERNIZATION_PROMPT.md.template) | Multi-phase modernization |
| [AGENT_RELEASE_CHECKLIST.md](templates/AGENT_RELEASE_CHECKLIST.md) | Ship/no-ship gate |

---

## Merged knowledge areas (1.0.1)

This release **merged seven external projects** into the handbook. Each was adapted (not bulk-copied) into the structure above:

| Source theme | Lives in |
|---|---|
| Skills catalog + taxonomy patterns | [skills/](skills/) — taxonomy, maturity, packaging, validation, awesome catalog |
| Personal-wiki / self-maintaining KB | [llm_wiki/wiki_pattern.md](llm_wiki/wiki_pattern.md), [docs/llm_readable_docs.md](docs/llm_readable_docs.md) |
| Agent prompt research patterns | [prompt_engineering/](prompt_engineering/) |
| Production coding-agent prompts + workflows | [coding_agents/](coding_agents/) — prompts, workflows, review |
| Machine-readable design specs | [design_docs/design_md_spec.md](design_docs/design_md_spec.md), [templates/DESIGN_DOC.md.template](templates/DESIGN_DOC.md.template) |
| ADRs + design reviews | [design_docs/adr_guide.md](design_docs/adr_guide.md), [design_docs/design_review.md](design_docs/design_review.md) |

📖 Full migration plan: [MIGRATION_AND_PROVIDER_EXPANSION_PLAN.md](MIGRATION_AND_PROVIDER_EXPANSION_PLAN.md)

---

## Supported LLM providers

The [`utilities/llm_provider.py`](utilities/llm_provider.py) module exposes a single `LLMProvider` interface (and a backwards-compatible `complete()` function). Switch via `LLM_PROVIDER` without touching agent code; route automatically with [`ProviderRouter`](utilities/provider_router.py).

24+ providers across frontier / fast / marketplace / enterprise / specialty / local. See:

- [providers/provider_matrix.md](providers/provider_matrix.md) — capability comparison
- [providers/env_vars.md](providers/env_vars.md) — every variable
- [.env.example](.env.example) — copy-and-fill

---

## Contributing

Contributions are very welcome — new examples, framework updates, fixes, and translations all help. Start with:

- [CONTRIBUTING.md](CONTRIBUTING.md) — workflow, scope, quality bar
- [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)
- [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)
- [checklists/open_source_quality_checklist.md](checklists/open_source_quality_checklist.md)

## Roadmap & changelog

- [ROADMAP.md](ROADMAP.md) — what's next
- [CHANGELOG.md](CHANGELOG.md) — what shipped

## License

MIT — see [LICENSE](LICENSE).

## Maintainer

Curated & maintained by **Sayed Allam** ([oxbshw](https://github.com/oxbshw)). If this handbook helped you ship, please ⭐ the repo and open a PR with what *you* learned along the way.
