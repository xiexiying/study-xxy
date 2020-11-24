"""

"""
from socket import *
from threading import Thread
from signal import *
import sys

HOST="0.0.0.0"
POST=8888
ADDR=(HOST,POST)

def handle(connfd):
    while True:
        data=connfd.recv(1024)

        if not data:
            break
        print(data.decode())
    connfd.close()
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
        t=Thread(target=handle,args=(connfd,),daemon=True)
        t.start()

if __name__ == '__main__':
    main()
