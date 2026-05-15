use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

with cte as(
select 
CRASH_DAY_OF_WEEK, CRASH_HOUR,
count(*) as total_crashes
from traffic_crashes
group by CRASH_DAY_OF_WEEK, CRASH_HOUR
)
select
CRASH_DAY_OF_WEEK,
round(avg(total_crashes), 2) as average_crashes
from cte
group by CRASH_DAY_OF_WEEK
order by average_crashes desc
limit 1;
