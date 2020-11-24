#服务端
# from socket import *
# #创建套接字
# udp_socketxxy=socket(AF_INET,SOCK_DGRAM)
# #绑定地址
# udp_socketxxy.bind(("0.0.0.0","9999"))
# #接收数据
# data,addr=udp_socketxxy.recvfrom(1024)
# #发送数据
# n=udp_socketxxy.sendto(b"hhhj",addr)
# #关闭套接字
# udp_socketxxy.close()

#客户端
from socket import *
#创建相同的套接字
udp_sock=socket(AF_INET,SOCK_DGRAM)
#服务器地址
addrsever=("127.0.0.1",9999)
#发送数据
udp_sock.sendto(b"hh",addrsever)
#接收数据
data,addrsever=udp_sock.recvfrom(1024)


