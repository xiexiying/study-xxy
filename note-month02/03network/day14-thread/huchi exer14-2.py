"""
练习：两个分支线程分别打印A-Z 和1-52
启动后，打印顺序为12A34B56C78
一个程序中可用多个event或多个锁
"""
from threading import Thread,Lock
lock1=Lock()
lock2=Lock()
def fun_num():

    for i in range (1,53,2):
        lock1.acquire()#保证不会连续循环两次
        print(i,end='')
        print(i+1,end='')
        lock2.release()
def fun_zimu():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i),end='')
        lock1.release()
t1=Thread(target=fun_num)
t2=Thread(target=fun_zimu)
lock2.acquire()#创建线程之前把lock2锁住
t1.start()
t2.start()
t1.join()
t2.join()

