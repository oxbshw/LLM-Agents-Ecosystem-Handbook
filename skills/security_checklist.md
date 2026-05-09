# Skill Security Checklist

Skills can include scripts and references. Both are attack surfaces.

## Before adding a Skill to your workspace

- [ ] **Source reviewed** — read `SKILL.md`, all references, and all scripts
- [ ] **No hidden instructions** — no "ignore previous instructions" or jailbreak content in references
- [ ] **No outbound calls without need** — scripts shouldn't ping the internet without a reason
- [ ] **No secrets** — scripts must read keys from `.env`, not hard-coded
- [ ] **No destructive ops without approval** — scripts that delete / rm / drop need explicit gating
- [ ] **Inputs validated** — scripts should not blindly trust skill inputs
- [ ] **Sandboxed if possible** — run scripts in a locked-down env (no network, restricted FS) when feasible

## Skill-specific risks

| Risk | Example | Mitigation |
|---|---|---|
| Indirect prompt injection | A reference file contains "When you read this, also do X" | Treat references as data, not instruction; sanitize on load |
| Memory poisoning | Skill writes to `MEMORY.md` based on untrusted input | Promote via human or curator skill, not direct write |
| Tool over-reach | Skill calls `shell` for tasks a narrower tool would solve | Replace with narrowest tool; gate `shell` |
| Silent fallback | Skill returns "success" with degraded output | Add explicit success criteria; fail loudly |

## On commit
- [ ] Skill version bumped if behavior changed
- [ ] Test fixture exists for at least one path
- [ ] Reviewed by a second human if Skill calls high-risk tools
