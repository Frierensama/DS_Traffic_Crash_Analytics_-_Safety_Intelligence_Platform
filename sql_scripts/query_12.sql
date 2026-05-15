use traffic_crash_analysis;

select * from traffic_crashes
limit 10; -- just to check column names

select
case 
when CRASH_HOUR between 6 and 11 then 'Morning'
when CRASH_HOUR between 12 and 16 then 'Afternoon'
when CRASH_HOUR between 17 and 20 then 'Evening'
else 'Night'
end as time_slot,
count(*) as injury_crashes
from traffic_crashes
where INJURIES_TOTAL > 0
group by time_slot
order by injury_crashes desc;