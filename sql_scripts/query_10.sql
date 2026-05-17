use traffic_crash_analysis;

select year(crash_date) as crash_year , crash_type, count(*) as total_crashes,
row_number() over (partition by year(crash_date) order by count(*) desc ) as rnk
from traffic_crashes_nfs
group by crash_year, crash_type
)
select crash_year, crash_type , total_crashes
from cte
where rnk = 1
order by crash_year;
