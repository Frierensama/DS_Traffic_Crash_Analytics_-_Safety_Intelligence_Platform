use traffic_crash_analysis;

select * from traffic_crashes limit 1;

select
round(LATITUDE, 2) as zone_latitude,
round(LONGITUDE, 2) as zone_longitude,
count(*) as total_crashes
from traffic_crashes
group by round(LATITUDE , 2) , round(LONGITUDE , 2)
order by total_crashes desc
limit 10;