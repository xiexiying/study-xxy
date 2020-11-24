"""

"""
from multiprocessing import Process
#自定义进程类
class MyProcess(Process):
    def __init__(self,num):
        self.num=num
        super().__init__()#执行父类__init__
    def fun1(self):
        print("fun1")
        #进程要执行的内容
    def run(self):
        for i in range(self.num):
            print("重写父类run")
            self.fun1()
p=MyProcess(3)#无需传target，因为重写的父类的run里没有target属性
p.start()#调用底层方法启动进程，运行run方法
p.join()