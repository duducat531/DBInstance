import pymysql

class DBInstance:
    def __init__(self):
        self.db = pymysql.connect("localhost", "wyn", "123456", "ebay_log", autocommit=True)

    def SaveToDB(self, data):
        pass

    def Execute(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

