use traffic_crash_analysis;

with cte as (
select crash_month, crash_hour, count(*) as total_crashes_per_hour, row_number() over (partition by crash_month order by count(*) desc ) as rnk
from traffic_crashes_nfs
group by crash_month, crash_hour
order by crash_month, rnk
)
select crash_month, crash_hour as peak_crash_hour, total_crashes_per_hour as total_crashes from cte
where rnk = 1;