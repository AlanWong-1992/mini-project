import pymysql

class DBHelper:
    
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def __connect__(self):
        self.con = pymysql.connect(
          host=self.host, 
          user=self.user, 
          password=self.password, 
          db=self.db, 
          cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.con.commit()
        self.__disconnect__()
    
    def execute_many(self, sql, val):
        self.__connect__()
        self.cur.executemany(sql, val)
        self.con.commit()
        self.__disconnect__()