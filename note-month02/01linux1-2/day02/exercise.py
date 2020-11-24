"""
装饰器，计算运行时间
"""
import time
def times(fun):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res =fun(*args,**kwargs )
        end_time=time.time()
        print(f"执行时间{end_time-start_time}")
        return res
    return wrapper
@times
def fun(n):
    ress=1
    for i in range (n):
        ress*=i
    return ress
print(fun(200))
