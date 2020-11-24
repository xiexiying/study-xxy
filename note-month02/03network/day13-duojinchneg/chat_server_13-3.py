'''
功能 ： 类似qq群功能
【1】 有人进入聊天室需要输入姓名，姓名不能重复
【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
'''
from socket import *
HOST="0.0.0.0"
PORT=8888
ADDR=(HOST,PORT)

user={}#{name:address}
def exit(udp_socket,name):
    del user[name]
    msg="%s 退出聊天室"%name
    for i in user:
        udp_socket.sendto(msg.encode(), user[i])
def chat(udp_socket,name,content):
    msg="%s:%s"%(name,content)
    for i in user:
        if i!=name:#除去自己，给其他人发送消息
            udp_socket.sendto(msg.encode(),user[i])
def login(udp_socket,name,address):
    if name in user:
        udp_socket.sendto(b"fail",address)
    else:
        udp_socket.sendto(b"ok", address)
        #通知其他人
        msg="welcome%s"%name
        for i in user:
            udp_socket.sendto(msg.encode(),user[i])
        user[name]=address#存储用户
        print(user)
#搭建基本结构，启动函数
def main():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(ADDR)
    #循环总体接收请求,分情况处理请求(模型结构：一处接收，分情况讨论)
    while True:
        data,addr=udp_socket.recvfrom(1024)#不断接收来自客户端消息
        # print(data.decode())#测试
        tmp=data.decode().split(" ",2)#解析得到列表
        if tmp[0]=="LOGIN":#需要网络协议设计，因为接收的消息是名字，不知道干嘛
            login(udp_socket,tmp[1],addr)# tmp--> [LOGIN,name]
        elif tmp[0]=="CHAT":#tmp--> [CHAT,name,content]
            chat(udp_socket,tmp[1],tmp[2])
        elif tmp[0]=="EXIT":#tmp--> [EXIT,name]
            exit(udp_socket,tmp[1])
if __name__ == '__main__':
    main()