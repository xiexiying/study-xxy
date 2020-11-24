"""
练习1： 文件夹拷贝
有一个目录里面有若干普通文件，编写一个程序，将其拷贝一份
要求： 使用进程池完成  拷贝每个文件都作为一个进程事件执行

提示： os.listdir()
      os.mkdir(dir)
      创建新文件夹 --》 将源文件夹中所有文件拷贝过来即可
"""
from multiprocessing import Pool,Queue
import os

# 全局变量声明要拷贝的文件夹和目标文件夹
old_folder = "/home/tarena/qtx/" #要拷贝的文件夹
new_folder = "./qtx/" # 拷贝到哪里
os.mkdir(new_folder) #　创建文件夹

q = Queue() # 用于传递拷贝的大小

# 复制文件
def copy(file):
    fr = open(old_folder+file,'rb')
    fw = open(new_folder+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data) # 写入的字节数
        q.put(n) # 已经拷贝的字节数
    fr.close()
    fw.close()

# 获取文件夹总大小
def get_size():
    total_size = 0
    for file in os.listdir(old_folder):
        total_size += os.path.getsize(old_folder+file)
    return total_size


# 创建进程池
def main():
    files = os.listdir(old_folder) # 文件列表
    total_size = get_size() # 总大小

    # 创建进程池
    pool = Pool(4)
    # 添加事件
    for file in files:
        pool.apply_async(func=copy,args=(file,))

    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get() # 获取大小
        print("拷贝了 %.2f%%"%(copy_size/total_size*100))

    # 结束
    pool.close()
    pool.join()

main()




