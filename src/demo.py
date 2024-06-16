import sys,os

basePath=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

sys.path.append(basePath)

from tools.fileOperate import FileHandler
from tools.sqliteOperate import SQLiteDatabase
from tools.mysqlOperate import MySQL
from tools.logOperate import Logger
import configparser

from datetime import datetime

# log
def log_demo():
    current_time=datetime.now()
    # formatted_time=current_time.strftime("%Y_%m_%d_%H:%M:%S")
    formatted_time=current_time.strftime("%Y_%m_%d_%H")

    logpath=os.path.join(basePath,"log")
    logName=f"log_{formatted_time}.log"
    logpath=os.path.join(logpath,logName)
    print(logpath)
    log = Logger(logpath)
    log.debug('这是一条debug信息')
    return log

# mysql db operate
def mysql_db_demo():
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


# sqlite db operate
def sqlite_db_demo():
    databasename="export.db"
    databasename=os.path.join(basePath,'db',databasename)
    db = SQLiteDatabase(databasename)
    db.close()

# file operate
def file_demo():
    log=log_demo()
    log.info("file operate")
    fileName=os.path.join(basePath,"log","example.txt")
    file_handler = FileHandler(fileName)
    content = file_handler.read_file()
    log.info(f"hfhdsjfhfhj {content}")
    log.info("dsasd %s" % content)
    log.info(content)
    file_handler.write_file('这是一段新的内容')
    content = file_handler.read_file()
    log.info(content)

# config operate
def config_demo():
    log=log_demo()
    # 创建一个配置解析器对象
    config = configparser.ConfigParser()

    confg_path=os.path.join(basePath,'conf/config.ini')
    # 读取配置文件
    config.read(confg_path)

    # 获取默认配置
    debug = config.getboolean('DEFAULT', 'debug')

    log.debug(f"debug:{debug}")
    # log.info(debug)
    databasename = config.get('database', 'dataBaseName')

    log.info("databasename: %s" % databasename)
    # log.info(databasename)




if __name__ == '__main__':
    # log_demo()
    config_demo()
    sqlite_db_demo()
    # mysql_db_demo()
    # file_demo()




    # basePath=os.path.dirname(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    # log.debug('这是一条debug信息')
    # log.info('这是一条info信息')
    # log.warning('这是一条warning信息')
    # log.error('这是一条error信息')
    # log.critical('这是一条critical信息')
    # file_handler = FileHandler('example.txt')
    
    # content = file_handler.read_file()
    
    # log.error(content)
    # file_handler.write_file('这是一段新的内容')
    # content = file_handler.read_file()
    # log.info(content)
    

    # 创建一个配置解析器对象
    # config = configparser.ConfigParser()

    # confg_path=os.path.join(basePath,'conf/config.ini')
    # # 读取配置文件
    # config.read(confg_path)

    # # 获取默认配置
    # debug = config.getboolean('DEFAULT', 'debug')
    # log.info(debug)
    # databasename = config.get('database', 'dataBaseName')
    # log.info(databasename)
    # databasename=os.path.join(basePath,'db',databasename)
    # db = SQLiteDatabase(databasename)
    # db.close()