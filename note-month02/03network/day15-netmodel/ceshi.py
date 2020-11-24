"""
客户端上传图片给服务端，服务端以日期名为名称存储
"""
from socket import *
import time
tcp_socket=socket()
tcp_socket.bind(("0.0.0.0",8888))
#设置监听套接字
tcp_socket.listen(5)
#等待处理客户端连接
while True:
    print("waiting....")
    connfd,addr=tcp_socket.accept()
    print("connect from",addr)
    #接受消息

    tuple_time=time.localtime()
    mytime=time.strftime("%y-%m-%d %H:%M:%S",tuple_time)
    with open(f"{mytime}.jpg",'wb') as f:
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            f.write(data)
    connfd.close()
tcp_socket.close()

