import pandas as pd
from db_config import get_connection
from dotenv import load_dotenv
import os

try:
    load_dotenv()
    path = os.getenv('CSV_PATH') # getting my csv file path from .env

    # load the csv.
    df = pd.read_csv(path)

    # removed duplicate/derived cols.
    df.drop(columns=['date','year'], inplace=True)

    # column data type transformations.
    df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'])
    df['DATE_POLICE_NOTIFIED'] = pd.to_datetime(df['DATE_POLICE_NOTIFIED'])

    # database connection.
    conn = get_connection()
    cursor = conn.cursor()

    columns = ", ".join(df.columns)
    rows = df.values.tolist()
    placeholder = ", ".join( ['%s'] * len(df.columns) )

    insert_query = f"insert into traffic_crashes ({columns}) values ({placeholder})"

    cursor.executemany(insert_query, rows)
    conn.commit() # commit changes to database.

    print("Data insertion successful.")

except Exception as e:
    # in-case if an error occures while loading or connecting or inserting.
    print("Error : ",e)

finally:
    # close cursor and connection.
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()