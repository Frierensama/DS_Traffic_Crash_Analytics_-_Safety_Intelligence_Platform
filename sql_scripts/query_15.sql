use traffic_crash_analysis;

select round( latitude, 2 ) as zone_latitude , round (longitude, 2) as zone_longitude , count(*) as total_crashes
from traffic_crashes_nfs
group by round(latitude, 2), round(longitude, 2)
order by total_crashes desc
limit 10;