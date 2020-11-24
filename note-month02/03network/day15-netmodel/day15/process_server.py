"""
重点代码 ！！！
基于tcp 的多进程并发

步骤：
创建网络套接字用于接收客户端请求
等待客户端连接
客户端连接，则创建新的进程具体处理客户端请求
主进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""
from socket import *
from multiprocessing import Process
from signal import *
import sys

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


# 客户端处理函数
def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()  # 函数结束 即子进程结束


def main():
    # tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d..." % PORT)
    signal(SIGCHLD, SIG_IGN)  # 处理僵尸进程

    # 循环处理客户端连接
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务退出！")

        # 创建新进程，处理客户端事务
        p = Process(target=handle, args=(connfd,), daemon=True)
        p.start()


if __name__ == '__main__':
    main()  # 启动服务
