# Roadmap

A living plan. Issues + PRs welcome on any of these.

## Now (next 3 months)

- [ ] Fill out remaining MCP server docs in [mcp/examples/](mcp/examples/) with concrete configs
- [ ] Add a runnable safety eval harness with the dataset in [evals/examples/](evals/examples/)
- [ ] Reusable trace exporter recipe (OpenTelemetry → Langfuse / Phoenix)
- [ ] Blueprint: voice agent
- [ ] Blueprint: scheduled / cron agent
- [ ] Translation pass: ZH, ES, FR for top-level docs

## Next (3–6 months)

- [ ] Hosted demo for a Skill-enabled research agent
- [ ] Reference implementation of the guarded action gateway in Python and TypeScript
- [ ] Eval harness that generates a release report under `evals/runs/<release>/`
- [ ] Cross-tool `AGENTS.md` interop notes (Cursor, Claude Code, Codex, Aider)
- [ ] Memory store comparison with end-to-end latency / cost numbers
- [ ] More framework-specific deep dives (LangGraph + MCP, OpenAI Agents SDK + handoffs)

## Later (6+ months)

- [ ] Maturity model + scoring rubric for agent projects
- [ ] Curriculum: 8-week course from "first agent" to "production-grade"
- [ ] Annual "state of agents" report based on data here

## Won't do

- Become a vendor-marketing site
- Take undisclosed sponsorships for entries in the framework matrix
- Add CI badges that aren't real
- Add code that requires a paid service to even run

## How to influence the roadmap

- Open an issue with the `roadmap:` label
- Show up with a PR — concrete code/docs beats discussion
- Vote (👍) on existing roadmap issues
