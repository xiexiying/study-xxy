"""
练习1：  从客户端上传一张图片给服务端，在服务端以
当前日期为名称存储。

比如： 客户端 将图片 timg.jpg 发送给服务端
      服务端存储为  2020-11-13.jpg 即可

思路 ： 客户端   打开文件 读取文件  发送文件
       服务端   打开文件 接收内容  写入文件
"""
from socket import *
import time

# 接收文件，写入本地
def recv_image(connfd):
    filename = "%d-%d-%d.jpg"%time.localtime()[:3]
    with open(filename,'wb') as f:
        # 边接收边写入
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            f.write(data)

def main():
    # 创建tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0",8888))
    tcp_socket.listen(5)
    while True:
        connfd,addr = tcp_socket.accept()
        print("Connect from",addr)
        # 接收图片
        recv_image(connfd)
        connfd.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
