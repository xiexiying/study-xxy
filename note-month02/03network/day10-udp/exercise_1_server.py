"""
练习2：
在客户端循环输入单词，可以得到单词的解释，打印出来
直接回车表示退出。

服务端，负责查询单词， 单词从数据库dict中查询，
给客户端提供查询结果

提示： 可以复制示例代码， 可以进行适当的封装
"""
from socket import *
import pymysql

args = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

# 数据处理类
class Database():
    def __init__(self,args):
        self.args = args
        self.db = pymysql.connect(**args)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 查询单词方法 传入单词返回单词解释
    def query(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        result = self.cur.fetchone() # (mean,) or None
        # 根据查询情况返回不同的内容 解释 or Not Found
        if result:
            return result[0]
        else:
            return "Not Found"

def main():
    # 生成udp套接字
    udp_sock = socket(AF_INET,SOCK_DGRAM)
    udp_sock.bind(("0.0.0.0",8888))

    # 实例化数据库处理对象
    db = Database(args)

    while True:
        # 接收单词
        data,addr = udp_sock.recvfrom(1024)
        # 获取单词解释
        mean = db.query(data.decode())
        # 发送解释
        udp_sock.sendto(mean.encode(),addr)

    # 关闭套接字
    db.close()
    udp_sock.close()

if __name__ == '__main__':
    main()