from socket import *
import re
filename="./chat.txt"
chat={}
def chat_dict():
    file=open(filename)
    list_=[]
    for line in file:
        res=re.findall(r"(\S+)\s+(.+)",line)
        list_+=res
    global chat
    chat=dict(list_)

def answer(requst):
    for key in chat:
        if key in requst:
            return chat[key]
    return "不知道"
def main():
# 创建tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)

    # 绑定地址
    tcp_socket.bind(("0.0.0.0",8888))

    # 设置监听套接字
    tcp_socket.listen(5)

    # 循环等待处理客户端
    while True:
        connfd,addr = tcp_socket.accept()

        qes = connfd.recv(1024)
        print("Receive:",qes.decode())


        res=answer(qes.decode())
        connfd.send(res.encode())
        connfd.close()

    # 关闭
    tcp_socket.close()


if __name__ == '__main__':
    chat_dict()
    main()