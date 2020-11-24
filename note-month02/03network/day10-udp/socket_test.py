"""
套接字
"""
import socket
udp_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#选择udp服务
udp_sock.bind(("0.0.0.0",8888))
