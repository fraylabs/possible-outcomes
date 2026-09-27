#!/usr/bin/env python3
"""Calculate an explicitly incomplete weekly capacity scenario from synthetic inputs."""
import csv,json
from decimal import Decimal as D, ROUND_HALF_UP
from pathlib import Path
from datetime import date
BASE=Path(__file__).resolve().parent
a=json.loads((BASE/'sample/assumptions.json').read_text())
assert (date.fromisoformat(a['week_end_exclusive'])-date.fromisoformat(a['week_start'])).days==7
rows=list(csv.DictReader((BASE/'sample/queue-demand.csv').open())); unique={}; duplicates=0
for r in rows:
    if r['queue'] in unique:
        if unique[r['queue']] != r: raise ValueError('Conflicting queue rows: '+r['queue'])
        duplicates+=1
    else: unique[r['queue']]=r
capacity=D(str(a['people']))*D(str(a['productive_hours_per_person']))*60
assert capacity>0
unknown=[r['queue'] for r in unique.values() if not r['minutes_per_ticket']]
known=[r for r in unique.values() if r['minutes_per_ticket']]
result=[]; queue_results=[]
for scenario,volume,handling in [('base',D(1),D(1)),('stress',D(str(a['stress_new_volume_multiplier'])),D(str(a['stress_handling_minutes_multiplier'])))]:
    new=backlog=D(0)
    for r in known:
        n,b,m=map(D,(r['new_tickets'],r['backlog_tickets'],r['minutes_per_ticket']))
        assert min(n,b,m)>=0
        queue_results.append({"scenario":scenario,"queue":r["queue"],"new_minutes":str(n*volume*m*handling),"backlog_minutes":str(b*m*handling),"total_minutes":str((n*volume+b)*m*handling),"status":"known"})
        new+=n*volume*m*handling
        backlog+=b*m*handling
    total=new+backlog
    result.append({'scenario':scenario,'known_new_minutes':str(new),'known_backlog_minutes':str(backlog),'known_total_minutes':str(total),'capacity_minutes':str(capacity),'known_utilization_percent':str((100*total/capacity).quantize(D('.1'),rounding=ROUND_HALF_UP)),'known_gap_minutes':str(total-capacity),'status':'incomplete: missing handling time for '+','.join(unknown) if unknown else 'complete'})
for scenario in ('base', 'stress'):
    for queue in unknown:
        queue_results.append({'scenario':scenario,'queue':queue,'new_minutes':'','backlog_minutes':'','total_minutes':'','status':'unknown: missing handling time'})
out=BASE/'example';out.mkdir(exist_ok=True)
with (out/'scenarios.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(result[0]));w.writeheader();w.writerows(result)
with (out/'queue-breakdown.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(queue_results[0]));w.writeheader();w.writerows(queue_results)
assert len(queue_results)==6
assert duplicates==1 and unknown==['specialist'] and capacity==3600
assert D(result[0]['known_total_minutes'])==2880
assert D(result[1]['known_total_minutes'])==4620
assert D(result[1]['known_gap_minutes'])==1020
assert result[0]['known_utilization_percent']=='80.0'
(out/'capacity-brief.md').write_text("""# Weekly support demand and capacity

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
""")
print('PASS: exact demand/capacity arithmetic, seven-day interval, identical duplicate, missing estimate and stress sensitivity verified')
