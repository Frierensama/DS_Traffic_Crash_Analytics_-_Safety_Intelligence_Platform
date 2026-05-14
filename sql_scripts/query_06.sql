use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select lighting_condition, count(*) as total_count from traffic_crashes group by lighting_condition; -- checking unique lighting conditons

select 
case 
when LIGHTING_CONDITION = 'DAYLIGHT' then 'Daylight'
else 'Darkness'
end as Lighting_group,
round(avg(INJURIES_TOTAL) , 2 ) as average_injuries
from traffic_crashes
where LIGHTING_CONDITION != 'UNKNOWN'
group by lighting_group;
