# Changelog

All notable changes to this repository will be documented in this file.  The format is based on [Keep a Changelog](https://keepachangelog.com/), and
the project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.1] – 2026-05-10 — "Provider expansion + merged knowledge"

Expansion release on top of 1.0. Merged seven external projects' patterns into the handbook (adapted, not bulk-copied) and rewrote the provider abstraction to support 24+ providers across six families. The repo now stands alone — no external folders are required.

### Added

* **Provider ecosystem** ([providers/](providers/)): 24+ providers across frontier / fast inference / marketplaces / enterprise / specialty / local. Includes:
  * `LLMProvider` interface with capability registry ([utilities/provider_config.py](utilities/provider_config.py))
  * `ProviderRouter` with task-class chains and graceful fallback ([utilities/provider_router.py](utilities/provider_router.py))
  * Typed error hierarchy ([utilities/provider_errors.py](utilities/provider_errors.py))
  * Per-provider runnable adapters in [providers/examples/](providers/examples/)
  * Docs: provider matrix, abstraction design, router patterns, local models guide, env-var reference, cost/latency matrix, model selection guide
* **Skills ecosystem expansion** ([skills/](skills/)): taxonomy, maturity model, packaging guide, validation guide, awesome-skills ecosystem map, curated [catalog/](skills/catalog/) with index + categories, six new high-quality skills (api-design-reviewer, pr-summarizer, adr-writer, incident-postmortem, sprint-planner, dataset-profiler)
* **Prompt engineering section** ([prompt_engineering/](prompt_engineering/)): agent prompt patterns, system prompt design, instruction hierarchy, context engineering, tool-use prompting, planning + reflection, memory prompting, prompt-injection defense, eval methods, anti-patterns
* **Coding agents section** ([coding_agents/](coding_agents/)): tool-neutral guidance plus tool-specific notes (Claude Code, Cursor, Codex), repo instructions, workflows, safe refactoring, review checklist, and seven copy-paste prompts (repo audit, modernization, feature implementation, bugfix, provider expansion, docs update, release review)
* **Design docs section** ([design_docs/](design_docs/)): agent design doc, technical design doc, ADR guide, design review, rollout plan, DESIGN.md format spec, four worked examples (research / MCP / memory / provider router)
* **LLM-readable docs pattern** ([llm_wiki/wiki_pattern.md](llm_wiki/wiki_pattern.md), [docs/llm_readable_docs.md](docs/llm_readable_docs.md)) describing self-maintaining personal-wiki KBs and conventions for docs LLMs can navigate
* **New templates**: `SYSTEM_PROMPT.md`, `AGENT_PROMPT.md`, `DESIGN_DOC.md`, `ADR.md`, `CODING_AGENT_TASK.md`, `REPO_MODERNIZATION_PROMPT.md`
* **New checklist**: [agent_prompt_checklist.md](checklists/agent_prompt_checklist.md)
* **New eval suite doc**: [evals/prompt_evals.md](evals/prompt_evals.md)
* **LLM-wiki additions**: [provider_matrix.md](llm_wiki/provider_matrix.md), [prompt_patterns.md](llm_wiki/prompt_patterns.md), [coding_agent_guide.md](llm_wiki/coding_agent_guide.md), [task_routing.md](llm_wiki/task_routing.md), [wiki_pattern.md](llm_wiki/wiki_pattern.md)
* **MIGRATION_AND_PROVIDER_EXPANSION_PLAN.md** at repo root recording the 1.0.1 merge plan and source attributions

### Changed

* **`utilities/llm_provider.py`** rewritten as a multi-provider abstraction. Backwards-compatible `complete()` API preserved.
* **README** rewritten to surface the provider ecosystem, merged-knowledge sections, and expanded learning paths
* **`llms.txt`** and **`llms-full.txt`** updated to reflect all new sections
* **`.env.example`** expanded to 24+ providers + router-override variables
* **Quickstart** updated with provider selection, env setup, and the new "use this with coding agents" path
* **Skills README** restructured to point at the new catalog + concept documents

### Preserved

All existing agent skeletons, tutorials, evaluation_frameworks, complete_apps, utilities (alongside new files), web_apps, notebooks, datasets, design assets, ecosystem overview, and 1.0 docs.

