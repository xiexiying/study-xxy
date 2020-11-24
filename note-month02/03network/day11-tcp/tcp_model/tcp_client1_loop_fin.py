"""
tcp 循环模型1 客户端
重点代码 ！！！
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 默认参数就是tcp
tcp_socket = socket()

# 连接服务端
tcp_socket.connect(ADDR)

# 循环数据收发
while True:
    data = input(">>")
    if not data:
        break
    tcp_socket.send(data.encode())

    # 如果输入## 则告知服务端，结束循环
    # if data == "##":
    #     break

    data = tcp_socket.recv(1024)
    print("From server:",data.decode())

tcp_socket.close()