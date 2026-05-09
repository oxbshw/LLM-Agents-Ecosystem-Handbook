# LLM-readable documentation

Write docs LLMs can actually navigate. Same docs that humans read — but structured so a coding agent can pick the right file in 30 seconds.

## Why this matters

Coding agents (Claude Code, Cursor, Codex, Aider, Cline, custom runtimes) all have one thing in common: they read your repo, not your minds. A repo whose docs LLMs can navigate is one humans can navigate too.

## The five conventions

### 1. `llms.txt` at the root
A short, hand-curated index pointing at the most important docs. Each entry is a link + one sentence. If you have 1000 docs, list the 30 that matter.

```
> One-line repo description.

## Start here
- [README.md](README.md): overview
- [agent_os/README.md](../agent_os/README.md): the operating model

## Concepts
- ...
```

This handbook ships [`llms.txt`](../llms.txt) and a more complete [`llms-full.txt`](../llms-full.txt).

### 2. A wiki for the LLM
A small set of pages optimized for the LLM's reading patterns: tables, glossaries, decision trees. See [`llm_wiki/`](../llm_wiki/) — short pages, strong cross-links, no decorative prose.

### 3. Section anchors that match the user's question
Headings should answer questions, not abstract a topic. "How do I add a provider?" beats "Provider extension." LLMs match anchor text aggressively.

### 4. Tables for structured comparisons
LLMs read tables more reliably than prose for comparisons. When you have N options with M attributes, write a table.

### 5. Code blocks with language tags
Always tag the language (`python`, `bash`, `yaml`). Agents that auto-execute snippets depend on the tag.

## Anti-patterns

- ❌ Walls of prose explaining the obvious
- ❌ "See above" / "see below" — LLMs may not have "above" in context
- ❌ Marketing voice in technical docs
- ❌ Diagrams as PNGs without alt text — LLMs can't read them
- ❌ Burying the answer in a tutorial — agents searching for "how do I X" want the snippet

## Checklist

- [ ] `README.md` makes a 30-second first impression
- [ ] `llms.txt` exists at root
- [ ] Tables for every multi-row comparison
- [ ] Code blocks have language tags
- [ ] Headings phrased as questions or imperatives where natural
- [ ] No "see above"; cross-links use full anchors
- [ ] Internal links resolve

## How this handbook does it

- `README.md` opens with what / who / why and a stack table
- `llms.txt` and `llms-full.txt` index the repo for coding agents
- `llm_wiki/index.md` maps "task → which file to read"
- Every concept folder has a top-level `README.md` summarizing the section
- Glossary and matrices live in `llm_wiki/`

## Wiki pattern

For larger doc estates, see [`llm_wiki/wiki_pattern.md`](../llm_wiki/wiki_pattern.md) — automated personal/team wikis built from your own docs, with agent-readable pages.
