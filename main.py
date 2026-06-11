from mysql_helper import MySqlHelper

db = MySqlHelper()

result = db.query("SELECT * FROM student")

print(result)

db.close()