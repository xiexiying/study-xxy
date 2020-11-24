import multiprocessing as mp
from time import sleep

a=1
# 进程函数
def fun():
    print("开始执行一个进程")
    sleep(3)
    print("进程执行结束了")
    global a
    a=100
    print("子进程的a=",a)
# 创建进程对象
p = mp.Process(target=fun)

# 启动进程  进程真正诞生  运行fun函数，将其作为一个进程
p.start()

print("我也干一点事....")
sleep(2)
print("我也干完事情啦...")
print("a==",a)
# 释放资源  阻塞等待进程结束（fun运行完）
p.join()
print("a=",a)