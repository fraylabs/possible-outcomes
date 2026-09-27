# Turn a process into interactive practice

Give a new teammate a short, offline practice desk for an approved process. This prompt turns explicit rules and fictional cases into a branching HTML exercise with evidence, feedback and source IDs. The downloadable example teaches three equipment-return decisions without sending messages or updating records.

## Try the example

Download [training.html](./training.html) and open it in a browser. Choose an initial check, inspect the revealed facts, then choose a disposition. Incorrect choices explain the relevant rule and stay on the same step. Restart or switch scenarios at any time. The file contains its own styles and code and requires no installation or connection.

Use [sample-input.md](./sample-input.md) with the [copyable prompt](./prompt.md), or replace it with your own approved process. Supply source IDs, rule priorities, allowed dispositions, audience, fictional scenarios and the boundaries on what must stay simulated. Do not feed an unresolved or unapproved process into a training exercise and assume the result settles it.

## Example input → result

| Case | Evidence revealed after checking | Correct simulated result | Source |
| --- | --- | --- | --- |
| Normal | EQ-014 monitor; receipt; no damage | Record ID and condition, complete | R1, R2 |
| Missing receipt | EQ-022 keyboard; no receipt or matching record; no damage | Record ID and condition, pending; lead to find record | R1, R3 |
| Damaged return | EQ-031 headset; receipt; cracked ear cup | Record ID and damage, pending review; refer to lead, no fee | R1, R4 |

All cases begin with inspection and a receipt/record check. R4 takes priority over the other dispositions. No click performs the described operational action; no progress or learner data is stored (R5).

## Prerequisites and limits

- A model or coding agent that can create an HTML file, and a browser to open it.
- An approved, internally consistent source process. A knowledgeable process owner should check any adaptation before staff use it.
- The example is a synthetic office workflow, not safety, legal or compliance training. Completion is not proof of competence or certification.
- The sample uses native keyboard-operable buttons, visible focus and a live feedback region. Assistive-technology compatibility still needs testing with the intended audience.
- This is an original Fray prompt and implementation. It is not the source creators’ prompt or code.

## Inspiration and model provenance

[Shikhar’s September 27 interactive-game post](https://x.com/xikhar/status/2104001664793600012) describes a third iteration combining tools including Blender, image generation and Three.js. [Web Dev Cody’s September 26 virtual-office demo](https://x.com/webdevcody/status/2103653857377292720) is another example of an interactive environment in the recent model discussion. These are creator demonstrations, not controlled evidence that a single prompt produces a reliable app. This adaptation applies the interaction idea to a smaller reproducible task: practice from explicit source rules, with no third-party assets.

[Anthropic announced Claude Opus 5.5 on September 22, 2026](https://www.anthropic.com/claude-opus-5-5). The prompt targets Claude as a product, but this sample was authored and implemented with OpenAI GPT-6 Astra. No Opus 5.5 execution was performed or claimed. Compatibility with Opus 5.5 is untested.

## Verification

OpenAI GPT-6 Astra generated the prompt, synthetic fixture and HTML. Node parsed the script and checked all 18 initial-check/disposition choices plus three completed-state cases against the explicit expected transitions. Wrong answers remain on their current step; correct answers advance. Static inspection found no external loading, network calls, forms or persistent storage. This checks the supplied example, not arbitrary future model generations. See [verification.md](./verification.md) for the check boundary and browser checklist.
