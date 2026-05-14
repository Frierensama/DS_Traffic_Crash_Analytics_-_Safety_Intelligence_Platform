use traffic_crash_analysis;

with cte as (
select 
year(CRASH_DATE) as crash_year,
CRASH_TYPE,
count(*) as total_crashes,
row_number() over ( 
partition by year(CRASH_DATE)
order by count(*) desc
) as rnk
from traffic_crashes
group by year(CRASH_DATE), CRASH_TYPE
)
select 
crash_year, CRASH_TYPE, total_crashes
from cte
where rnk = 1
order by crash_year;
