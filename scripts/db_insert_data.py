import pandas as pd
from db_config import get_connection

df = pd.read_csv("C:/Users/rudeu/Documents/Github_Repos/DS_Traffic_Crash_Analytics_&_Safety_Intelligence_Platform/data/Traffic_CrashesData.csv")

#drop redundant cols
df.drop(columns=['date','year'], inplace=True)



df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'])
df['DATE_POLICE_NOTIFIED'] = pd.to_datetime(df['DATE_POLICE_NOTIFIED'])
