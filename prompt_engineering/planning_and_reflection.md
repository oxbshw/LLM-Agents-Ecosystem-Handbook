# Planning and reflection

Plan → act → reflect — applied with restraint.

## When planning helps

- Multi-step tasks (≥ 3 distinct actions)
- Tool-using flows where wrong tool choice is expensive
- Tasks where the user benefits from seeing the plan before execution

## When planning hurts

- One-shot tasks (a planning preamble adds cost without value)
- Tasks the user just wants done (planning becomes friction)
- Smaller / older models that degrade with planning prompts

Test, don't assume.

## The minimal plan-then-act prompt

```
PHASE 1 — PLAN:
  Read the task. Produce a numbered plan (3–7 steps).
  After the plan, STOP. Do not act yet.

PHASE 2 — ACT:
  Execute step <i>. Report what changed in 1–2 lines.
  After acting, return to step <i+1> until the plan is complete.
```

## Reflection patterns

### Per-step reflection

```
After each action:
  - Did this action succeed by my definition of success?
  - Did anything unexpected happen?
  - Update plan if needed.
```

### End-of-task reflection

```
Before declaring done:
  - Does the output match the contract?
  - Are there unsupported claims? Cite or remove.
  - What would I do differently next time? (one line)
```

### Reflection logging

Save the "what I'd do differently" line into your episodic log. Over weeks, those lines distill into real lessons (see [memory/episodic_memory.md](../memory/episodic_memory.md)).

## Anti-patterns

- ❌ Planning every trivial task. The plan can be longer than the work.
- ❌ Reflection theater — long monologues that don't change behavior. If the reflection doesn't change the next step, drop it.
- ❌ Plan-as-output when the user wanted action — match output to the user's actual ask.
- ❌ Letting the model edit its own plan freely each step — the plan stops being a plan.

## Tree-search variants

For very hard tasks, more elaborate patterns work:
- **Self-consistency**: sample multiple plans, pick the modal
- **Tree of thought**: branch on uncertain steps, score, pick the best

These are expensive. Use only when a regression eval shows they help.

## Plan quality

A good plan:
- Has 3–7 steps (more → split the task)
- Names tools where applicable
- Has explicit success criteria per step
- Identifies risks ("step 3 may fail if …")

A bad plan:
- Vague verbs ("understand", "explore")
- No tools mentioned
- Missing the obvious step
- Dependency-unclear

## Stop conditions

Plans should declare when to stop. A common failure: the model keeps planning after the work is done. Add a step: *"After step N, the answer is complete; return."*

## Cross-references

- [`agent_prompt_patterns.md`](agent_prompt_patterns.md) — pattern 2 + 3
- [`blueprints/multi_agent_team.md`](../blueprints/multi_agent_team.md) — planner / worker / reviewer split
- [`evals/eval_design.md`](../evals/eval_design.md) — measuring planning lift
