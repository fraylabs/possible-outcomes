# Choose a Software Rollout from Conflicting Memos

Turn dated rollout notes into a defensible recommendation with hard gates, source citations, and explicit unresolved facts.

## Use it

Copy [the prompt](prompt.md) into your assistant and attach your dated source records. Replace the input placeholders, or attach [the synthetic sample](source-bundle.md) and use its decision/meeting context. Read [the worked output](decision-brief.md) and [its evidence index](evidence-index.json) to see the expected level of traceability. File-writing is optional: the prompt also requests saveable text blocks.

## What you receive

A decision brief comparing both options against explicit hard gates, explaining why the narrower pilot qualifies, and keeping the rollout approval separate from the recommendation. The sample contains a changed price, a failed rehearsal, an untested optimistic estimate, and an unapproved start date.

## Inspiration and provenance

Original Fray Labs prompt and synthetic example, authored September 27, 2026. Inspired by the document and communication workflows described in [Anthropic’s September 22 Opus 5.5 launch](https://www.anthropic.com/claude-opus-5-5) and the [September 25 work webinar](https://www.anthropic.com/webinars/opus-5-5-for-work). These sources motivate the task; they are not evidence that this prompt achieves a particular benchmark or works on every model.

A second inspiration is [Konstantin’s September 23 public post](https://x.com/kkttnjj/status/2102669194160492960), which reports checking 74 paper abstracts against a set of rules. That is the author’s unreplicated account. This outcome applies the broader idea of checking claims against supplied evidence to an original, non-medical software-rollout example; it does not reproduce or verify that post’s results.

## Verification and limits

The worked example was authored and executed in an OpenAI GPT-6 Astra agent session, then checked against the supplied synthetic source IDs and acceptance conditions. This is one worked example, not an independent rerun or a reliability benchmark. **Not tested on Claude Opus 5.5.** Claude is the intended product for reuse; its compatibility is untested. No private records or paid third-party prompts were used. Review real evidence and permissions before using a result operationally.
