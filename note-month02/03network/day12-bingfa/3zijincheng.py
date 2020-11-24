"""
蓄暖创建子进程
"""
from multiprocessing import Process
from time import sleep
import os
def th1():
    sleep(2)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())
def th2():
    sleep(3)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())
def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), "--", os.getpid())
jobs=[]
for i in [th1,th2,th3]:
    p = Process(target=i)
    jobs.append(p)
    p.start()
for i in jobs:
    p.join()