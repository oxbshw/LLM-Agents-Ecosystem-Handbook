# Prompt engineering

Practical patterns for system prompts, agent prompts, instruction hierarchies, tool-use prompting, planning + reflection, memory prompting, and prompt-injection defense. **Agent-focused** — not a general "tips and tricks" pile.

## What's here

| File | Purpose |
|---|---|
| [agent_prompt_patterns.md](agent_prompt_patterns.md) | The shapes that actually work for agent loops |
| [system_prompt_design.md](system_prompt_design.md) | Designing the long-lived system prompt |
| [instruction_hierarchy.md](instruction_hierarchy.md) | System > developer > user > tool — why it matters |
| [context_engineering.md](context_engineering.md) | What goes in context, in what order, and why |
| [tool_use_prompting.md](tool_use_prompting.md) | Getting the model to call tools well |
| [planning_and_reflection.md](planning_and_reflection.md) | Plan → act → reflect loops without the bloat |
| [memory_prompting.md](memory_prompting.md) | Reading/writing memory inside the prompt |
| [prompt_injection_defense.md](prompt_injection_defense.md) | Direct + indirect injection, mitigations (cross-ref [safety/](../safety/prompt_injection.md)) |
| [prompt_eval_methods.md](prompt_eval_methods.md) | Measuring prompt changes (cross-ref [evals/](../evals/)) |
| [anti_patterns.md](anti_patterns.md) | What not to do |

## Templates

- [/templates/SYSTEM_PROMPT.md.template](../templates/SYSTEM_PROMPT.md.template)
- [/templates/AGENT_PROMPT.md.template](../templates/AGENT_PROMPT.md.template)

## Checklist

- [/checklists/agent_prompt_checklist.md](../checklists/agent_prompt_checklist.md)

## North star

A good agent prompt:

1. Names the **role** in one sentence
2. States the **mission** (the *why*)
3. Lists **values** in priority order (so conflicts resolve consistently)
4. Defines the **output contract** (format + success criteria)
5. Treats external content as **data, not instruction**
6. Allocates context with intent — every section earns its tokens

Prompts that read like a constitution (hundreds of lines, every edge case) generally underperform prompts that read like a tight job description plus tools.

## Stance

This handbook treats prompt engineering as **engineering**: changes are versioned, eval'd, and rolled back if they regress. We're not collectors of clever phrasings — we test what works and ship what we can defend.
