# Migration & Provider Expansion Plan

> Plan for merging seven external projects into the **LLM Agents Ecosystem Handbook**, plus a major provider-abstraction expansion. Implemented in this same change.

## 0. Source projects inspected

| # | Source | Purpose | License | Action |
|---|---|---|---|---|
| 1 | `skillshub-main` | 12,900+ community Claude Code skills, federated by author/domain | not stated (community) | **Adapt** — taxonomy + curated examples, not bulk copy |
| 2 | `llm_wiki-main` | Tauri desktop app turning docs into self-maintaining knowledge graphs | GPLv3 | **Adapt** — pattern doc only, no GPL code copied |
| 3 | `agentic-ai-prompt-research-main` | 200+ system prompts, jailbreaks, agent-architecture research | not stated | **Adapt** — defensive patterns only; jailbreaks/leaks excluded |
| 4 | `antigravity-awesome-skills-main` | 1,420+ community skills with categorization | not stated | **Adapt** — taxonomy + curated examples |
| 5 | `claude-code-system-prompts-main` | 245 production agent/system prompts | not stated | **Adapt** — distil into ~10–15 reusable patterns |
| 6 | `design.md-main` | DESIGN.md format spec + reference CLI | Apache 2.0 | **Adapt** — spec + ADR pattern, not the CLI |
| 7 | `everything-claude-code-main` | Production harness: 48 agents, 183 skills, 79 commands, hooks | MIT | **Adapt** — subagent/hooks/skills patterns + curated examples |

## 1. Guiding principles

- **Adapt, don't dump.** Every imported piece must fit the handbook's voice, structure, and quality bar.
- **Stand-alone after migration.** No reference to `F:\New folder (3)\…` survives in the final repo.
- **Vendor-neutral.** Coding-agent guidance generalizes beyond Claude Code (Cursor, Codex, Aider, Cline).
- **No bulk-copy.** Where source repos have thousands of files, we ship a *taxonomy*, *catalog index*, *curation criteria*, and a small set of **high-quality concrete examples**.
- **Attribution by category.** When a pattern is widely-shared community knowledge (skills taxonomy, prompt design patterns), we describe the pattern. When a specific artifact is borrowed, we credit the source.
- **License safety.** GPLv3 source (`llm_wiki-main`) is NOT code-copied; only the *idea* is documented. Apache 2.0 (`design.md`) and MIT (`everything-claude-code`) content is freely adapted with attribution where appropriate.

## 2. Mapping: source → target

| Source | Target in main repo |
|---|---|
| `skillshub-main` skills index | `skills/catalog/`, `skills/awesome_skills_catalog.md`, `skills/skill_taxonomy.md` |
| `antigravity-awesome-skills-main` taxonomy | `skills/skill_taxonomy.md`, `skills/awesome_skills_catalog.md`, `skills/catalog/categories.md` |
| `llm_wiki-main` README + design | `llm_wiki/wiki_pattern.md`, `docs/llm_readable_docs.md`, expanded `llms.txt` / `llms-full.txt` |
| `agentic-ai-prompt-research-main` system-prompt patterns | `prompt_engineering/`, `templates/SYSTEM_PROMPT.md.template`, `templates/AGENT_PROMPT.md.template`, `safety/prompt_injection.md` (cross-link) |
| `claude-code-system-prompts-main` agent prompts | `coding_agents/prompts/`, `coding_agents/claude_code.md`, `templates/CODING_AGENT_TASK.md.template` |
| `everything-claude-code-main` harness | `coding_agents/` (workflows, repo_instructions, hooks-as-docs), `examples/agent_workspace_production/` |
| `design.md-main` spec | `design_docs/design_md_spec.md`, `templates/DESIGN_DOC.md.template`, `templates/ADR.md.template` |

## 3. Provider expansion (parallel work)

The original repo supported only OpenAI, Anthropic, MiniMax. We expand to **24+ providers** organized in five families.

### 3.1 Provider families

| Family | Members | Best for |
|---|---|---|
| Frontier APIs | OpenAI, Anthropic, Google Gemini | Reasoning, tool use, production |
| Fast inference | Groq, Cerebras, SambaNova | Low-latency, high-volume |
| Marketplaces | OpenRouter, Together, Fireworks, DeepInfra | Model choice, vendor neutrality |
| Enterprise | Azure OpenAI, AWS Bedrock, Google Vertex | Compliance, governance |
| Specialty | xAI, Perplexity, Mistral, Cohere, DeepSeek, Hugging Face, Replicate, NVIDIA NIM | Domain-specific |
| Local | Ollama, LM Studio, vLLM, llama.cpp, generic OpenAI-compatible | Privacy, cost, offline |

### 3.2 Architecture

