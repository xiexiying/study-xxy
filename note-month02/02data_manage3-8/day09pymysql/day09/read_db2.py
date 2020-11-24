"""
数据库查询操作示例 2
"""
import pymysql

# 连接数据库
args = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"stu",
    "charset":"utf8"
}

db = pymysql.connect(**args)

# 创建游标  操作数据库数据，获取操作结果的对象
cur = db.cursor()

# 数据库读操作
name = input(">>")
# sql = "select name,age,score from cls where name='%s';"%name
# print(sql)

# 使用参数列表给sql传值，不能传 关键字，字段名表名
sql="select name,age,score from cls where name=%s or score>%s;"
cur.execute(sql,[name,75])

print("Result:",cur.fetchall())


# 关闭游标和数据库连接
cur.close()
db.close()







