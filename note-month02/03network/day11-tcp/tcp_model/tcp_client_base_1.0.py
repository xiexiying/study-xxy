"""
tcp 基础示例 客户端
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 默认参数就是tcp
tcp_socket = socket()

# 连接服务端
tcp_socket.connect(ADDR)

# 数据收发
data = input(">>")
tcp_socket.send(data.encode())

data = tcp_socket.recv(1024)
print("From server:",data.decode())

tcp_socket.close()