# Memory prompting

How to *read* memory into a prompt and how to *write* memory from a session — without bloat or drift.

## Reading memory into the prompt

The model needs the right facts at the right time, not the entire memory.

```
WHAT YOU REMEMBER ABOUT THE USER (do not contradict):
  - {{distilled fact}} ({{date}})
  - {{distilled fact}} ({{date}})

WHAT YOU REMEMBER ABOUT THE PROJECT (do not contradict):
  - {{distilled fact}} ({{date}})
```

Rules:

- Inject only **dated, distilled** facts (not transcripts)
- Keep the load **bounded** — top-N by relevance, not "everything"
- Tag where each fact came from if it was sourced externally
- Phrase as facts, not orders ("user prefers terse" — not "always be terse")

## Selecting which memories to load

Three strategies:

| Strategy | Use when |
|---|---|
| **All of `MEMORY.md`** | The file is small (< 200 lines). Cheap, simple. |
| **Topic-filtered** | You can predict which topics the task touches. |
| **Embedding retrieval** | The memory store is large; retrieve top-K relevant. |

For most projects, all-of-`MEMORY.md` is fine until it isn't. Only graduate when it grows past the budget.

## Writing memory from a session

End-of-session distillation. Either prompted to the model, or done by a curator skill ([agent-memory-curator](../skills/examples/agent-memory-curator/SKILL.md)).

```
END-OF-SESSION MEMORY DISTILLATION

From today's session, identify facts that:
  - Apply beyond this session (not one-off)
  - Are confident (observed twice OR explicitly stated by user)
  - Are stable (unlikely to change next week)
  - Are useful (would change a future decision)

For each, output:
  - one line, dated YYYY-MM-DD
  - tagged: #user | #project | #decision | #feedback
  - supersedes: <existing entry if it conflicts>
```

Always **review** the model's proposed memory before promoting. The model is overconfident.

## Anti-patterns

- ❌ Pasting the entire chat as memory ("remember everything we talked about")
- ❌ Memory as a personality dump ("remember the user is a Capricorn")
- ❌ Letting external content auto-promote into memory (poisoning surface — see [memory/memory_security.md](../memory/memory_security.md))
- ❌ Storing secrets / tokens / PII in memory
- ❌ Re-stating memory in every prompt as if the model can't see it

## Memory + tool composition

When the user asks "what's our deploy time of day?":

1. The model checks memory first
2. If memory has the answer → use it (no tool call)
3. If not → search → answer → propose new memory

Without memory in the prompt, you'll re-run the search every time.

## Eval

See [evals/memory_evals.md](../evals/memory_evals.md). Three properties:

- **Recall** — given a fact in memory, the model uses it
- **No-fab** — without a fact in memory, the model doesn't invent it
- **Isolation** — user-A memory never surfaces for user-B
