queries = {
    "1. Top 5 Dangerous Weather + Crash Type": """

    select weather_condition, crash_type, count(*) as total_crashes
    from traffic_crashes_nfs
    where weather_condition != 'UNKNOWN'
    group by weather_condition, crash_type
    order by total_crashes desc
    limit 5;

    """,

    "2. Top 10 Streets with Highest Injury Crashes": """

    select street_name, count(*) as injury_crashes
    from traffic_crashes_nfs
    where injuries_total > 0
    group by street_name
    order by injury_crashes desc
    limit 10;

    """,

    "3. Injury Percentage by Crash Type": """

    with cte as(
    select crash_type, 
    count(case when injuries_total > 0 then 1 end ) as injury_crashes, 
    count(*) as total_crashes
    from traffic_crashes_nfs
    group by crash_type
    )
    select
    crash_type,
    round( injury_crashes * 100 / total_crashes, 2) as injury_crash_percent
    from cte
    order by injury_crash_percent desc;

    """,

    "4. Peak Crash Hour for Each Month": """

    with cte as (
    select crash_month, crash_hour, count(*) as total_crashes_per_hour, row_number() over (partition by crash_month order by count(*) desc ) as rnk
    from traffic_crashes_nfs
    group by crash_month, crash_hour
    order by crash_month, rnk
    )
    select crash_month, crash_hour as peak_crash_hour, total_crashes_per_hour as total_crashes from cte
    where rnk = 1;

    """,

    "5. Top 5 Night-Time Primary Crash Causes": """

    select prim_contributory_cause, count(*) as total_crashes
    from traffic_crashes_nfs
    where crash_hour >= 18
    group by prim_contributory_cause
    order by total_crashes desc
    limit 5;

    """,

    "6. Average Injuries: Daylight vs Darkness": """

    select
    case when lighting_condition = 'DAYLIGHT' then 'Daylight' else 'Darkness' end as light_condition,
    round ( avg(injuries_total), 2 ) as average_injuries
    from traffic_crashes_nfs
    where lighting_condition != 'UNKNOWN'
    group by light_condition;

    """,

    "7. Traffic Control Device with Highest Average Injuries": """

    with cte as (
    select traffic_control_device, round( avg(injuries_total), 2 ) as average_injuries
    from traffic_crashes_nfs
    group by traffic_control_device
    order by average_injuries desc
    )
    select traffic_control_device, average_injuries
    from cte
    limit 1;

    """,

    "8. Top 5 Crash Hotspots by Exact Coordinates": """

    select latitude, longitude, count(*) as total_frequency
    from traffic_crashes_nfs
    group by latitude, longitude
    order by total_frequency desc
    limit 5;

    """,

    "9. Top 5 Streets with Highest Injury Rate (>100 crashes)": """

    with cte as (
    select street_name , count( case when injuries_total > 0 then 1 end ) as injury_crashes, count(*) as total_crashes
    from traffic_crashes_nfs
    group by street_name )
    select street_name,  injury_crashes, total_crashes, round( injury_crashes * 100 / total_crashes, 2 ) as injury_rate
    from cte
    where total_crashes > 100
    order by injury_rate desc
    limit 5;

    """,

    "10. Most Common Crash Type Per Year": """

    with cte as
    (
    select year(crash_date) as crash_year , crash_type, count(*) as total_crashes,
    row_number() over (partition by year(crash_date) order by count(*) desc ) as rnk
    from traffic_crashes_nfs
    group by crash_year, crash_type
    )
    select crash_year, crash_type , total_crashes
    from cte
    where rnk = 1
    order by crash_year;

    """,

    "11. Day with Highest Average Crashes Per Hour": """

    with cte as (
    select crash_day_of_week, crash_hour, count(*) as crashes_per_hour
    from traffic_crashes_nfs
    group by crash_day_of_week, crash_hour
    )
    select crash_day_of_week, round( avg(crashes_per_hour), 2 ) as average_crashes_per_hour
    from cte
    group by crash_day_of_week
    order by average_crashes_per_hour desc
    limit 1;

    """,

    "12. High-Risk Time Slots (Morning/Afternoon/Evening/Night)": """

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

    """,

    "13. Top 3 Contributing Causes per Crash Type": """

    with cte as (
    select crash_type, prim_contributory_cause, count(*) as total_crashes,
    row_number() over (partition by crash_type order by count(*) desc ) as rnk
    from traffic_crashes_nfs
    group by crash_type, prim_contributory_cause
    )
    select crash_type, prim_contributory_cause as cause, total_crashes
    from cte
    where rnk <=3
    order by crash_type, total_crashes desc;

    """,

    "14. Year-over-Year Crash Growth Rate": """

    with cte1 as 
    (
    select year(crash_date) as crash_year, count(*) as total_crashes
    from traffic_crashes_nfs
    group by year(crash_date)
    )
    ,
    cte2 as (
    select crash_year, total_crashes, lag(total_crashes) over ( order by crash_year) as prev_year_crashes
    from cte1
    )
    select crash_year, total_crashes as curr_year_crashes, prev_year_crashes,
    round ( (total_crashes - prev_year_crashes) * 100 / prev_year_crashes , 2) as crash_growth
    from cte2
    order by crash_year;

    """,

    "15. Hotspot Zones (Rounded Coordinates)": """

    select round( latitude, 2 ) as zone_latitude , round (longitude, 2) as zone_longitude , count(*) as total_crashes
    from traffic_crashes_nfs
    group by round(latitude, 2), round(longitude, 2)
    order by total_crashes desc
    limit 10;

    """
}


insights = {
    "1. Top 5 Dangerous Weather + Crash Type":
        "Most of the crashes occured during normal weather conditons ie. clear weather.",

    "2. Top 10 Streets with Highest Injury Crashes":
        "These streets report the highest number of injury crashes, which requires closer traffic safety measures.",

    "3. Injury Percentage by Crash Type":
        "Some crash types lead to injuries much more often than others, showing which collision types tends to more injuries.",

    "4. Peak Crash Hour for Each Month":
        "Crash activity is not evenly spread throughout the day. This highlights the peak crash hour for each month.",

    "5. Top 5 Night-Time Primary Crash Causes":
        "Most common causes behind crashes during night hours is still unknown.",

    "6. Average Injuries: Daylight vs Darkness":
        "We can say that injury during crash is more during night than during daytime.",

    "7. Traffic Control Device with Highest Average Injuries":
        "This identifies which traffic control setup is associated with the highest average injuries per crash.",

    "8. Top 5 Crash Hotspots by Exact Coordinates":
        "These exact coordinates with the highest number of recorded crashes.",

    "9. Top 5 Streets with Highest Injury Rate (>100 crashes)":
        "We know which street has highest injury rate where crashes are more than 100.",

    "10. Most Common Crash Type Per Year":
        "This shows how the most frequent crash type changes from year to year, no injury / drive away is most frequent crash type during each year.",

    "11. Day with Highest Average Crashes Per Hour":
        "This identifies the weekday 6 with the heaviest crash activity on an hourly average basis.",

    "12. High-Risk Time Slots (Morning/Afternoon/Evening/Night)":
        "During Afternoon, most crashes take place in a day.",

    "13. Top 3 Contributing Causes per Crash Type":
        "For each crash type, primary cause of crash is unknown which has majority of the crashes.",

    "14. Year-over-Year Crash Growth Rate":
        "Tells the growth rate of crashes per year if it increased or decreased.",

    "15. Hotspot Zones (Rounded Coordinates)":
        "By spliting the crashes according to zones, its easier to identify which zone requires more attention."
}