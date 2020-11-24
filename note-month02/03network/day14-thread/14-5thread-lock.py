"""
互斥
不使用锁的话，结果不确定
"""
from threading import Thread,Lock
a=1
b=1
lock=Lock()
def fun():

    while True:
        lock.acquire()  # 上锁
        if a!=b:
            print("a=%d,b=%d"%(a,b))
        lock.release()
t=Thread(target=fun)
t.start()
# while True:
#     lock.acquire()
#     a+=1
#     b+=1
#     lock.release()
with lock:
    a += 1
    b+=1
t.join()