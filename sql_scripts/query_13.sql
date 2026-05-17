use traffic_crash_analysis;

with cte as (
select crash_type, prim_contributory_cause, count(*) as total_crashes,
row_number() over (partition by crash_type order by count(*) desc ) as rnk
from traffic_crashes_nfs
group by crash_type, prim_contributory_cause
)
select crash_type, prim_contributory_cause as cause, total_crashes
from cte
where rnk <=3
order by crash_type, total_crashes desc;