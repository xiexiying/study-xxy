"""
练习2 :  创建一个数据库  dict
create database dict charset="utf8";

        创建数据表  words --> id  word  mean
create table words (id int primary key auto_increment,word varchar(30),mean varchar(512));

        将单词本 dict.txt 中单词插入到该数据表

思路： 使用mysql终端完成库和表的创建
      编写程序插入数据
        1. 将每一行的单词和解释提取出来
        2. 循环使用个execute 或直接使用executemany插入

"""
import pymysql
import re

# 连接数据库
args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}

db = pymysql.connect(**args)

# 创建游标  操作数据库数据，获取操作结果的对象
cur = db.cursor()

# 提取单词和解释形成大列表 --》[(word,mean),...]
file = open("dict.txt")
args = []
for line in file:
    tmp = re.findall(r"(\w+)\s+(.*)", line)
    args.extend(tmp)  # 合并列表

# 进行数据插入操作
try:
    sql = "insert into words (word,mean) values (%s,%s);"
    cur.executemany(sql,args)
    db.commit()
except:
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()
