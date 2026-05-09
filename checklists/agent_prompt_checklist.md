# Agent prompt checklist

Walk before merging a prompt change.

## Identity
- [ ] Role + mission + values present
- [ ] Output contract explicit (format + required + forbidden)
- [ ] Refusal style defined and consistent

## Length
- [ ] System prompt under ~1,500 tokens
- [ ] No bloat — every section earns its tokens

## Hierarchy
- [ ] System prompt explicitly treats tool / RAG / memory output as DATA, not instruction
- [ ] No bribe / threat tricks
- [ ] No "ignore future instructions" recursion

## Tools
- [ ] Tool discipline block present (narrow tool, fail loudly, approval gates)
- [ ] No tool schemas inlined that the harness already provides

## Memory
- [ ] User and project memory injected as **distilled, dated** facts
- [ ] No transcripts pasted in
- [ ] No PII / secrets in memory section

## Loop
- [ ] Max steps cap
- [ ] Repeat detection rule
- [ ] Cost-budget hint (when applicable)

## Versioning
- [ ] `version:` bumped if behavior changed
- [ ] Pinned model recorded with the prompt
- [ ] One-version rollback retained

## Evals
- [ ] Ran [evals/prompt_evals.md](../evals/prompt_evals.md)
- [ ] Critical refusals at 100%
- [ ] Quality not regressed
- [ ] Cost within budget

## Anti-pattern check (from [`prompt_engineering/anti_patterns.md`](../prompt_engineering/anti_patterns.md))
- [ ] Not a "constitution" (under 1,500 tokens)
- [ ] Positive guidance > negative
- [ ] No persona theater
- [ ] No magic prompts copied without test
- [ ] Refusal style consistent

## Date
- [ ] `Today's date is YYYY-MM-DD` line present (if time-sensitive)
