"""
tcp 循环模型1 客户端
重点代码 ！！！
"""
from socket import *

# 服务端地址ss
ADDR = ("127.0.0.1",8888)
tcp_socket = socket()
# 连接服务端
tcp_socket.connect(ADDR)
#长时间占有服务端
while True:
    data = input(">>")
    if not data:
        break
    tcp_socket.send(data.encode())

    # data = tcp_socket.recv(1024)
    # print("From server:",data.decode())

tcp_socket.close()