use traffic_crash_analysis;

with cte as (
select traffic_control_device, round( avg(injuries_total), 2 ) as average_injuries
from traffic_crashes_nfs
group by traffic_control_device
order by average_injuries desc
)
select traffic_control_device, average_injuries
from cte
limit 1;