"""
聊天室 客户端代码
"""

from socket import *
from multiprocessing import Process
import sys

# 服务器地址
ADDR = ("127.0.0.1",8888)

#　接收消息
def recv_msg(sock):
    while True:
        data,addr = sock.recvfrom(1024 * 10)
        print(data.decode())

# 发送消息
def send_msg(sock,name):
    while True:
        try:
            content = input("发言:")
        except KeyboardInterrupt:
            content = "exit"
        # 输入ｅｘｉｔ表示退出
        if content == "exit":
            msg = "EXIT " + name
            sock.sendto(msg.encode(),ADDR)
            sys.exit("您已退出聊天室")
        msg = "CHAT %s %s"%(name,content)
        sock.sendto(msg.encode(),ADDR)

# 启动函数
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入昵称:")
        msg = "LOGIN "+name
        udp_socket.sendto(msg.encode(),ADDR) # 发请求
        result,addr = udp_socket.recvfrom(128) # 收结果
        # OK 表示成功
        if result == b"OK":
            print("您已进入聊天室")
            break
        else:
            print("该用户已存在")

    #　创建子进程
    p = Process(target = recv_msg,args=(udp_socket,),daemon=True)
    p.start()
    #　父进程循环发送消息
    send_msg(udp_socket,name)


if __name__ == '__main__':
    main()