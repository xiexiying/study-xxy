"""
io多路复用 循环链接处理客户端（没有长期的阻塞）
重点代码
"""
from socket import *
from select import select
HOST="0.0.0.0"
PORT=8888
ADDR=(HOST,PORT)
sockfd=socket()
sockfd.bind(ADDR)
sockfd.listen(5)
#IO多路复用往往与非阻塞IO一起使用，避免耗时较长的处理造成卡顿
sockfd.setblocking(False)
#初始化
rlist=[sockfd]
wlist=[]
xlist=[]
while True:#里边不能出现死循环
    rs,ws,xs=select(rlist,wlist,xlist)
    #对监控的套接字分情况讨论(总共俩种情况，监听套接字和连接套接字)
    for r in rs:
        if r is sockfd:#监听套接字情况
            connfd,addr=r.accept()
            print("connect from",addr)
            connfd.setblocking(False)
            #每连接一个客户端就多监听一个
            rlist.append(connfd)#关注连接套接字的读事件
        else:#客户端连接套接字就绪，可以发消息了
            data=r.recv(1024).decode()
            if not data:#当客户端退出的时候，避免这个循环再返回空打印空，需要删除监控
                rlist.remove(r)
                r.close()
                continue#继续处理下一个
            print(data)
            r.send(b"ok")#连接套接字的写事件，与rlist无关，也可以存入wlist多路复用，但每次用完要删除如下：
    #         wlist.append(r)
    # for w in ws:
    #     w.send(b"ok")
    #     wlist.remove(w)#发完记得删除