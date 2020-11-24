"""
进程函数传参
"""
from multiprocessing import Process
from time import sleep
def worker(sec,name):
    for i in range (3):
        sleep(sec)
        print("i'm %s"%name)
        print("i'm working")
#位置传参
# p=Process(target=worker,args=(2,"xxy"))
#关键字传参
p=Process(target=worker,kwargs={"sec":2,"name":"xxy"},name="test",daemon=True)
# print("进程名称：",p.name)
# print("进程pid：",p.pid)
# print("进程生命：",p.is_alive())
p.start()
print("进程名称：",p.name)
print("进程pid：",p.pid)
print("进程生命：",p.is_alive())
p.join()