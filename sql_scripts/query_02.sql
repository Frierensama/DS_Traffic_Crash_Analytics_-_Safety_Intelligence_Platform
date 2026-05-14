use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select
STREET_NAME , count(*) as injury_crash_count
from traffic_crashes
where INJURIES_TOTAL > 0
group by STREET_NAME
order by injury_crash_count desc
limit 10;
