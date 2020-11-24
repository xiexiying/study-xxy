"""
【1】 分为服务端和客户端，要求可以有多个客户端同时操作。

【2】 客户端可以查看服务器文件库中有什么文件。

【3】 客户端可以从文件库中下载文件到本地。

【4】 客户端可以上传一个本地文件到文件库。

【5】 使用print在客户端打印命令输入提示，引导操作

"""
from socket import *
from threading import Thread
from time import sleep
import sys,os

HOST="0.0.0.0"
POST=8888
ADDR=(HOST,POST)
FTP="/home/tarena/图片/图片/"#文件库
class Handle(Thread):
    def __init__(self, connfd):
        self.connfd=connfd

        super().__init__(daemon=True)
    def list_(self):
        files = os.listdir(FTP)
        if files:
            self.connfd.send(b"ok")
            sleep(0.1)#避免毡包,连续发送俩个消息
            data = "\n".join(files)  # 文件名拼接换行，也可避免毡包,在这用sleep方法，会出现一个一个的打印，效果不好
            self.connfd.send(data.encode())
            sleep(0.1)
            self.connfd.send(b"##")
        else:
            self.connfd.send(b"fail")
    def down(self,filename):#下载
        try:
            file = open(FTP+filename, 'rb')
        except:
            self.connfd.send(b"fail")
        else:
            self.connfd.send(b"ok")
            sleep(0.1)
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            sleep(0.1)
            self.connfd.send(b"##")#发送##告知结束
            file.close()
    def up(self,filename):#上传
        listdir=os.listdir(FTP)
        if filename in listdir:
            self.connfd.send(b"fail")
        else:
            self.connfd.send(b"ok")
            sleep(0.1)
            with open(FTP+filename, 'wb') as f:
                while True:
                    data = self.connfd.recv(1024)
                    if data==b"##":
                        break
                    f.write(data)
                f.close()

    def run(self):
        #循环接收请求，调用不同方法处理
        while True:
            data=self.connfd.recv(1024).decode()
            tmp=data.split(" ",1)
            if not tmp or tmp[0]=="EXIT":
                break
            if tmp[0]=="list":
                self.list_()
            if tmp[0]=="DOWN":
                self.down(tmp[1])
            if tmp[0]=="UP":
                self.up(tmp[1])
            if not data:
                break
            print(data)
        self.connfd.close()#函数结束，线程结束

def main():
    sock=socket()
    sock.bind(ADDR)
    sock.listen(5)
    #循环呢链接客户端
    while True:
        try:
            connfd,addr=sock.accept()
            print("connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务端退出")
    #创建新线程，处理客户端事务
        t=Handle(connfd)#与Handle中的属性对应传参
        t.start()


if __name__ == '__main__':
    main()

