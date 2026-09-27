# Weekly support demand and capacity

Planning interval: September 28, 2026 inclusive through October 5 exclusive (seven dates). Inputs are weekly forecasts, not counts derived from individual ticket timestamps. Capacity: 3 people × 20 productive hours × 60 = 3,600 minutes. Productive hours already exclude meetings, breaks and other work; no second shrinkage deduction was made.

| Scenario | Known new demand | Known backlog | Known total | Available | Known utilization | Demand minus capacity |
|---|---:|---:|---:|---:|---:|---:|
| Base | 2,640 min | 240 min | 2,880 min | 3,600 min | 80.0% | −720 min |
| Stress | 4,356 min | 264 min | 4,620 min | 3,600 min | 128.3% | +1,020 min |

Stress increases new volume by 50% and handling time by 10%; backlog count stays fixed but its handling time also increases. Calculations use decimal arithmetic, rounding only displayed percentages. These are workload scenarios, not measured performance.

## Missing evidence changes the conclusion

The specialist queue has 10 new tickets and 2 backlog tickets but no handling estimate. Its demand is excluded, never assumed zero. Therefore both totals/utilizations are partial lower bounds assuming nonnegative handling time, and the base case does not establish spare capacity. One identical email row was removed. Conflicting queue rows would halt the reference calculation.

For a specialist handling time m minutes, base demand is 2,880 + 12m. The base reaches capacity at m=60 minutes. Stress demand is 4,620 + 18.7m, so known demand already exceeds capacity by 17 productive hours even before specialist work.

## Next planning inputs

Obtain a representative specialist handling-time estimate, confirm the weekly volume forecast and check whether the 20 productive hours include all support work. Then rerun. Actual queue scheduling, service-level targets, skill routing, arrival peaks and parallel chat handling can change feasibility. No hiring, performance, overtime or staffing action is recommended or taken from this fixture.
