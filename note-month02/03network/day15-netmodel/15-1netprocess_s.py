"""
多进程并发模型（重点代码）

"""
from socket import *
from multiprocessing import Process
from signal import *
import sys
#定义全局变量
HOST="0.0.0.0"
PORT=8888
ADDR=(HOST,PORT)
def handle(connfd):#connfd传递客户端套接字，函数结束，子进程需结束
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()#函数结束，客户端结束
def main():
    #tcp套接字
    sock=socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("listen the port%d"%PORT)
    signal(SIGCHLD, SIG_IGN)  # 处理僵尸进程
    #循环处理客户端链接
    while True:
        try:#避免万一服务端退出，不要报错，捕获异常
            connfd,addr=sock.accept()
            print("connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务退出")
        #创建新进程，处理客户端事务
        p=Process(target=handle,args=(connfd,),daemon=True)#daemon=True:父进程退出的时候，子进程也退出
        p.start()
        #p.join(),不能用join，会导致必须这个进程结束才能接收下一个客户端进程，
        # 父进程不退出，很多子进程终将会退出，会产生大量僵尸进程，需要销毁进程，此时可用sigal,(也可创建一个线程专门回收进程垃圾)


if __name__ == '__main__':
    main()

