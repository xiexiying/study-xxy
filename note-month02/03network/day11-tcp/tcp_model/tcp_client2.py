"""
tcp 循环模型2 客户端
重点代码 ！！！
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)


# 循环数据收发
while True:
    data = input(">>")
    if not data:
        break
    # 整个套接字创建连接操作都需要重新来
    tcp_socket = socket()
    tcp_socket.connect(ADDR)

    tcp_socket.send(data.encode())
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())

    tcp_socket.close()