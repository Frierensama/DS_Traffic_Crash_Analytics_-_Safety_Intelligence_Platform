use traffic_crash_analysis;

with cte as (
select
STREET_NAME,
count( case when INJURIES_TOTAL > 0 then 1 end ) as injury_crashes,
count(*) as total_crashes
from traffic_crashes
group by STREET_NAME
)
select 
STREET_NAME, injury_crashes, total_crashes, round(injury_crashes * 100 / total_crashes , 2 ) as injury_rate
from cte
where total_crashes > 100
order by injury_rate desc
limit 5;
