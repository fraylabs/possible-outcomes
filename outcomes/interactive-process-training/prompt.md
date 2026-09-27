Build an offline branching practice page from the approved process supplied below. The deliverable is a self-contained `training.html` that a learner can open locally and use without an account or internet connection.

## Inputs I will supply

- PROCESS: approved rules, each with a stable source ID, version/date, priority or exception rules, and the exact allowed dispositions.
- SCENARIOS: fictional facts for at least three distinct cases: routine success, missing evidence, and an exception. Include the evidence that becomes visible after an initial check.
- AUDIENCE: role, language and assumed knowledge.
- BOUNDARIES: actions that must remain simulated; information the page must never collect or store.

Use the attached `sample-input.md` if I explicitly request the sample. Otherwise ask for missing inputs rather than substituting sample policies for my real process. If two supplied rules conflict without a priority rule, list the conflict and stop that branch until I resolve it. Never invent a policy, fee, approval, source ID or authority.

## Build

1. First make a compact decision table: scenario facts → required checks → allowed disposition → supporting source IDs. Distinguish facts from your explanatory copy. Identify any incomplete branches before coding.
2. Produce original HTML, inline CSS and inline JavaScript. Use semantic headings and native buttons, visible keyboard focus, readable contrast and a mobile-friendly layout. No external libraries, assets, fonts, fetches, tracking, cookies, storage or form submission. The file must work offline.
3. Give each scenario at least two meaningful steps: choose the initial check, then choose a disposition from plausible alternatives. Reveal evidence only after the appropriate check. Wrong choices must explain the relevant rule and allow retry without silently advancing. Correct choices must show a clearly labeled simulated result with source IDs. Do not reward unsupported shortcuts.
4. Include a scenario picker, progress text, restart, an accessible feedback region and a visible reference panel containing the supplied rules. Move focus appropriately when the current controls are replaced. Do not impose time limits. Do not collect names or claim certification.
5. Respect BOUNDARIES in both code and copy. A choice labeled “refer to lead” must remain a simulation, never a message or record update. Display “Practice only — no records updated.”

## Verify and deliver

Return `training.html`, the decision table and a short test report. Trace every possible choice in every scenario against the source IDs. Check wrong-answer retry, correct completion, switching scenarios, restart, keyboard-only use and narrow screens. Inspect the code for network calls and persistent storage. Test the page in a real browser if available; otherwise label those checks unperformed. State the model/tool actually used and any unresolved policy ambiguity. Do not claim this proves learner competence or compliance.

PROCESS / SCENARIOS / AUDIENCE / BOUNDARIES:
[Attach or paste the approved input document here.]
