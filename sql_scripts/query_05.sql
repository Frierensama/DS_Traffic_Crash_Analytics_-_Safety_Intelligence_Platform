use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select
PRIM_CONTRIBUTORY_CAUSE, count(*) as total_crashes
from traffic_crashes
where CRASH_HOUR >= 18
group by PRIM_CONTRIBUTORY_CAUSE
order by total_crashes desc
limit 5;