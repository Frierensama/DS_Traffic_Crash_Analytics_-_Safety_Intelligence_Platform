use traffic_crash_analysis;

select * from traffic_crashes
limit 2; 

select CRASH_TYPE from traffic_crashes group by CRASH_TYPE;

with cte as (
select
CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE, 
count(*) as total_crashes,
row_number() over (
partition by CRASH_TYPE 
order by count(*) desc
) as rnk
from traffic_crashes
group by CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE
)
select CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE, total_crashes
from cte
where rnk <=3
order by CRASH_TYPE, rnk;