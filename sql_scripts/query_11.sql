use traffic_crash_analysis;

with cte as (
select crash_day_of_week, crash_hour, count(*) as crashes_per_hour
from traffic_crashes_nfs
group by crash_day_of_week, crash_hour
)
select crash_day_of_week, round( avg(crashes_per_hour), 2 ) as average_crashes_per_hour
from cte
group by crash_day_of_week
order by average_crashes_per_hour desc
limit 1;