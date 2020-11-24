"""
收到##，不再接收消息
"""
from socket import *
tcp_socket=socket()
tcp_socket.bind(("0.0.0.0",8888))
#设置监听套接字
tcp_socket.listen(5)
#等待处理客户端连接
while True:
    print("waiting....")
    connfd,addr=tcp_socket.accept()
    print("connect from",addr)
#接受消息
    while True:
        data=connfd.recv(1024)
        # if data=="##".encode():
        #     break
        if not data:
            break
        print("receive",data.decode())
        connfd.send(b"thanks")
    connfd.close()
tcp_socket.close()


