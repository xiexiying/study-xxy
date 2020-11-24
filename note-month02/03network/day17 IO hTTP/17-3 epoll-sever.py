"""
基于epoll的IO并发模型
"""
from socket import *
from select import *
HOST="0.0.0.0"
PORT=8888
ADDR=(HOST,PORT)
sockfd=socket()
sockfd.bind(ADDR)
sockfd.listen(5)
#IO多路复用往往与非阻塞IO一起使用，避免耗时较长的处理造成卡顿
sockfd.setblocking(False)
#初始化
#建立文件描述符与对象的关系地图，与关注的IO保持一致
ep = epoll()#创建epoll对象
ep.register(sockfd, EPOLLIN)
map={
    sockfd.fileno():sockfd
}
while True:#里边不能出现死循环
    events=ep.poll()#循环监控
    #对监控的套接字分情况讨论(总共俩种情况，监听套接字和连接套接字)
    for fd,event in events:
        if fd ==sockfd.fileno():
            #处理客户端连接
            connfd, addr = map[fd].accept()
            print("connect from", addr)
            ep.register(connfd, EPOLLIN)
            connfd.setblocking(False)
            map[connfd.fileno()]=connfd#随时在字典添加关注的connfd
        else:#elif event==POLLIN:
            data=map[fd].recv(1024).decode()
            if not data:#当客户端退出的时候，避免这个循环再返回空打印空，需要删除监控
                ep.unregister(fd)#取消关注
                del map[fd]
                map[fd].close()
                continue#继续处理下一个
            print(data)
            map[fd].send(b"ok")