import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="traffic_crash_analysis",
        # use_pure=True
    )

connection = get_connection()

print(connection)