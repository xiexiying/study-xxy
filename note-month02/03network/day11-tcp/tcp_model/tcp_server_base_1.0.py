"""
tcp 套接字基础实例
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听套接字
tcp_socket.listen(5)

# 等待处理客户端连接
print("Waiting for connect...")
connfd,addr = tcp_socket.accept()
print("Connect from",addr)

# 收发数据
data = connfd.recv(1024)
print("Receive:",data.decode())

connfd.send(b"Thanks")

# 关闭
connfd.close()
tcp_socket.close()


