import pandas as pd

df = pd.read_csv("C:/Users/rudeu/Documents/Github_Repos/DS_Traffic_Crash_Analytics_&_Safety_Intelligence_Platform/data/Traffic_CrashesData.csv")

print("\n\nNull checks : ")
print(df.isnull().sum())

columns = df.columns.to_list()
print("\n\nColumns : ")
print(columns)

print("\n\nData Types : ")
print(df.dtypes)