"""
僵尸进程演示
1. join 回收僵尸
2. 如果子进程成为僵尸，当其父进程退出那么这个僵尸也会被系统处理
"""
from multiprocessing import Process
import signal

# 进程函数
def worker():
    for i in range(3):
        print("I'm zombie")
        print("I'm coming...")

# 声明忽略子进程退出
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

p = Process(target=worker)
p.start()

print(p.pid)

# p.join()

# 父进程不结束
while True:
    pass






