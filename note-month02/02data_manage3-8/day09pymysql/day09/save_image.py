"""
写入二进制文件演示
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

# 将图片读取为字节串
# with open("timg.jfif",'rb') as f:
#     data = f.read()
#
# # 将图片写入数据库
# sql = "update cls set image=%s where id=1;"
# cur.execute(sql,[data])
# db.commit()

# 提取图片
sql="select image from cls where id=1;"
cur.execute(sql)
data = cur.fetchone()[0] # 查询到的内容

# 将查询内容写入到文件
with open("mm.jpg",'wb') as f:
    f.write(data)

# 关闭游标和数据库连接
cur.close()
db.close()







