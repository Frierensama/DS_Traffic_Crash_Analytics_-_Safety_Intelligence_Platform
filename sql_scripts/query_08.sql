use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select
LATITUDE, LONGITUDE, count(*) as crash_frequency
from traffic_crashes
group by LATITUDE, LONGITUDE
order by crash_frequency desc
limit 5;