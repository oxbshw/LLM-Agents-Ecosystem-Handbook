# Memory safety checklist

Walk this before promoting episodic notes to semantic memory.

## Content
- [ ] No secrets / tokens / keys
- [ ] No PII unless explicitly allowed by policy
- [ ] No NDA-covered content without consent
- [ ] No raw transcripts (distil to learnings)

## Source
- [ ] Source tagged on each entry
- [ ] If source is external (web, MCP, RAG), human-confirmed before promotion
- [ ] If source is from another user / tenant — STOP, isolation breach

## Quality
- [ ] One fact per entry
- [ ] Dated `(YYYY-MM-DD)`
- [ ] Specific, not vague
- [ ] Verifiable

## Reconciliation
- [ ] Conflicts with existing entries resolved (update + outdated, not dual-state)
- [ ] No duplicates (search before adding)

## Diff hygiene
- [ ] Memory diff committed in git
- [ ] Diff message explains the session/source

## Eval
- [ ] Run [memory eval](../evals/memory_evals.md) on the new state
- [ ] Recall ≥ 95%, no-fab 100%, isolation 100%
