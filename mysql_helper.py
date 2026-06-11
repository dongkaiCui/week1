import pymysql

class MySqlHelper:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="qaz92451888",
            database="student_db"
        )

        self.cursor = self.conn.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()