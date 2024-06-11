import pymysql
import sys,os

basePath=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

sys.path.append(basePath)
from tools.logOperate import Logger

class MySQL:
    def __init__(self, host, user, password, database):
        self.log = Logger(saveFile=False)
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def create_database(self, db_name):
        sql = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        self.log.info(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def create_table(self, table_name, columns):
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.log.info(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_data(self, table_name, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
        self.log.info(sql)
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()

    def update_data(self, table_name, data, condition):
        set_clause = ', '.join([f"{key}=%s" for key in data.keys()])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()

    def query_data(self, table_name, columns='*', condition=None):
        sql = f"SELECT {columns} FROM {table_name}"
        if condition:
            sql += f" WHERE {condition}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete_data(self, table_name, condition):
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(sql)
        self.conn.commit()




if __name__=="__main__":
    # 创建数据库连接
    db = MySQL(host='localhost', user='root', password='lsz990324', database='mypythontext')
    db.connect()

    # 创建数据库
    db.create_database('mypythontext')
    db.log.info("create database mypythontext")
    # 创建表
    db.create_table('users', 'id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT')

    # 插入数据
    db.insert_data('users', {'name': '张三', 'age': 18})
    db.insert_data('users', {'name': '李四', 'age': 20})

    # 更新数据
    db.update_data('users', {'age': 19}, "name='张三'")

    # 查询数据
    result = db.query_data('users', 'name, age', "age>18")
    # print(result)
    db.log.info(result)
    # 删除数据
    db.delete_data('users', "name='张三'")

    # 关闭数据库连接
    db.close()
    db.log.warning("close db")
