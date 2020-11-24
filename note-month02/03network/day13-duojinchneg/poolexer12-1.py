"""
文件夹拷贝
"""
from multiprocessing import Pool
import os
old_folder="/home/tarena/xxy/note-month02/03network/day10-udp/"
new_folder="./day10-udp/"
os.mkdir(new_folder)#创建文件夹
def cp_file(file):#复制文件
    fr = open(old_folder+file, 'rb')
    fw = open(new_folder+file, 'wb')
    while True:  # 边读边写
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

def main():

    pool = Pool(4)
    files = os.listdir(old_folder)#文件列表
    for file in files:
        pool.apply_async(func=cp_file,args=(file,))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
