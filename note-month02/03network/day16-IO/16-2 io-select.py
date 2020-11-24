from socket import *
from time import *
from select import select
sock=socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)
udp_sock=socket(AF_INET,SOCK_DGRAM)
file=open("mylog.txt","rb")
print("开始监控io")

rs,ws,xs=select([file,udp_sock],[sock,udp_sock],[])
print("rslist:",rs)
print("wslist:",ws)#监听套接字没有写行为，udp套接字有写行为
print("xslist:",xs)