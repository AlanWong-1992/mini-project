import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

class DBHelper:
    
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def __connect__(self):
        try:
            self.con = mysql.connector.connect(
            host=self.host, 
            user=self.user, 
            password=self.password, 
            db=self.db
            #   cursorclass=mysql.connector.cursors.DictCursor
            )
            self.cur = self.con.cursor()
        except mysql.connector.errors.ProgrammingError as connectError:
            print(f'The Database you are connecting to does not exist. Please create the Database')

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
    
    def no_commit_execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()
    
    def execute_many(self, sql, val):
        self.__connect__()
        self.cur.executemany(sql, val)
        self.con.commit()
        self.__disconnect__()
