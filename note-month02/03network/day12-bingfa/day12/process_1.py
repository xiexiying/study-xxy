"""
进程创建示例

将需要新进程执行的事件封装为函数
通过模块的Process类创建进程对象，关联函数
通过进程对象调用start启动进程
通过进程对象调用join回收进程资源
"""
import multiprocessing as mp
from time import sleep

a = 1

# 进程函数
def fun():
    print("开始执行一个进程")
    sleep(3)
    global a
    print("a = ",a)
    a = 10000
    print("进程执行结束了")

# 创建进程对象
p = mp.Process(target=fun)

# 启动进程  进程真正诞生  运行fun函数，将其作为一个进程
p.start()

print("我也干一点事....")
sleep(2)
print("我也干完事情啦...")


# 释放资源  阻塞等待进程结束（fun运行完）
p.join()
print("a:",a)