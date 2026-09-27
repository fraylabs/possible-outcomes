# Extract Decisions and Real Commitments from a Meeting

Convert a messy transcript and follow-up correction into a source-linked decision log and action draft without inventing owners, dates, or approval.

## Use it

Copy [the prompt](prompt.md) into your assistant and attach your dated source records. Replace the input placeholders, or attach [the synthetic sample](source-bundle.md) and use its decision/meeting context. Read [the worked output](follow-through.md) and [its evidence index](evidence-index.json) to see the expected level of traceability. File-writing is optional: the prompt also requests saveable text blocks.

## What you receive

A current decision log, accepted action table, unresolved-request queue, and unsent team-update draft. The sample deliberately includes a later scope correction, a retracted deadline, and suggestions that the proposed owners refused to accept.

## Inspiration and provenance

Original Fray Labs prompt and synthetic example, authored September 27, 2026. Inspired by the document and communication workflows described in [Anthropic’s September 22 Opus 5.5 launch](https://www.anthropic.com/claude-opus-5-5) and the [September 25 work webinar](https://www.anthropic.com/webinars/opus-5-5-for-work). These sources motivate the task; they are not evidence that this prompt achieves a particular benchmark or works on every model.

## Verification and limits

The worked example was authored and executed in an OpenAI GPT-6 Astra agent session, then checked against the supplied synthetic source IDs and acceptance conditions. This is one worked example, not an independent rerun or a reliability benchmark. **Not tested on Claude Opus 5.5.** Claude is the intended product for reuse; its compatibility is untested. No private records or paid third-party prompts were used. Review real evidence and permissions before using a result operationally.
