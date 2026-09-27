# Decision brief — support console rollout

As of **2026-09-27**, recommend **B, the limited pilot**, for Maya Chen's decision. B meets the stated gates in the supplied evidence; A fails the demonstrated rollback gate. Neither option is approved for rollout. [C1.1–C1.3, T1.1–T1.3]

## Hard gates

| Gate | A: all-team cutover | B: limited pilot |
| --- | --- | --- |
| Customer data stays in existing workspace | PASS for the documented configuration; both plans retain this boundary. [M1.1, T1.3] | PASS for the documented configuration. [M1.1, T1.3] |
| Demonstrated rollback within 15 minutes | FAIL: 18-minute rehearsal, 3 minutes over the limit. [C1.1, T1.1] | PASS: 11-minute rehearsal, 4 minutes under the limit. [C1.1, T1.2] |
| Approved incremental spend ≤ $500/month | PASS: $450/month approved contingent on selection. [C1.1, F1.1] | PASS: $180/month approved contingent on selection. [C1.1, F1.1] |

These passes concern the stated criteria and supplied records. The rehearsals used synthetic sessions; production rollback time remains unmeasured. [T1.3]

## Preferences and tradeoff

Fewer first-week staff-hours of disruption ranks before coverage. B is estimated at 12 versus A at 48: **36 fewer staff-hours** (48 − 12), an estimate rather than a measured saving. B reaches 12 staff versus A's 60, sacrificing **48 staff of first-week coverage** (60 − 12). B therefore also fits the higher-priority preference, while A would offer broader coverage if it became eligible. [C1.2, M1.1, M1.3, U1.1]

## Stale and conflicting evidence

- A's old $600/month estimate is superseded by the $450 quote and conditional approval. B's $180 amount is unchanged. [M1.2, F1.1]
- The earlier “rollback untested” status is superseded by the rehearsals. The suggestion of a 10-minute A rollback is unsupported by a new rehearsal and does not replace the 18-minute result. [M1.4, T1.1–T1.2, U1.3]
- October 1 is a proposed date, not an accepted start. [M1.4, U1.2]

## Questions and decision boundary

1. **Operations, individual unassigned:** Is support coverage available on the proposed October 1 date? No commitment or due date is recorded. This affects when a selected option can start. [U1.2]
2. **Owner not recorded:** Does a new rehearsal demonstrate A at or below 15 minutes? A could then become eligible, though the current disruption preference would still favor B. No optimization result is available. [C1.1–C1.2, U1.3]
3. **Owner not recorded:** How well do the synthetic rehearsals represent production rollback time? This could affect confidence in either option; production time is unknown. [T1.3]

**Next step:** Maya can accept or reject the B recommendation and request coverage confirmation before choosing a start date. This brief does not approve a rollout, buy licenses, or change any system. [C1.3, F1.1, U1.2]
