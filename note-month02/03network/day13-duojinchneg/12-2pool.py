from multiprocessing import Pool
from time import time
def worker(msg,n):
    print("hhh")
pool=Pool(4)
for i in range(10):
    msg="id%d"%i
    pool.apply_async(func=worker,args=(msg,2))
pool.close()
pool.join()