"""
进程池演示
进程池函数必须在进程池创建之前声明
父进程结束，进程池会立即销毁
"""
from multiprocessing import Pool
from time import sleep,ctime

# 进程池函数
def worker(msg,sec):
    print(ctime(),"---",msg)
    sleep(sec)

# 创建进程池  进程已经有了
pool = Pool(4)

# 添加事件
for i in range(10):
    msg = "Tedu-%d"%i
    pool.apply_async(func=worker,args=(msg,2))

pool.close() #  关闭进程池 不能添加新的事件函数

pool.join() # 阻塞回收进程池