```
utilities/
├── llm_provider.py         # generic LLMProvider interface + auto-detection
├── provider_router.py      # route by task class with fallback chains
├── provider_config.py      # capability metadata per provider
└── provider_errors.py      # typed error hierarchy
providers/
├── README.md
├── provider_matrix.md      # capability comparison table
├── provider_abstraction.md # design + interface contract
├── env_vars.md             # full env-var reference
├── local_models.md         # Ollama / LM Studio / vLLM / llama.cpp
├── router_patterns.md      # fast/cheap/reasoning/local/fallback patterns
├── cost_latency_matrix.md  # rough comparison (with caveats)
├── model_selection_guide.md
└── examples/
    └── {openai,anthropic,google,mistral,cohere,groq,together,fireworks,
          openrouter,deepseek,xai,perplexity,azure_openai,
          ollama,lmstudio,vllm}_provider.py + router_example.py
```

### 3.3 Capabilities tracked per provider

`chat`, `streaming`, `tool_calling`, `structured_outputs`, `json_mode`, `vision`, `embeddings`, `rerank`, `long_context`, `local`, `openai_compatible`.

### 3.4 Provider tiers (for routing)

- `default` — cheap, good
- `cheap` — minimum-cost summarization/classification
- `fast` — Groq/Cerebras for latency-sensitive
- `reasoning` — strongest tool/reasoning
- `long_context` — 200k+ context
- `vision` — multimodal
- `local` — privacy/offline
- `fallback` — chain when primary fails
- `embedding` / `rerank` — non-chat capabilities

## 4. New top-level structure (after migration)

```
.
├── README.md
├── llms.txt / llms-full.txt
├── docs/
├── agent_os/                ← unchanged (already from previous pass)
├── providers/               ← NEW
├── prompt_engineering/      ← NEW
├── coding_agents/           ← NEW
├── design_docs/             ← NEW
├── skills/                  ← expanded with catalog/, taxonomy, awesome catalog, maturity model
├── memory/                  ← unchanged
├── mcp/                     ← unchanged
├── safety/                  ← unchanged
├── observability/           ← unchanged
├── evals/                   ← extended with prompt_evals.md
├── blueprints/              ← unchanged
├── examples/                ← unchanged
├── templates/               ← extended with SYSTEM_PROMPT, AGENT_PROMPT, DESIGN_DOC, ADR, CODING_AGENT_TASK, REPO_MODERNIZATION_PROMPT
├── checklists/              ← extended with agent_prompt_checklist
├── tutorials/               ← unchanged
├── utilities/               ← provider files added
├── complete_apps/, web_apps/, notebooks/, datasets/, design/, resources/, ecosystem/, scripts/, tests/, agents/, evaluation_frameworks/  ← preserved
├── llm_wiki/                ← extended with wiki_pattern.md, prompt_patterns.md, coding_agent_guide.md, task_routing.md, provider_matrix.md
├── .github/                 ← unchanged
├── CONTRIBUTING.md / SECURITY.md / ROADMAP.md / CHANGELOG.md
├── MIGRATION_AND_PROVIDER_EXPANSION_PLAN.md   ← THIS FILE
└── (old: TRANSLATION.md, github/ legacy folder — preserved untouched)
```

## 5. What gets created

### From `skillshub-main` + `antigravity-awesome-skills-main`
- `skills/catalog/README.md` — curation philosophy
- `skills/catalog/index.md` — table of curated skills
- `skills/catalog/categories.md` — domain → skill mapping
- `skills/awesome_skills_catalog.md` — ecosystem of community skills (link-out, hedged)
- `skills/skill_taxonomy.md` — categories + tags + risk axes
- `skills/skill_maturity_model.md` — experimental → production
- `skills/skill_packaging.md` — how to ship a skill across tools
- `skills/skill_validation.md` — testing a skill
- `skills/catalog/<skill>/SKILL.md` — at least 6 high-quality curated skills representing top categories

### From `llm_wiki-main`
- `llm_wiki/wiki_pattern.md` — the personal-KB pattern (idea-only)
- `docs/llm_readable_docs.md` — how to write docs LLMs can navigate

### From `agentic-ai-prompt-research-main`
- `prompt_engineering/README.md`
- `prompt_engineering/agent_prompt_patterns.md`
- `prompt_engineering/system_prompt_design.md`
- `prompt_engineering/instruction_hierarchy.md`
- `prompt_engineering/context_engineering.md`
- `prompt_engineering/tool_use_prompting.md`
- `prompt_engineering/planning_and_reflection.md`
- `prompt_engineering/memory_prompting.md`
- `prompt_engineering/prompt_injection_defense.md`
- `prompt_engineering/prompt_eval_methods.md`
- `prompt_engineering/anti_patterns.md`
- `evals/prompt_evals.md`
- `templates/SYSTEM_PROMPT.md.template`
- `templates/AGENT_PROMPT.md.template`
- `checklists/agent_prompt_checklist.md`

