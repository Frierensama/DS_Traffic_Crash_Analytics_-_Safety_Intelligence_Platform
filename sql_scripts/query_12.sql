use traffic_crash_analysis;

select 
case when crash_hour between 6 and 11 then 'Morning'
when crash_hour between 12 and 16 then 'Afternoon'
when crash_hour between 17 and 19 then 'Evening'
else 'Night' 
end as time_slot,
count( case when injuries_total > 0 then 1 end ) as injury_crashes
from traffic_crashes_nfs
group by time_slot
order by injury_crashes desc
limit 1;