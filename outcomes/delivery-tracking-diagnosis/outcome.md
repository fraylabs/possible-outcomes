# Diagnose late deliveries and stale tracking separately

Turn a shipment export into a per-shipment diagnosis and a short operations brief that distinguishes late parcels from stale tracking—even when both apply to the same parcel.

## What you get

A copyable analysis prompt, a synthetic CSV with eight shipment IDs, a reproducible Python analysis and a worked diagnosis. The sample includes an identical duplicate, conflicting promise dates, missing timestamps, a delivered-late parcel and exact time boundaries. No customer data is included.

## Try the example

Download `analyze.py` and `sample/shipments.csv` keeping that folder layout; run `python3 analyze.py`. It writes `example/diagnosis.csv`, `example/exceptions.csv` and `example/brief.md`. Use the prompt with your own export, an explicit snapshot/timezone and an agreed definition of the promise date. Python 3.10+ is sufficient; no packages or account credentials are needed for the example.

At the sample snapshot, A is both late and stale, B is late with fresh tracking, C has stale tracking before its deadline, and D is exactly at both thresholds. F and H remain unknown. The brief explains why 3 of 6 evaluable IDs being late is not a complete-fleet late rate.

## Inspiration and provenance

[Anthropic's September 22, 2026 Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5) includes Hex's account of investigating package lateness versus slow tracking. This original prompt turns that reported distinction into explicit, testable rules. The anecdote is inspiration, not independent proof of model performance.

## Verification and limits

GPT-6 Astra authored the prompt and example implementation and executed the bundled Python example via its tools. Assertions check independent classifications, equality boundaries, duplicate treatment and unknowns. This is a worked synthetic example, not an independent run of the published prompt against a new model. **The prompt has not been tested on Claude Opus 5.5; Claude compatibility is unverified.** The selected Claude product describes its intended workflow, not tested model provenance.

The export cannot prove physical delivery when scans are absent, carrier causality or entitlement to compensation. Production data needs privacy review and source-specific deadline semantics. It is an illustrative fixture implementation, not a general import validator.
