"""
同步互斥
没有event，俩线程抢占执行速度不同，主线程和子线程 在某个时间段有执行时间差结果不确定
"""
from threading import Thread,Event
psd="123lalala"
# e = Event()
def eve():
    print("xxy")
    global psd
    psd="456lelele"
    # e.set()
t=Thread(target=eve)
t.start()
print("psd")
# e.wait()
if psd=="456lelele":
    print("ok")
else:
    print("fail")
t.join()