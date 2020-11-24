"""
客户端输入单词，得到解释，回车退出
在客户端循环输入单词，可以得到单词的解释，打印出来
直接回车表示退出。

服务端，负责查询单词， 单词从数据库dict中查询，
给客户端提供查询结果
"""
from socket import *
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
cur=db.cursor()
# 生成udp套接字
udp_sock = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_sock.bind(("0.0.0.0",8888))
while True:
# 接收数据  recvfrom 阻塞等待

    data,addr = udp_sock.recvfrom(1024)
    print("接收到word：",data.decode()) # data --> bytes
    #获取单词解释
    sql="select mean from words where word=%s;"#需要都是%s字符串，才能使得sql语句正确
    cur.execute(sql,[data.decode()])
    res=cur.fetchone()#返回元祖
    if res:
        result=res[0]
    else:
        result="not found"
#发解释到客户端
    udp_sock.sendto(result.encode(),addr)
    print("mean",res)
cur.close()
db.close()
# 关闭套接字
udp_sock.close()