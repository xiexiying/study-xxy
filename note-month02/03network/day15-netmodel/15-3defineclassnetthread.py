"""

"""
from socket import *
from threading import Thread
from signal import *
import sys

HOST="0.0.0.0"
POST=8888
ADDR=(HOST,POST)
class Handle(Thread):
    def __init__(self, connfd):
        self.connfd=connfd
        super().__init__(daemon=True)
    def run(self):
        while True:
            data=self.connfd.recv(1024)
            if not data:
                break
            print(data.decode())
        self.connfd.close()
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
