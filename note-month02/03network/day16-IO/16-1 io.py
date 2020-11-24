from socket import *
from time import *
sock=socket()
sock.bind(("0.0.0.0",8888))

sock.listen(5)
# sock.setblocking(False)#设置套接字对象为非阻塞
sock.settimeout(3)#3秒之后没有客户端进来，报错:socket.timeout: timed out
log=open("mylog.txt","a")
while True:
    try:
        print("waiting...")
        connfd,addr=sock.accept()
        print("connect from",addr)
    except BlockingIOError as e:#在阻塞的时候做其他的事情：写入日志
        sleep(1)
        msg="%s: %s\n"%(ctime(),e)
        log.write(msg)
    except timeout as e:
        msg = "%s: %s\n" % (ctime(), e)
        log.write(msg)
    else:#需要先链接再操作的IO
        data=connfd.recv(1024)
        print(data.decode())
