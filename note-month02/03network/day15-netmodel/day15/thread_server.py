"""
重点代码 ！！！
基于tcp 的多线程并发
"""
from socket import *
from threading import Thread
import sys

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

class Handle(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__(daemon=True) # 使用父类

    # 客户端处理函数
    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
        self.connfd.close()  # 函数结束 即分支线程结束


def main():
    # tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d..." % PORT)

    # 循环处理客户端连接
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务退出！")

        # 使用自定义线程类创建新线程，处理客户端事务
        t = Handle(connfd)
        t.start()


if __name__ == '__main__':
    main()  # 启动服务
