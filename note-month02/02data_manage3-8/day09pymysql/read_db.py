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
sql="select name,age,score from cls;"
cur.execute(sql)
#迭代获取查询结果
# for row in cur:
#     print(row)
one=cur.fetchone()
print(one)
#关闭游标、数据库连接
cur.close()
db.close()
