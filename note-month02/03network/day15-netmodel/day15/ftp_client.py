"""
ftp文件服务客户端
"""

from socket import *
import sys
from time import sleep

# 服务器地址
ADDR = ("0.0.0.0", 8888)


# 客户端发起请求的功能 --》 风格与服务端保持统一
class FTPClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    # 请求文件列表
    def do_list(self):
        self.sockfd.send(b"LIST")  # 发送请求
        result = self.sockfd.recv(128).decode()  # 等待反馈
        # 分情况讨论
        if result == 'OK':
            while True:
                file = self.sockfd.recv(10).decode()
                if file == "##":
                    break
                print(file, end="")
        else:
            print("文件库为空")

    def do_get(self, filename):
        msg = "GET " + filename
        self.sockfd.send(msg.encode())  # 发送请求
        result = self.sockfd.recv(128).decode()  # 等待反馈
        # 分情况讨论
        if result == 'OK':
            # 接收文件
            f = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")

    # 上传方法
    def do_put(self, filename):
        # 确保上传的文件存在
        try:
            f = open(filename, 'rb')
        except:
            print("要上传的文件不存在")
            return

        # 如果文件带路径提取文件名
        filename = filename.split('/')[-1]

        msg = "PUT " + filename
        self.sockfd.send(msg.encode())  # 发送请求
        result = self.sockfd.recv(128).decode()  # 等待反馈
        # 分情况讨论
        if result == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.sockfd.send(data)
            sleep(0.1)
            self.sockfd.send(b'##')
            f.close()
        else:
            print("文件已存在")

    def do_exit(self):
        self.sockfd.send(b"EXIT")
        self.sockfd.close()
        sys.exit("谢谢使用")


# 连接网络
def main():
    sock = socket()
    sock.connect(ADDR)

    ftp = FTPClient(sock)  # 实例化对象用于调用方法

    while True:
        print("\n======== 命令选项 =========")
        print("****     list        ****")
        print("****   get file      ****")
        print("****   put file      ****")
        print("****     exit        ****")
        print("===========================")

        cmd = input("请输入命令：")  # 选择功能
        if cmd == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        elif cmd == "exit":
            ftp.do_exit()
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
