"""
1. 会创建进程，理解进程执行过程中特征原理
      2. 使用一个进程求100000以内质数之和，获取其时间
         使用4个进程求100000以内质数只能 记录时间
         验证多进程会不会缩短总时间
         提示： 100000分4分，每个进程求1份
"""
from multiprocessing import Process
import time

def timeis(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = f(*args,**kwargs)
        end = time.time()
        t=end - start
        print("函数执行时间:",t)
        return res
    return wrapper

@timeis
def fun(num,n):
    prime=[]
    for i in range(num,n+1):
        if isprime(i):
            prime.append(i)
    print(sum(prime))
def isprime(n):#判断是否是质数
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

jobs = []
# for i in range (4):#分4份1自己的
#     p = Process(target=fun, args=(25000*i, 25000*i+25000))
#     jobs.append(p)
#     p.start()
for i in range(1,10001,2500):#分4份2老师方法
    p=Process(target=fun,args=(i,i+2500))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
# fun(1,100000)
