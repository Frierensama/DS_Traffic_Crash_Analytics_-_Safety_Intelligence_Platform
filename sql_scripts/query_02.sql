use traffic_crash_analysis;

select street_name, count(*) as injury_crashes
from traffic_crashes_nfs
where injuries_total > 0
group by street_name
order by injury_crashes desc
limit 10;