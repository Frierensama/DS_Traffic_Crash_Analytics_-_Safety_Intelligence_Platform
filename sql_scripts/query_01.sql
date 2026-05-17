use traffic_crash_analysis;

select weather_condition, crash_type, count(*) as total_crashes
from traffic_crashes_nfs
where weather_condition != 'UNKNOWN'
group by weather_condition, crash_type
order by total_crashes desc
limit 5;