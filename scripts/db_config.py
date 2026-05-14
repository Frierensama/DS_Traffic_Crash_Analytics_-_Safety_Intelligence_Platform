import pymysql

# database connection function.
def get_connection():
    return pymysql.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "traffic_crash_analysis" # database name in my system.
    )