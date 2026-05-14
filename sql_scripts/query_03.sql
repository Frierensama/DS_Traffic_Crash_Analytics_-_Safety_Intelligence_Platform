use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select
CRASH_TYPE, round( count(case when INJURIES_TOTAL > 0 then 1 end ) * 100 / count(*), 2 ) as percent_injury_for_type
from traffic_crashes
group by CRASH_TYPE
order by percent_injury_for_type desc;
