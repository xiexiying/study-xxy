from threading import Thread
from time import sleep
def fun(sec,name):
    print("开始")
    sleep(sec)
    print("执行%s"%name)

jobs=[]
for i in range(4):
    t=Thread(target=fun,args=(1,"xxy%d"%i))
    jobs.append(t)
    t.start()
[i.join() for i in jobs]
