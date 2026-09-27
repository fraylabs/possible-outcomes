# Example verification

Executed 2026-09-27 with Node, for the supplied training.html:

- Inline JavaScript parses.
- Evaluated the pure `assess` function for three scenarios × two steps × three choices: 18 cases. Every choice matches the source decision table; incorrect choices retain the step and correct choices advance.
- Three completed-state checks retain completion.
- Every checked feedback string includes a rule ID.
- Static inspection found no external script/asset loading, fetch, XMLHttpRequest, WebSocket, browser storage, cookies, iframe or form.

Authoring/execution model: OpenAI GPT-6 Astra. No Opus model run. The checks do not measure model reliability or prove accessibility.

## Browser checks completed by the integrating owner

The following checklist describes the full suggested adaptation check; the exact checks performed are recorded below.

1. Open training.html locally. Choose the drop-off shortcut: explanation cites R1 and the first step remains visible.
2. Choose inspection, then normal completion: EQ-014 complete is shown. Restart resets the first step.
3. Pick Missing receipt. Inspect; try complete (rejected), then pending (accepted, EQ-022).
4. Pick Damaged return. Inspect; try complete and missing-record disposition (both rejected), then pending review (accepted, EQ-031).
5. Use only Tab, Shift+Tab and Enter/Space to select, answer and restart. Confirm visible focus and focus placement after a step change.
6. Open source rules. At a narrow viewport, verify choices and all text remain readable without horizontal scrolling.
7. Reload: progress must reset. Disconnect network: the already downloaded file must still run.

Chrome checked on September 27: all three correct outcomes; incorrect drop-off, missing-record completion and damaged completion retained their steps with source feedback. Tab/Enter completed the normal scenario and focus moved to the new heading. Reload reset progress. At 390 × 844, full-page visual inspection found readable wrapped controls and no horizontal overflow (scrollWidth = innerWidth = 390). Source rules now start expanded. These checks do not include a screen reader, a full keyboard-only journey, or a disconnected-network browser run; self-containment was checked by source inspection.
