"""
模拟售票系统
500张票，t1-t500 将票存入列表
创建10个线程，记为w1-w10模拟10个卖票机器
10个线程同时卖到所有票卖完为止
票按顺序卖出，每张票出票时间0.1s
打印例：w6---t302
"""
from threading import Thread
from time import sleep
t_list=[]
for i in range (1,501):
    t_list.append("t%d"%i)
def sale_t(w):
    while t_list:

        print(w+"---"+t_list.pop(0))#pop弹出 索引为0的项，参数不传，默认弹出第一项
        sleep(0.1)
        #先执行sleep(0.1)，再执行打印的话会报错（列表为空不能弹出的错误），
        # 原因：比如最后3张票，10个线程过来，有的线程不能执行了，就报错了
jobs=[]
for i in range(10):
    t=Thread(target=sale_t,args=("w%d"%i,))
    jobs.append(t)
    t.start()
[i.join() for i in jobs]
