# Turn support demand into a weekly capacity plan

Calculate how much support work fits into a week, compare a base and stress scenario, and make missing estimates visible before anyone relies on apparent spare capacity.

## What you get

An original copyable prompt, synthetic queue forecasts and assumptions, an inspectable scenario CSV, a one-page planning brief and a Python script that reproduces the example. The prompt accepts your own queue forecasts or a timestamped ticket log with explicit date boundaries.

## Try the example

Download `analyze.py`, `sample/queue-demand.csv` and `sample/assumptions.json`, preserving the folder layout. Run `python3 analyze.py` with Python 3.10+. It writes `example/scenarios.csv`, `example/queue-breakdown.csv` and `example/capacity-brief.md`; no additional packages are required.

The sample has 3,600 productive minutes of capacity. Known base demand is 2,880 minutes; stress demand is 4,620 minutes. A specialist queue lacks handling time, so neither total is complete. The brief shows that a 60-minute specialist handling estimate would consume all apparent base-case headroom. An identical duplicate email record does not double-count demand.

## Inspiration and provenance

[Anthropic's September 25, 2026 Opus 5.5 for work webinar](https://www.anthropic.com/webinars/opus-5-5-for-work) describes workflows connecting data analysis and collaborative documents. This independent example narrows that idea to a reusable support planning artifact. It does not reproduce a webinar prompt or claim that Anthropic demonstrated this exact calculation.

## Verification and limits

GPT-6 Astra authored the prompt and implementation and executed the bundled script through its tools. Assertions check scenario arithmetic, units, a seven-day interval, duplicate handling and explicit unknown demand. This is a deterministic synthetic worked example, not an independent end-to-end model benchmark. **Claude Opus 5.5 has not been tested; compatibility with its file/code workflow remains unverified.** Claude is the intended product, while the metadata identifies the model used for this artifact.

The sample uses weekly forecasts, so it verifies the interval length but does not exercise timestamped ticket aggregation. The included script reproduces this fixed fixture; it is not a general import validator. Weekly totals cannot establish service-level feasibility, account for arrival spikes or determine personnel decisions. Productive hours, handling-time measurement and routing constraints must come from the team using the plan.
