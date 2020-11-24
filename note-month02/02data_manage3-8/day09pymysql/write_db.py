"""
数据库操作
如果数据表支持事务，要执行写操作，sql为写入语句，默认开启事务，需要用支持事务控制的引擎，然后commit
如果数据表不支持事务，执行写操作立即生效
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
#操作数据库写数据
# try:#一般用异常处理来进行写操作
#     sql="update cls set score=120 where id=1"
#     cur.execute(sql)
#     db.commit()#因为数据表引擎支持事务，所以要提交
# except Exception as e:
#     print(e)
#     db.rollback()
#-----------批量写数据------------
data=[
    ("ccc",33,44),
    ("ddd",33,44),
    ("eee",33,44)
]
try:
    sql2="insert into cls (name,age,score) values (%s,%s,%s);"#需要都是%s字符串，才能使得sql语句正确
    cur.executemany(sql2,data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
#关闭游标、数据库连接
cur.close()
db.close()
