use traffic_crash_analysis;

select latitude, longitude, count(*) as total_frequency
from traffic_crashes_nfs
group by latitude, longitude
order by total_frequency desc
limit 5;