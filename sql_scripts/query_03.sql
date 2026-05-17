use traffic_crash_analysis;

with cte as(
select crash_type, 
count(case when injuries_total > 0 then 1 end ) as injury_crashes, 
count(*) as total_crashes
from traffic_crashes_nfs
group by crash_type
)
select
crash_type,
round( injury_crashes * 100 / total_crashes, 2) as injury_crash_percent
from cte
order by injury_crash_percent desc;
