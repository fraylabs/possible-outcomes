# Synthetic equipment-return procedure

Purpose: teach a new desk coordinator how to triage loaned office equipment. All people, identifiers and rules here are fictional. This is practice, not an operational system.

## Approved rules (version 1, 2026-09-27)

- **R1 — Check first.** Before choosing a return status, inspect the item and check whether a loan receipt or matching loan record is available. Do not treat a drop-off alone as a completed return.
- **R2 — Normal return.** If the item is undamaged and a receipt or matching loan record is available, record the item ID and condition and mark the return complete.
- **R3 — Missing record.** If there is no receipt and no matching loan record, record the item ID and condition, mark the return pending, and ask the desk lead to locate the loan record. Do not mark complete.
- **R4 — Damaged item.** If damage is visible, record the item ID and damage, mark the return pending review, and refer it to the desk lead. This rule takes priority over R2 and R3. Do not assess a fee or promise a refund.
- **R5 — Practice boundary.** The training page must not update records, send messages, collect learner names or store progress. Referral actions appear only as simulated choices.

## Scenario facts

1. **Normal:** loaned monitor EQ-014; receipt present; casing and screen undamaged.
2. **Missing receipt:** loaned keyboard EQ-022; no receipt; loan lookup has no matching record; item undamaged.
3. **Damaged return:** loaned headset EQ-031; receipt present; ear cup visibly cracked.

## Delivery preferences

Audience: a new office equipment desk coordinator. Plain English; three short scenarios; no timer or leaderboard. One offline HTML file with inline CSS and JavaScript, usable with keyboard alone. Each scenario must require the learner to choose the initial check before revealing inspection/record facts, then choose the disposition. Incorrect choices explain the source rule and allow another attempt; correct choices show a simulated record. Include a restart button, scenario picker and visible source rules. No external assets, libraries, network requests or browser storage.
