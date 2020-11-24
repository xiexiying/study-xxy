"""
udp 客户端演示

重点代码 ！！！
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 创建与服务端相同的套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送数据
data = input(">>")
udp_socket.sendto(data.encode(),ADDR)

# 接收
data,addr = udp_socket.recvfrom(1024)
print("从服务端收到:",data.decode())

udp_socket.close()