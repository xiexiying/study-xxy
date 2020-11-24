from socket import *
from time import sleep
import sys
ADDR=("0.0.0.0",8888)
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b"list")#发请求
        result=self.sockfd.recv(128).decode()#等待响应（响应情况ok or file，响应情况可以定义一个字典，响应数据）
        # 分情况讨论
        if result == 'ok':
            while True:
                file = self.sockfd.recv(10).decode()
                if file == "##":
                    break
                print(file, end="")#每次接收10，可能在循环接收的过程中接收到文件名中间，可能出现一个文件名打印成 两行，end=“
        else:
            print("文件库为空")
    def do_down(self,filename):
        msg="DOWN "+filename
        self.sockfd.send(msg.encode())#发请求
        result = self.sockfd.recv(128).decode()
        sleep(0.1)
        if result=="ok":
            # 接收文件
            f = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    print(data.decode())
                    break
                f.write(data)
            f.close()
            print("wanbi")
        else:
            print("文件不存在")
    def do_up(self,filename):
        msg = "UP " + filename
        self.sockfd.send(msg.encode())
        result=self.sockfd.recv(128).decode()
        sleep(0.1)
        if result=="ok":
            file = open(filename, 'rb')#当前目录文件上传
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.sockfd.send(data)
            sleep(0.1)
            self.sockfd.send(b'##')
            file.close()
        else:
            print("文件已存在，是否覆盖？")
    def do_exit(self):
        self.sockfd.send(b"EXIT")
        self.sockfd.close()
        sys.exit("谢谢使用")
def main():
    sock=socket()
    sock.connect(ADDR)
    ftp = FTPClient(sock)  # 实例化对象用于调用方法
    while True:
        print("""
        list     查看
        down     下载
        up       上传
        """)
        cmd = input("输入命令>>")

        if cmd=="list":

            ftp.do_list()
        elif cmd=="down":
            filename=input("输入要下载的文件名：")
            ftp.do_down(filename)
        elif cmd=="up":
            filename = input("输入要上传的文件名：")
            ftp.do_up(filename)
        elif cmd == "exit":
            ftp.do_exit()
        else:
            print("请输入正确命令")
if __name__ == '__main__':
    main()