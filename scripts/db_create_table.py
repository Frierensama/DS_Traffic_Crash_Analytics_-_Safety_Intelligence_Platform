from db_config import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    # to prevent error if table exists. drops table before creating again.
    cursor.execute(""" drop table if exists traffic_crashes_nfs """) 

    # table creation query.
    table_create_query = """ 
    create table traffic_crashes_nfs (

        #crash details
        CRASH_RECORD_ID char(128) primary key,
        CRASH_DATE datetime,
        POSTED_SPEED_LIMIT int,

        #some data regarding envi, crash, conditions
        TRAFFIC_CONTROL_DEVICE varchar(25),
        DEVICE_CONDITION varchar(25),
        WEATHER_CONDITION varchar(25),
        LIGHTING_CONDITION varchar(23),
        FIRST_CRASH_TYPE varchar(29),
        TRAFFICWAY_TYPE varchar(32),
        ALIGNMENT varchar(22),
        ROADWAY_SURFACE_COND varchar(16),
        ROAD_DEFECT varchar(26),
        REPORT_TYPE varchar(27),
        CRASH_TYPE varchar(33),
        DAMAGE varchar(14),


        DATE_POLICE_NOTIFIED datetime,

        #cause of crash
        PRIM_CONTRIBUTORY_CAUSE varchar(81),
        SEC_CONTRIBUTORY_CAUSE varchar(81),

        #address
        STREET_NO int,
        STREET_DIRECTION char(1),
        STREET_NAME varchar(30),
        BEAT_OF_OCCURRENCE float,
        NUM_UNITS int,

        #injuries
        MOST_SEVERE_INJURY varchar(25),
        INJURIES_TOTAL float,
        INJURIES_FATAL float,
        INJURIES_INCAPACITATING float,
        INJURIES_NON_INCAPACITATING float,
        INJURIES_REPORTED_NOT_EVIDENT float,
        INJURIES_NO_INDICATION float,
        INJURIES_UNKNOWN float,

        #crash details
        CRASH_HOUR int,
        CRASH_DAY_OF_WEEK int,
        CRASH_MONTH int,

        #location details
        LATITUDE float,
        LONGITUDE float,
        LOCATION varchar(40)
    )
    """
    # crash_report_id -- char(128).
    # crash_date, date_police_notified -- datetime.
    # year and date -- not included, duplicate/derived columns.
    # sizes of varchar columns are based on the max len element for each respective column with 1 char extra freedom.

    cursor.execute(query=table_create_query)
    conn.commit() # commit changes to database.

    print("Table Created in database=traffic_crash_analysis, table=traffic_crashes_nfs")

except Exception as e:
    # in-case if an error occures while connecting to database.
    print("Error :",e)

finally:
    # close cursor and connection.
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()