use traffic_crash_analysis;

select * from traffic_crashes
limit 2; -- just to check column names

select 
WEATHER_CONDITION , CRASH_TYPE , count(*) as total_crashes
from traffic_crashes
group by WEATHER_CONDITION , CRASH_TYPE
order by total_crashes desc
limit 5;