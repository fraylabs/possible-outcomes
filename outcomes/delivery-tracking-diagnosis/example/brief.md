# Delivery and tracking diagnosis

Snapshot: 2026-09-27 12:00 UTC. Stale means strictly more than 24 hours since the last tracking event on an open shipment. Due exactly now is not late. Promise timestamps are assumed to be contractual deadlines.

10 source rows → 8 shipment IDs. One identical duplicate removed; H has conflicting promises and is quarantined. No source files changed.

- A is late AND has stale tracking. Both issues deserve investigation.
- B is late with fresh tracking. Fresh tracking does not mean timely delivery.
- C has stale tracking but is not late yet. Check tracking before calling it a delivery failure.
- D is exactly at its promise and freshness thresholds: neither condition is true.
- E was delivered one hour late; tracking freshness no longer applies.
- F lacks the evidence needed for either classification.
- G is neither late nor stale.
- H requires source reconciliation; neither promise was silently chosen.

Three shipments are confirmed late (A, B, E). This is 3 of 6 evaluable IDs, not a complete fleet late rate. Two have stale tracking (A, C), among 5 evaluable open shipments. F and H remain unknown; E is excluded from tracking freshness.

Next actions: investigate delivery for A/B, tracking for A/C, obtain missing timestamps for F and reconcile H. These are draft internal follow-ups only; no customer message, refund or carrier action has been sent. The CSV cannot establish why a shipment was late or whether an absent delivery scan means the parcel is physically undelivered.
