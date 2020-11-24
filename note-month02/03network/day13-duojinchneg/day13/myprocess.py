"""
自定义进程类 示例
"""
from multiprocessing import Process

# 自定义进程类
class MyProcess(Process):
    def __init__(self,num):
        self.num = num
        super().__init__() # 执行父类init

    def fun1(self):
        print("执行fun1")

    def fun2(self):
        print("执行fun2")

    # 进程要执行的内容
    def run(self):
        for i in range(self.num):
            print("假装很复杂")
            self.fun1()
            self.fun2()

# 使用自定义类创建进程
p = MyProcess(3)
p.start() # 启动进程 --》 运行类中的run方法
p.join()



# class Process:
#     def __init__(self,target=None):
#         self._target = target
#
#     def run(self):
#         self._target()
#
#     def start(self):
#         # 调用底层方法创建进程
#         self.run()









