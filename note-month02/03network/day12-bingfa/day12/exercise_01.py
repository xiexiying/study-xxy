"""
练习1： 有一个大文件，先需要将其拆分为两个小文件
要求上下两个部分同时拷贝

思路：
上下两个部分的拷贝分别封装为一个函数，各自由一个进程
执行
os.path.getsize()

加强型： 假设文件较大，不许1次读取全部
"""
from multiprocessing import Process
import os

filename = "./timg.jfif"
size = os.path.getsize(filename) # 文件大小

# 如果父进程打开文件，子进程直接使用fr那么父子进程使用
# 同一个文件偏移量，相互影响。如果在各自进程中open则不会
# fr = open(filename, 'rb')

# 拷贝上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')

    # fw.write(fr.read(size//2)) # 一次性读取问价一半内容

    n = size // 2 # 一半内容大小
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))

    fr.close()
    fw.close()

# 拷贝下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size//2,0) # 文件偏移量到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 使用多进程完成同时执行两个任务
p = Process(target = top)
p.start() # 上半部分

bot() # 下半部分

p.join()