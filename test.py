import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="qaz92451888",
    database="student_db"
)

print("MySQL连接成功")

conn.close()