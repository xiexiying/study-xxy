from threading import Thread
from time import sleep
import os
a=1
def fun():
    global a
    print("a->",a)
    a=100
    for i in range(3):
        sleep(1)
        print(os.getpid(),"hello%d"%i)
#子线程
t=Thread(target=fun)
t.start()
#主线程
for i in range(3):
    sleep(1)
    print(os.getppid(),"yoyo%d" % i)
t.join()
print("a=",a)#子线程可以修改全局变量
