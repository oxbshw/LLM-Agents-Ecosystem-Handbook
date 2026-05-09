# Prompt patterns (LLM wiki view)

Compact map of agent prompt patterns. Full discussions in [`/prompt_engineering/`](../prompt_engineering/).

## Top patterns

| Pattern | When | Doc |
|---|---|---|
| Role + mission + values + output contract | Every agent prompt | [agent_prompt_patterns.md#1](../prompt_engineering/agent_prompt_patterns.md) |
| Plan-then-act | Multi-step, tool-using | [agent_prompt_patterns.md#2](../prompt_engineering/agent_prompt_patterns.md) |
| Reflection-after-step | Reduces silent failures, breaks loops | [planning_and_reflection.md](../prompt_engineering/planning_and_reflection.md) |
| Tool-use scaffolding | Models that overcall or miscall tools | [tool_use_prompting.md](../prompt_engineering/tool_use_prompting.md) |
| Output gate | Strict format compliance | [agent_prompt_patterns.md#5](../prompt_engineering/agent_prompt_patterns.md) |
| Refusal scaffold | Consistent decline shape | [agent_prompt_patterns.md#7](../prompt_engineering/agent_prompt_patterns.md) |
| Loop control | Cap steps, detect repeat | [agent_prompt_patterns.md#8](../prompt_engineering/agent_prompt_patterns.md) |
| Memory prompt block | Carry distilled facts | [memory_prompting.md](../prompt_engineering/memory_prompting.md) |

## Decision tree

```
Single-shot task?  ── Yes ──► no plan; lean prompt + output contract
       │ No
       ▼
Tool-using?        ── Yes ──► plan-then-act + tool-use scaffolding
       │ No
       ▼
Long task?         ── Yes ──► plan-then-act + reflection-after-step
       │ No
       ▼
Default ──► role + mission + values + output contract
```

## Anti-patterns (top 5)

1. The constitution (2,000-line system prompt)
2. Negative-only guidance
3. Persona theater
4. Bribe / threat tricks
5. Magic prompts copied without test

📖 [`prompt_engineering/anti_patterns.md`](../prompt_engineering/anti_patterns.md)
