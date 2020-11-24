from socket import *
from multiprocessing import Process
import sys
ADDR=("127.0.0.1",8888)

def recv_msg(sock):#收消息
    while True:
        data, addr = sock.recvfrom(1024*10)
        msg="\n"+data.decode()+"\n>>"
        print(msg,end="")
def send_msg(sock,name):#发消息
    while True:
        content = input(">>")

        if content=="exit":
            msg="EXIT "+name
            sock.sendto(msg.encode(),ADDR)
            sys.exit("您已退出")
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(),ADDR)
def main():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    # udp_socket.sendto("测试".encode(),ADDR)#测试
    while True:
        name=input("输入姓名：")
        msg="LOGIN "+name
        udp_socket.sendto(msg.encode(),ADDR)
        result,addr=udp_socket.recvfrom(128)
        if result==b"ok":
            print("已进入聊天室")
            break
        else:
            print("用户存在，重新输入")
    p=Process(target=recv_msg,args=(udp_socket,),daemon=True)#　创建子进程
    p.start()
    send_msg(udp_socket,name)#　父进程循环发送消息
    # p.join()



if __name__ == '__main__':
    main()