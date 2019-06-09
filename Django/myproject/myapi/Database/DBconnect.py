from . import DBconfig
import pymysql.cursors

class MyConnect:
    connection  = None
    def getConnection(self):
        self.connection = pymysql.connect(host=DBconfig.HOST,
                                          user=DBconfig.USER,
                                          password=DBconfig.PASSWORD,
                                          db=DBconfig.DB_NAME,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
    #---------Execute query------------
    def executeQuery(self, sql):
        self.getConnection()
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
            return result


