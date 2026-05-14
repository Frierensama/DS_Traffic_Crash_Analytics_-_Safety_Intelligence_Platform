use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select TRAFFIC_CONTROL_DEVICE, count(*) as total_count from traffic_crashes group by TRAFFIC_CONTROL_DEVICE;

with cte as (
select TRAFFIC_CONTROL_DEVICE, round ( avg( INJURIES_TOTAL ), 2 ) as average_injuries
from traffic_crashes
where TRAFFIC_CONTROL_DEVICE != 'UNKNOWN'
group by TRAFFIC_CONTROL_DEVICE
order by average_injuries desc
)
select TRAFFIC_CONTROL_DEVICE, average_injuries as average
from cte
limit 1;