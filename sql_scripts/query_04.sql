use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

-- with crashes_by_hour as (
-- select 
-- CRASH_MONTH, CRASH_HOUR, count(*) as crashes_total
-- from traffic_crashes
-- group by CRASH_MONTH, CRASH_HOUR
-- )
-- select * from crashes_by_hour;

with crashes_by_hour as(
select CRASH_MONTH, CRASH_HOUR, count(*) as total_crashes
from traffic_crashes
group by CRASH_MONTH, CRASH_HOUR
)
,
hours_ranked as (
select CRASH_MONTH, CRASH_HOUR, total_crashes, row_number() over ( partition by CRASH_MONTH order by total_crashes desc ) as rnk
from crashes_by_hour
)
select CRASH_MONTH, CRASH_HOUR as peak_crash_hour, total_crashes
from hours_ranked
where rnk = 1
order by CRASH_MONTH; 