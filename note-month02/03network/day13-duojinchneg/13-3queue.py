from multiprocessing import Process,Queue
q=Queue(3)
def reguest():
    name="hobby"
    psd="xxxxxx"
    q.put(name)
    q.put(psd)
def handle():
    print(q.get())
    print(q.get())
p1=Process(target=reguest)
p2=Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()