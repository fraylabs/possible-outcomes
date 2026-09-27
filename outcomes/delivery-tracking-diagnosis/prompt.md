Analyze shipment delivery performance separately from tracking freshness and give me a short, evidence-backed operations brief.

Inputs I will provide:
- A CSV with shipment_id, promised_at, delivered_at, last_tracking_at. Empty values are unknown; timestamps include timezone offsets.
- Snapshot time: [AS_OF, including timezone].
- Tracking-staleness threshold: [HOURS, default 24].
- Whether promised_at is a contractual deadline or an estimate: [DEADLINE_TYPE].

First inspect columns and timestamp validity. Stop to ask about missing timezone or ambiguous deadline semantics instead of silently assuming. Preserve the raw input. Collapse only identical duplicate rows; quarantine conflicting rows for the same ID and show them in an exceptions table. Flag impossible/future observed timestamps. Future promised deadlines are allowed.

For each non-conflicting shipment calculate two independent fields:
1. delivery_late: for delivered shipments, delivered_at > promised_at; for open shipments, AS_OF > promised_at. Equality is not late. If promised_at is missing, unknown. Explain that open means no recorded delivery, not proven physically undelivered.
2. tracking_stale: on open shipments, AS_OF - last_tracking_at > threshold; equality is fresh. Missing event is unknown. For delivered shipments, not_applicable.

Do not make these mutually exclusive: a shipment can be late and stale. Keep unknown and not_applicable distinct from false. If timestamps fail validation, quarantine that ID, do not guess. Add a reason/evidence column per row.

Produce diagnosis.csv, exceptions.csv (even if empty), and a one-page brief.md. Summarize the four known combinations, missing/conflicting evidence, and denominator for every rate. Separate delivered and open populations where relevant. Include a compact verification script using the available runtime, with checks for duplicates, missing values, equality boundaries and an item that is BOTH late and stale. Run it and report actual results.

Finish with three prioritized internal follow-ups linked to shipment IDs, plus what this export cannot prove. Do not send messages, issue refunds or modify source systems. Do not invent causal explanations or convert estimated dates into contractual failure claims.
