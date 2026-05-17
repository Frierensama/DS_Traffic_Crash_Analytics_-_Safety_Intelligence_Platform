use traffic_crash_analysis;

select
case when lighting_condition = 'DAYLIGHT' then 'Daylight' else 'Darkness' end as light_condition,
round ( avg(injuries_total), 2 ) as average_injuries
from traffic_crashes_nfs
where lighting_condition != 'UNKNOWN'
group by light_condition;
