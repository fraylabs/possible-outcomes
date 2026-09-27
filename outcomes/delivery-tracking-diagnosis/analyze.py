#!/usr/bin/env python3
"""Reproduce the bundled synthetic example. Run from any directory."""
import csv
from datetime import datetime, timedelta
from pathlib import Path
BASE = Path(__file__).resolve().parent
AS_OF = datetime.fromisoformat('2026-09-27T12:00:00+00:00')
def dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')) if value else None
rows = list(csv.DictReader((BASE / 'sample/shipments.csv').open()))
unique = {}; duplicates = 0; conflicts = set()
for row in rows:
    key = row['shipment_id']
    if key in unique:
        if row == unique[key]: duplicates += 1
        else: conflicts.add(key)
    else: unique[key] = row
results = []
for key, row in unique.items():
    if key in conflicts:
        results.append(dict(shipment_id=key, delivery_late='unknown', tracking_stale='unknown', reason='conflicting records; reconcile source'))
        continue
    promise, delivered, event = map(dt, (row['promised_at'], row['delivered_at'], row['last_tracking_at']))
    if any(t and t > AS_OF for t in (delivered,event)):
        raise ValueError('Future observed event: ' + key)
    late = 'unknown' if promise is None else 'yes' if (delivered or AS_OF) > promise else 'no'
    stale = 'not_applicable' if delivered else 'unknown' if event is None else 'yes' if AS_OF-event > timedelta(hours=24) else 'no'
    reason = 'delivered; lateness compares delivery with promise' if delivered else 'open; lateness and tracking freshness are independent'
    if late == 'unknown' or stale == 'unknown': reason = 'missing timestamps; do not infer status'
    results.append(dict(shipment_id=key,delivery_late=late,tracking_stale=stale,reason=reason))
out = BASE/'example';out.mkdir(exist_ok=True)
with (out/'diagnosis.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(results[0]));writer.writeheader();writer.writerows(results)
with (out/'exceptions.csv').open('w', newline='') as f:
    writer=csv.DictWriter(f, fieldnames=['shipment_id','reason']);writer.writeheader()
    writer.writerows({'shipment_id': r['shipment_id'], 'reason': r['reason']} for r in results if 'unknown' in (r['delivery_late'], r['tracking_stale']))
by_id={r['shipment_id']:r for r in results}
assert len(results)==8 and duplicates==1 and conflicts=={'H'}
assert (by_id['A']['delivery_late'],by_id['A']['tracking_stale'])==('yes','yes')
assert (by_id['B']['delivery_late'],by_id['B']['tracking_stale'])==('yes','no')
assert (by_id['C']['delivery_late'],by_id['C']['tracking_stale'])==('no','yes')
assert (by_id['D']['delivery_late'],by_id['D']['tracking_stale'])==('no','no')
assert by_id['E']['tracking_stale']=='not_applicable' and by_id['E']['delivery_late']=='yes'
assert by_id['F']['delivery_late']=='unknown' and by_id['H']['delivery_late']=='unknown'
(out/'brief.md').write_text("""# Delivery and tracking diagnosis

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
""")
print('PASS: 8 IDs; independent states, exact thresholds, missing data and conflicting/identical duplicates verified')
