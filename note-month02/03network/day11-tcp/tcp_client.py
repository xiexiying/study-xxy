"""
循环发送，发##结束接收
"""
from socket import *
tcp_socket=socket()
addr=("127.0.0.1",8888)
#连接服务端
tcp_socket.connect(addr)
while True:

    data=input(">>")
    tcp_socket.send(data.encode())
    # if data=="##":
    #     break
    if not data:
        break
    data=tcp_socket.recv(1024)
    print("from sever:",data.decode())
tcp_socket.close()

