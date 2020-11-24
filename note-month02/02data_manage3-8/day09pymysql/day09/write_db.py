"""
数据库写操作 示例

如果数据表支持事务控制，那么写操作会自动开启事务，
在execute后需要进行commit/rollback

如果数据表不支持事务控制，那么写操作在execute后立即生效
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

# 操作数据库写数据
# try:
#     sql="update cls set score=%s where id=%s;"
#     cur.execute(sql,[98,1])
#     db.commit() # 提交事务
# except Exception as e:
#     print(e)
#     db.rollback() # 回滚

# 批量进行数据写操作
data = [
    ("Lily",18,78),
    ("Dava",18,79),
    ("James",18,80),
    ("Boran",18,81)
]
try:
    sql = "insert into cls (name,age,score) " \
          "values (%s,%s,%s);"
    cur.executemany(sql,data)
    db.commit()
except:
    db.rollback()


# 关闭游标和数据库连接
cur.close()
db.close()







