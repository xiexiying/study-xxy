"""
进程函数传参 进程对象属性示例
"""
from multiprocessing import Process
from time import sleep

# 带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# 按照位置传参
# p = Process(target=worker,args=(2,"Tom"))

# 关键字传参
p = Process(target=worker,
            args=(2,),
            kwargs={"name":'Tom'},
            name = "Test",
            daemon=True)

# 子进程随父进程而退出
# p.daemon = True

p.start() # 启动进程

print("进程名称:",p.name)
print("进程PID：",p.pid)
print("生命周期：",p.is_alive())

p.join(3)
print("===========================")