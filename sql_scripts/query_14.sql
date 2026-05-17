use traffic_crash_analysis;

with cte1 as 
(
select year(crash_date) as crash_year, count(*) as total_crashes
from traffic_crashes_nfs
group by year(crash_date)
)
,
cte2 as (
select crash_year, total_crashes, lag(total_crashes) over ( order by crash_year) as prev_year_crashes
from cte1
)
select crash_year, total_crashes as curr_year_crashes, prev_year_crashes,
round ( (total_crashes - prev_year_crashes) * 100 / prev_year_crashes , 2) as crash_growth
from cte2
order by crash_year;
