import pymysql

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='admin'
)

print(connection.cursor().execute('show databases;'))