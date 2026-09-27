# Five useful workday prompts

A small collection of original workflows prompted by the September 2026 discussion around Claude Opus 5.5. Start with a sample, inspect the result, then substitute your own authorized inputs.

| Outcome | What you get | Sample |
| --- | --- | --- |
| [Delivery and tracking diagnosis](outcomes/delivery-tracking-diagnosis/outcome.md) | Separate late deliveries from delayed tracking updates | Synthetic shipment exports |
| [Support demand and capacity](outcomes/support-demand-capacity-plan/outcome.md) | Reproducible base and stress scenarios | Synthetic ticket data |
| [Source-backed decision brief](outcomes/source-backed-decision-brief/outcome.md) | A recommendation with evidence, conflicts and open questions | Dated rollout memos |
| [Meeting decisions and follow-through](outcomes/meeting-decisions-followthrough/outcome.md) | Decisions and actual commitments separated from suggestions | Synthetic meeting notes |
| [Interactive process training](outcomes/interactive-process-training/outcome.md) | An offline branching practice exercise | Equipment-return procedure |

Each folder contains a copyable `prompt.md`, sample inputs, a worked output, prerequisites and verification limits. These are independent workflows; you do not need to run them in sequence. They use Possible's existing primary Product model (`anthropic/claude`), with actual example model provenance recorded separately.

## Model and verification

Anthropic announced **Claude Opus 5.5 on September 22, 2026**, with API identifier `claude-opus-5-5` and availability through Claude and supported platforms. See the [official release](https://www.anthropic.com/claude-opus-5-5) and [model page](https://www.anthropic.com/claude/opus). Availability is not proof of access in your account.

**These examples were authored and worked using GPT-6 Astra, not Opus 5.5.** We had no authorized Opus execution route for this assignment. Opus compatibility remains untested. The accompanying checks establish properties of these particular artifacts, not model reliability or a guaranteed repeatable generation. No benchmark or model superiority claim is made. Inspect each outcome's verification section before using it.

## Where the ideas came from

- [Shikhar, September 27](https://x.com/xikhar/status/2104001664793600012) shows a browser game and describes a third iteration with multiple tools. This suggested using interactivity for a modest training exercise. We did not copy the game, assets or prompt.
- [WebDevCody, September 26](https://x.com/webdevcody/status/2103653857377292720) describes a virtual office for agent work. This is inspiration for making a process tangible, not evidence that our training example integrates with agents.
- [Konstantin, September 23](https://x.com/kkttnjj/status/2102669194160492960) describes checking source claims and testing an app with synthetic data. This informed the collection's evidence and fixture discipline; his results are self-reported.
- [okeanskiy, September 27](https://x.com/okeanskiy/status/2104089404080066813) reports a disappointing game result and substantial quota use. Social demonstrations omit many conditions; we do not advertise these prompts as one-shot or low-cost.
- [Anthropic's launch article](https://www.anthropic.com/claude-opus-5-5) includes a Hex account of separating delivery trouble from tracking trouble, plus writing and research examples. Those are vendor-published reports, not our measurements.
- [Anthropic's September 25 work webinar](https://www.anthropic.com/webinars/opus-5-5-for-work) describes moving from analysis to usable documents. We chose small artifacts whose assumptions can be inspected.

All prompt wording and synthetic examples are original Fray Labs work. No third-party demo media or paid/private prompt text is included. Publication does not authorize uploading confidential workplace data to a model; use inputs you are permitted to process.
