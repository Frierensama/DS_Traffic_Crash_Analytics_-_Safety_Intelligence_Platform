import pymysql

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='admin'
)
cursor = connection.cursor()
query = 'show databases;'


cursor.execute(query)

result = cursor.fetchall()

print(result)



# print()