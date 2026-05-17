use traffic_crash_analysis;

select prim_contributory_cause, count(*) as total_crashes
from traffic_crashes_nfs
where crash_hour >= 18
group by prim_contributory_cause
order by total_crashes desc
limit 5;