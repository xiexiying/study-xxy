from socket import *
tcp_socket=socket()
addr=("127.0.0.1",8888)
#连接服务端
tcp_socket.connect(addr)
file=open("dlaam.jpg",'rb')
while True:
    data = file.read(1024)

    if not data:
        break
    tcp_socket.send(data)
tcp_socket.close()