### From `claude-code-system-prompts-main` + `everything-claude-code-main`
- `coding_agents/README.md`
- `coding_agents/claude_code.md`
- `coding_agents/cursor.md`
- `coding_agents/codex.md`
- `coding_agents/repo_instructions.md`
- `coding_agents/coding_agent_workflows.md`
- `coding_agents/safe_refactoring.md`
- `coding_agents/review_checklist.md`
- `coding_agents/prompts/repo_audit_prompt.md`
- `coding_agents/prompts/modernization_prompt.md`
- `coding_agents/prompts/feature_implementation_prompt.md`
- `coding_agents/prompts/provider_expansion_prompt.md`
- `coding_agents/prompts/bugfix_prompt.md`
- `coding_agents/prompts/docs_update_prompt.md`
- `coding_agents/prompts/release_review_prompt.md`
- `templates/CODING_AGENT_TASK.md.template`
- `templates/REPO_MODERNIZATION_PROMPT.md.template`

### From `design.md-main`
- `design_docs/README.md`
- `design_docs/agent_design_doc.md`
- `design_docs/technical_design_doc.md`
- `design_docs/adr_guide.md`
- `design_docs/design_review.md`
- `design_docs/rollout_plan.md`
- `design_docs/design_md_spec.md` — adapted format spec
- `design_docs/examples/research_agent_design.md`
- `design_docs/examples/mcp_agent_design.md`
- `design_docs/examples/memory_agent_design.md`
- `design_docs/examples/provider_router_design.md`
- `templates/DESIGN_DOC.md.template`
- `templates/ADR.md.template`

### Provider expansion
- `utilities/llm_provider.py` — rewritten with multi-provider, OpenAI-compatible default
- `utilities/provider_router.py` — routing/fallback engine
- `utilities/provider_config.py` — capability registry
- `utilities/provider_errors.py` — error hierarchy
- `providers/README.md`
- `providers/provider_matrix.md`
- `providers/provider_abstraction.md`
- `providers/env_vars.md`
- `providers/local_models.md`
- `providers/router_patterns.md`
- `providers/cost_latency_matrix.md`
- `providers/model_selection_guide.md`
- `providers/examples/<provider>_provider.py` × ~16
- `providers/examples/router_example.py`

## 6. What gets updated

- `README.md` — add Provider ecosystem, Skills ecosystem, Coding agents, Prompt engineering, Design docs, Merged knowledge sections
- `llms.txt` + `llms-full.txt` — point to the new sections
- `llm_wiki/index.md` + new matrices (`prompt_patterns.md`, `coding_agent_guide.md`, `task_routing.md`, `provider_matrix.md`)
- `tutorials/quickstart.md` — provider selection, env, new "use this with coding agents" section
- `.env.example` — add ~25 provider keys
- `CHANGELOG.md` — 1.0.1 entry
- `CONTRIBUTING.md` — call out the new sections + LLM-readable docs

## 7. What gets ignored / not imported

- All jailbreak / leak content from `agentic-ai-prompt-research-main`
- The Tauri / React desktop-app code from `llm_wiki-main` (GPLv3)
- All raw bulk skills from skillshub / antigravity (size + duplication; we provide taxonomy + curated subset)
- The `design.md` Bun CLI binaries (we ship the *spec*, not the tool)
- Internal/snapshot iterations of the same prompt across `claude-code-system-prompts-main`
- Per-author inner READMEs from skillshub (community attribution noise)

## 8. Risks

| Risk | Mitigation |
|---|---|
| GPLv3 license contamination from `llm_wiki-main` | We do not copy code; we describe the *pattern* in our own words |
| Stale prompt research aging poorly | We focus on patterns, not specific prompt strings |
| Provider examples requiring live keys to run | Each example is self-checking; raises clear "set X env var" message |
| Provider SDKs as heavy deps | All optional; OpenAI-compatible HTTP fallback for most |
| Bloating the repo with thousands of skills | Catalog + taxonomy + curated 6-skill core; rest documented as ecosystem |
| Coding-agent guidance becoming Claude-only | Each major doc has a "applies to Cursor / Codex / Aider / Cline" footer |

## 9. Quality gates (run at end)

- No reference to `F:\New folder (3)\` outside of THIS plan
- No external folder names appear in core docs (only in this plan and CHANGELOG)
- No `TODO` / `FIXME` / `lorem` / `placeholder` strings shipped
- No real API keys or secrets
- All new internal links resolve
- All new providers have an env var documented
- All new sections referenced from README + llms.txt

## 10. Implementation order

1. ✅ Plan (this file)
2. Provider abstraction + `providers/` (highest user value)
3. `prompt_engineering/`
4. `coding_agents/` + new templates
5. `design_docs/` + DESIGN_DOC / ADR templates
6. Skills expansion (catalog, taxonomy, maturity, awesome list)
7. `llm_wiki/` extensions
8. README + llms.txt + quickstart updates
9. CHANGELOG + .env.example
10. Quality pass

After this plan, the repo stands alone; no external folder is required.
