"""

"""
from socket import *
from time import *
from select import *
sock=socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)
udp_sock=socket(AF_INET,SOCK_DGRAM)
file=open("mylog.txt","rb")
print("开始监控io")
p=poll()
p.register(sock,POLLIN)
p.register(udp_sock,POLLOUT)
p.register(file,POLLOUT)
#建立文件描述符与对象的关系地图，与关注的IO保持一致
map={
    sock.fileno():sock,
    udp_sock.fileno():udp_sock,
    file.fileno():file
}
events=p.poll()
print(events)


