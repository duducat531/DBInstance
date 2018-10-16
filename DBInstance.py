import pymysql

class DBInstance:
    def __init__(self, server, user, password, database):
        self.db = pymysql.connect(server, user, password, database, autocommit=True)

    def SaveToDB(self, data):
        pass

    def Execute(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

if __name__ == '__main__':
    dbInstance = DBInstance("localhost", "wyn", "123456", "ebay_log")

