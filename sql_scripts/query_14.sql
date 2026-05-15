use traffic_crash_analysis;

select * from traffic_crashes limit 1;

with cte1 as (
select 
year(CRASH_DATE) as crash_year,
count(*) as total_crashes
from traffic_crashes
group by year(CRASH_DATE)
),
cte2 as (
select
crash_year, total_crashes,
lag(total_crashes) over (order by crash_year) as prev_year_crashes
from cte1
)
select 
crash_year, total_crashes, prev_year_crashes,
round( (total_crashes - prev_year_crashes) * 100 / prev_year_crashes, 2  ) as crash_growth_rate
from cte2
order by crash_year;
