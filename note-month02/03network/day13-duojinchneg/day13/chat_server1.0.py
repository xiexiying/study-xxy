"""
Author: Levi
Email: lvze@tedu.cn
Time: 2020-11-17
Env: Python 3.6
socket and Process exercise
"""
from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息  {name:address}
user = {}


# 处理进入聊天室
def login(udp_socket, name, address):
    if name in user or "管理" in name:
        udp_socket.sendto(b"FAIL", address)
    else:
        udp_socket.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for i in user:
            udp_socket.sendto(msg.encode(), user[i])
        # 存储用户
        user[name] = address
        # print(user)


# 处理聊天
def chat(udp_socket, name, content):
    msg = "%s : %s" % (name, content)
    for i in user:
        # 　出去本人
        if i != name:
            udp_socket.sendto(msg.encode(), user[i])


# 　退出
def exit(udp_socket, name):
    del user[name]
    msg = "%s 退出聊天室" % name
    # 　通知其他人
    for i in user:
        udp_socket.sendto(msg.encode(), user[i])


# 子进程 处理客户请求
def request(udp_socket):
    # 循环接收请求,处理请求  (模型结构：一处接收，分情况讨论)
    while True:
        data, addr = udp_socket.recvfrom(1024)
        tmp = data.decode().split(" ", 2)  # 解析
        # 分情况讨论具体干什么
        if tmp[0] == "LOGIN":
            # tmp--> [LOGIN,name]
            login(udp_socket, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # tmp--> [CHAT,name,content]
            chat(udp_socket, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            # tmp--> [EXIT,name]
            exit(udp_socket, tmp[1])


# 搭建基本结构，启动函数
def main():
    # UDP套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(ADDR)

    p = Process(target=request, args=(udp_socket,), daemon=True)
    p.start()

    while True:
        content = input("管理员消息:")
        if content == "exit":
            print("服务退出")
            break
        msg = "CHAT 管理员消息 " + content
        udp_socket.sendto(msg.encode(), ADDR)  # 发给子进程


if __name__ == '__main__':
    main()
