"""
udp 服务端模型

重点代码 ！！！
"""
from socket import *

# 生成udp套接字
udp_sock = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_sock.bind(("0.0.0.0",8888))
while True:
# 接收数据  recvfrom 阻塞等待
    data,addr = udp_sock.recvfrom(5)
    print("接收到：",data.decode()) # data --> bytes
    # if data.decode() == "##":
    #     break
    # 发送数据 发送字节串
    n = udp_sock.sendto(b"Thanks",addr)
    print("发送了%d bytes"%n)

# 关闭套接字
udp_sock.close()