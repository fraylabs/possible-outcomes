Build a weekly support workload and capacity plan from the files I attach. Produce calculations I can inspect and rerun, not a staffing recommendation.

Inputs:
- Planning week: [START_DATE inclusive], [END_DATE exclusive], timezone [TIMEZONE].
- Per queue: forecast new tickets, backlog tickets intended for this week, and average productive handling minutes per ticket.
- Available people: [COUNT]; productive support hours per person this week: [HOURS]. State whether productive hours already exclude meetings/breaks/other duties.
- Stress assumptions: new volume multiplier [default 1.5], handling-time multiplier [default 1.1].

Inspect inputs before calculating. Confirm a seven-day planning interval; if given a timestamped ticket log instead, aggregate using the explicit timezone and start-inclusive/end-exclusive boundary. Never count a forecast as observed demand. Remove exact duplicate queue records with a receipt, but stop and show conflicting duplicates. Require nonnegative numeric counts/time and positive capacity. Treat missing handling time as unknown, not zero. Do not invent estimates to complete a table.

For each queue and scenario calculate:
new demand = new tickets × volume multiplier × handling minutes × handling multiplier;
backlog demand = backlog tickets × handling minutes × handling multiplier;
capacity = people × productive hours × 60.
Base multipliers are 1. Stress changes new arrivals, not backlog count. Do not subtract meeting time again if productive hours already excludes it. Keep minutes as the common unit; round only display values. Clarify whether parallel chat handling is already reflected in the handling estimate rather than assuming it.

Deliver queue-breakdown.csv with demand by queue and scenario, scenarios.csv with total demand, capacity, utilization and demand-minus-capacity (positive means shortfall), plus a one-page capacity-brief.md. If any queue is unknown, label totals partial and report known demand as a lower bound; never call apparent headroom available. Show a sensitivity or break-even value for the missing estimate when meaningful. Include formulas, assumptions, excluded work, duplicate receipt and the dates covered.

Create and run a small reproducible calculation script. Verify at least one hand-calculated queue, units, exact duplicates, missing estimates and week-boundary handling if logs were supplied. Report what actually ran. End with the specific information needed to improve the plan and the limitations of weekly averages. Do not recommend hiring, firing, performance ratings or involuntary overtime, and do not modify schedules or contact staff.
