use traffic_crash_analysis;

with cte as (
select street_name , count( case when injuries_total > 0 then 1 end ) as injury_crashes, count(*) as total_crashes
from traffic_crashes_nfs
group by street_name )
select street_name,  injury_crashes, total_crashes, round( injury_crashes * 100 / total_crashes, 2 ) as injury_rate
from cte
where total_crashes > 100
order by injury_rate desc
limit 5;
