import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DBNAME')

# database connection function.
def get_connection():
    return pymysql.connect(
        host = host,
        user = user,
        password = password,
        database = database # database name in my system.
    )
