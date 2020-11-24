"""
创建数据库dict
创建数据表，words---id word mean
将单词本dict.txt中单词插入
"""
# create table words(id int primary key auto_increment,word varchar (30)not null,
# mean varchar(512) not null);
# def find_w(word):
#     file = open("dict.txt", "r")
#     for line in file:
#         temp=line.split(' ',1)#每次取一个单词  切割一处
#         if temp[0]>word:
#             break
#         elif temp[0]==word:
#             return temp[1].strip()#去除两边的空格
# print(find_w("a"))
import pymysql
args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}
db=pymysql.Connect(**args)
#创建游标 操作数据库数据，获取操作结果对象
cur=db.cursor()
data=[]
file = open("dict.txt", "r")
for line in file:
    temp=line.split(' ',1)#每次取一个单词  切割一处
    word=temp[0]
    mean=temp[1].strip()#去除两边的空格
    tuple01=(word,mean)
    data.append(tuple01)
# ---------------正则表达式版获取data-----------------------
# import re
# data=[]
# for line in file:
#     tmp=re.findall(r"(\w+)\s+(.*),line")#只输出子组内容，每次获得一个列表，列表由元祖组成
#     data.extend(tmp)
try:
    sql="insert into words (word,mean) values (%s,%s);"#需要都是%s字符串，才能使得sql语句正确
    cur.executemany(sql,data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
#关闭游标、数据库连接
cur.close()
db.close()