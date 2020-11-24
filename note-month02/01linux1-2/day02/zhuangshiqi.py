'''练习1： 使用vi编写一个程序
写一个求函数运行时间的装饰器

提示 ：  import time

        def fun():
            pass

        start = time.time()
        fun()
        end  = time.time()
        end - start()

plan : 求 1 到 20 20个整数的乘积结果'''
import time

def timeis(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = f(*args,**kwargs)
        end = time.time()
        print("函数执行时间:",end - start)
        return res 
    return wrapper 

@timeis
def fun(n):
    result = 1 
    for i in range(1,n + 1):
        result *= i
    return result

print(fun(20))