## [1.0.0] – 2026-05-09 — "LLM Agents Operating System Handbook"

Major modernization. Repository repositioned from a curated catalog into a practical operating manual for modern LLM agent systems. All previous content preserved.

### Added

* **Agent OS section** ([agent_os/](agent_os/)) — concept docs and three example workspaces (minimal, research, coding)
* **Templates** ([templates/](templates/)) — `AGENTS.md`, `SOUL.md`, `MEMORY.md`, `USER.md`, `TOOLS.md`, `SKILL.md`, `MCP_SERVER.md`, `EVAL_PLAN.md`, `GUARDRAILS.md`, `HUMAN_APPROVAL_POLICY.md`, `AGENT_RELEASE_CHECKLIST.md`
* **Skills section** ([skills/](skills/)) — design guide, comparison vs tools/MCP, security checklist, four full Skill examples (research-summarizer, repo-auditor, mcp-security-reviewer, agent-memory-curator)
* **Memory architecture** ([memory/](memory/)) — taxonomy, distillation, episodic vs semantic, user vs project, security, examples
* **MCP** ([mcp/](mcp/)) — basics, architecture, server catalog, security, approval flows, vs function-calling, four agent examples
* **Safety** ([safety/](safety/)) — guardrails, human approval, tool risk levels, prompt injection, data exfiltration, secure-agent checklist, two example agents
* **Observability** ([observability/](observability/)) — tracing, spans, logging, cost, latency, failure analysis, dashboards
* **Evals** ([evals/](evals/)) — design, regression, tool-call, memory, MCP, safety; sample dataset and rubric
* **Blueprints** ([blueprints/](blueprints/)) — research, coding, customer support, data analysis, personal assistant, multi-agent team, RAG, MCP-first, secure-action
* **Examples** ([examples/](examples/)) — minimal/production workspaces; skill-enabled, memory-enabled, MCP-enabled, guarded, traced
* **Checklists** ([checklists/](checklists/)) — agent design, production readiness, MCP security, memory safety, skill quality, eval readiness, open-source quality
* **LLM-readable index** — [llms.txt](llms.txt), [llms-full.txt](llms-full.txt), [llm_wiki/](llm_wiki/) with index, glossary, agent stack, framework / memory / MCP / skills / safety matrices
* **Contributor experience** — refreshed [CONTRIBUTING.md](CONTRIBUTING.md), new [SECURITY.md](SECURITY.md), [ROADMAP.md](ROADMAP.md), [.github/](.github/) issue + PR templates
* **`.env.example`** at repo root for the provider abstraction

### Changed

* **README** rewritten as an operating-manual hero page with modern agent stack, learning paths, and full repo map
* **Framework comparison** ([docs/framework_comparison.md](docs/framework_comparison.md)) expanded to a 13-framework matrix with use-case decision tree and cautious hedging
* **Quickstart** ([tutorials/quickstart.md](tutorials/quickstart.md)) fixed (correct repo URL, current install, paths to new sections)
* **Beginner's guide** updated with pointers to the new sections

### Preserved

* All existing agent skeletons under [agents/](agents/)
* [docs/](docs/), [tutorials/](tutorials/), [evaluation_frameworks/](evaluation_frameworks/), [complete_apps/](complete_apps/), [utilities/](utilities/), [web_apps/](web_apps/), [notebooks/](notebooks/), [datasets/](datasets/), [design/](design/), [resources/](resources/), [ecosystem/](ecosystem/)

## [0.2.0] – 2025-09-06

### Added

* Created `web_apps` directory with `streamlit_summarizer` and `gradio_faq_bot` examples, including README and code.
* Added `datasets` directory with `sample_products.csv` and documentation.
* Added `design` directory containing `architecture_diagram.png` and a README explaining its purpose.
* Added Jupyter notebook scaffolding under `notebooks` (placeholder for future interactive demos).
* Introduced `docs/roadmap.md` outlining short, medium and long‑term goals.
* Added `CHANGELOG.md` to track project changes.

### Changed

* Updated `README.md` to reflect new categories, projects and documentation links.

## [0.1.0] – 2025-09-05

### Added

* Initial release with comparison of agent frameworks, evaluation framework guide, 30 example agent skeletons, contribution guidelines, code of conduct and
  generator script.