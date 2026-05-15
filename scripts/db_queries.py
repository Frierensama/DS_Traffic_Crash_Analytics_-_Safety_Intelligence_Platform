queries = {
    "1. Top 5 Dangerous Weather + Crash Type": """
    
    select 
    WEATHER_CONDITION , CRASH_TYPE , count(*) as total_crashes
    from traffic_crashes
    group by WEATHER_CONDITION , CRASH_TYPE
    order by total_crashes desc
    limit 5;

    """,

    "2. Top 10 Streets with Highest Injury Crashes": """

    select
    STREET_NAME , count(*) as injury_crash_count
    from traffic_crashes
    where INJURIES_TOTAL > 0
    group by STREET_NAME
    order by injury_crash_count desc
    limit 10;

    """,

    "3. Injury Percentage by Crash Type": """

    select
    CRASH_TYPE, round( count(case when INJURIES_TOTAL > 0 then 1 end ) * 100 / count(*), 2 ) as percent_injury_for_type
    from traffic_crashes
    group by CRASH_TYPE
    order by percent_injury_for_type desc;

    """,

    "4. Peak Crash Hour for Each Month": """

    with crashes_by_hour as(
    select CRASH_MONTH, CRASH_HOUR, count(*) as total_crashes
    from traffic_crashes
    group by CRASH_MONTH, CRASH_HOUR
    )
    ,
    hours_ranked as (
    select CRASH_MONTH, CRASH_HOUR, total_crashes, row_number() over ( partition by CRASH_MONTH order by total_crashes desc ) as rnk
    from crashes_by_hour
    )
    select CRASH_MONTH, CRASH_HOUR as peak_crash_hour, total_crashes
    from hours_ranked
    where rnk = 1
    order by CRASH_MONTH; 

    """,

    "5. Top 5 Night-Time Primary Crash Causes": """

    select
    PRIM_CONTRIBUTORY_CAUSE, count(*) as total_crashes
    from traffic_crashes
    where CRASH_HOUR >= 18
    group by PRIM_CONTRIBUTORY_CAUSE
    order by total_crashes desc
    limit 5;

    """,

    "6. Average Injuries: Daylight vs Darkness": """

    select 
    case 
    when LIGHTING_CONDITION = 'DAYLIGHT' then 'Daylight'
    else 'Darkness'
    end as Lighting_group,
    round(avg(INJURIES_TOTAL) , 2 ) as average_injuries
    from traffic_crashes
    where LIGHTING_CONDITION != 'UNKNOWN'
    group by lighting_group;

    """,

        "7. Traffic Control Device with Highest Average Injuries": """

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

    """,

    "8. Top 5 Crash Hotspots by Exact Coordinates": """

    select
    LATITUDE, LONGITUDE, count(*) as crash_frequency
    from traffic_crashes
    group by LATITUDE, LONGITUDE
    order by crash_frequency desc
    limit 5;

    """,

    "9. Top 5 Streets with Highest Injury Rate (>100 crashes)": """

    with cte as (
    select
    STREET_NAME,
    count( case when INJURIES_TOTAL > 0 then 1 end ) as injury_crashes,
    count(*) as total_crashes
    from traffic_crashes
    group by STREET_NAME
    )
    select 
    STREET_NAME, injury_crashes, total_crashes, round(injury_crashes * 100 / total_crashes , 2 ) as injury_rate
    from cte
    where total_crashes > 100
    order by injury_rate desc
    limit 5;

    """,

    "10. Most Common Crash Type Per Year": """

    with cte as (
    select 
    year(CRASH_DATE) as crash_year,
    CRASH_TYPE,
    count(*) as total_crashes,
    row_number() over ( 
    partition by year(CRASH_DATE)
    order by count(*) desc
    ) as rnk
    from traffic_crashes
    group by year(CRASH_DATE), CRASH_TYPE
    )
    select 
    crash_year, CRASH_TYPE, total_crashes
    from cte
    where rnk = 1
    order by crash_year;

    """,

    "11. Day with Highest Average Crashes Per Hour": """
    with cte as(
    select 
    CRASH_DAY_OF_WEEK, CRASH_HOUR,
    count(*) as total_crashes
    from traffic_crashes
    group by CRASH_DAY_OF_WEEK, CRASH_HOUR
    )
    select
    CRASH_DAY_OF_WEEK,
    round(avg(total_crashes), 2) as average_crashes
    from cte
    group by CRASH_DAY_OF_WEEK
    order by average_crashes desc
    limit 1;

    """,

    "12. High-Risk Time Slots (Morning/Afternoon/Evening/Night)": """

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

    """,

    "13. Top 3 Contributing Causes per Crash Type": """

    with cte as (
    select
    CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE, 
    count(*) as total_crashes,
    row_number() over (
    partition by CRASH_TYPE 
    order by count(*) desc
    ) as rnk
    from traffic_crashes
    group by CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE
    )
    select CRASH_TYPE, PRIM_CONTRIBUTORY_CAUSE, total_crashes
    from cte
    where rnk <=3
    order by CRASH_TYPE, rnk;

    """,

    "14. Year-over-Year Crash Growth Rate": """

    with cte1 as (
    select 
    year(CRASH_DATE) as crash_year,
    count(*) as total_crashes
    from traffic_crashes
    group by year(CRASH_DATE)
    ),
    cte2 as (
    select
    crash_year, total_crashes,
    lag(total_crashes) over (order by crash_year) as prev_year_crashes
    from cte1
    )
    select 
    crash_year, total_crashes, prev_year_crashes,
    round( (total_crashes - prev_year_crashes) * 100 / prev_year_crashes, 2  ) as crash_growth_rate
    from cte2
    order by crash_year;

    """,

    "15. Hotspot Zones (Rounded Coordinates)": """

    select
    round(LATITUDE, 2) as zone_latitude,
    round(LONGITUDE, 2) as zone_longitude,
    count(*) as total_crashes
    from traffic_crashes
    group by round(LATITUDE , 2) , round(LONGITUDE , 2)
    order by total_crashes desc
    limit 10;

    """
}
