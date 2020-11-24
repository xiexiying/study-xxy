"""
文件夹拷贝基础上，拷贝过程中显示拷贝进度，实时显示拷贝百分比
已拷贝的大小/总大小*100%
0.05秒打印一次
总大小=每个文件大小之和
"""
from multiprocessing import Pool,Process,Queue
import os
old_folder="/home/tarena/xxy/note-month02/03network/day10-udp/"
new_folder="./day10-udp/"
os.mkdir(new_folder)#创建文件夹
q=Queue()
def cp_file(file):#复制文件
    fr = open(old_folder+file, 'rb')
    fw = open(new_folder+file, 'wb')
    while True:  # 边读边写
        data = fr.read(1024)
        if not data:
            break
        n=fw.write(data)#已经拷贝的大小
        q.put(n)#已拷贝的字节传到消息队列
    fr.close()
    fw.close()
def get_size():
    total_size=0
    for file in os.listdir(old_folder):
        total_size += os.path.getsize(old_folder + file)
    return total_size

def main():#创建进程池

    files = os.listdir(old_folder)  # 文件列表
    total_size = get_size()
    pool = Pool(4)

    for file in files:
        pool.apply_async(func=cp_file,args=(file,))#进程池里的进程都是子进程
    cp_size=0
    while cp_size<total_size:
        cp_size+=q.get()
        print("copy:%.2f%%"%(cp_size/total_size*100))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
