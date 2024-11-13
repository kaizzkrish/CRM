import pymysql

database = pymysql.connect(
    host='localhost',
    user='root',
    password='root@123'
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE elderco")

print("All Done!")
