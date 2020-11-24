"""
tcp 套接字循环模型 2
重点代码 ！！！
可以同时启动多个客户端
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听套接字
tcp_socket.listen(5)

# 循环等待处理客户端
while True:
    connfd,addr = tcp_socket.accept()

    data = connfd.recv(1024)
    print("Receive:",data.decode())
    connfd.send(b"Thanks")

    connfd.close()

# 关闭
tcp_socket.close()


