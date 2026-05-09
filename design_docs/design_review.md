# Design review

A design review meeting that improves the design — not a rubber-stamp ritual.

## Before the meeting

- [ ] Doc shared ≥ 24h in advance
- [ ] Author has marked open questions explicitly
- [ ] Reviewers come having *read* the doc
- [ ] Inline comments started; meeting is for the high-friction items only

## In the meeting (60 min max)

| Time | Activity |
|---|---|
| 0–5 | Author re-states goal + non-goals in 3 minutes |
| 5–15 | Reviewers ask the "is this even the right problem" questions |
| 15–35 | Walk the alternatives + the chosen path |
| 35–50 | Risks + rollout + open questions |
| 50–60 | Decide: accept / revise / re-review |

## Reviewer mindset

- **Steelman the alternative.** The strongest version of "why not the other path" is the most useful contribution.
- **Stay above implementation.** Don't bikeshed naming. Save that for the PR.
- **Surface assumptions.** "What if X is false?"
- **Care about the negative consequences.** "What's the worst quarter we'd have if this went sideways?"

## Author mindset

- **You are not your doc.** Reviewers attacking the doc are improving it.
- **Open questions are gifts.** Mark them honestly; reviewers will help.
- **One page of pre-reads beats one hour of presentation.**

## Outputs

- An updated doc (committed within ~2 days)
- A short decision: accepted / revise / re-review
- A list of follow-up issues if any

## Anti-patterns

- ❌ Pre-meeting "consensus" so the meeting is theater
- ❌ Reviewing in real-time without pre-reads
- ❌ Letting one loud reviewer dominate
- ❌ "Looks good" with no engagement (suggest "skipping" instead)
- ❌ Going over time — momentum dies; schedule a part 2

## When to NOT have a meeting

- Doc is small and the change is contained
- Async review surfaces all the same issues
- Author is genuinely senior and the change is reversible

A culture that defaults to async is healthier than one that defaults to meetings.
