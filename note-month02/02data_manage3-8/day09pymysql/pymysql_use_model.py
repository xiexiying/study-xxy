"""
数据库操作
"""
#连接数据库
import pymysql
args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"stu",
    "charset":"utf8"
}
db=pymysql.Connect(**args)
#创建游标 操作数据库数据，获取操作结果对象
cur=db.cursor()
#操作数据库数据



#关闭游标、数据库连接
cur.close()
db.close()
