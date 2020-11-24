"""
 使用一个线程求100000以内质数之和，获取其时间
 使用4个线程求100000以内质数只能 记录时间
 提示： 100000分4分，每个进程求1份
"""
import time
from threading import Thread

def timeis(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = f(*args,**kwargs)
        end = time.time()
        print("函数执行时间:",end - start)
        return res
    return wrapper

# 判断一个数是否为质数
def isprime(n):
    if n <= 1:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

# 求从begin到end之间的所有质数之和
class Prime(Thread):
    def __init__(self,begin,end):
        super().__init__()
        self.begin = begin
        self.end = end

    # 求质数之和
    def run(self):
        prime = []  # 所有质数加入列表
        for i in range(self.begin,self.end):
            if isprime(i):
                prime.append(i)
        print(sum(prime))

@timeis
def thread_4():
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(i,i + 25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]
#
# # process_4() # 函数执行时间: 7.283637762069702
thread_4() # 函数执行时间: 13.1912841796875
# thread_10() # 函数执行时间: 13.1912841796875

# @timeis
# def no_process():
#     prime = []  # 所有质数加入列表
#     for i in range(1,100001):
#         if isprime(i):
#             prime.append(i)
#     print(sum(prime))
# no_process()
#
# no_process() # 函数执行时间: 15.625181198120117


