"""
输入姓名，获取学生信息
列表传参，不用给变量加引号
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
cur = db.cursor()
def get_massage(name):

    #操作数据库数据
    #sql=f"select * from cls where name='{name}';"
    # sql=f"select * from cls where name={name};"
    sql="select * from cls where name=%s;"
    #sql=f"select * from cls where id={id};"
    print(sql)
    cur.execute(sql,[name])
    #迭代获取查询结果
    for row in cur:
        print(row)
    # one=cur.fetchone()
    # print(one)
get_massage("jim")
#关闭游标、数据库连接
cur.close()
db.close()
