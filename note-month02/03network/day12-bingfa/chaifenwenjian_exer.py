"""
将一个大文件拆分为俩小文件
两个部分同时拷贝
"""
from multiprocessing import Process
import os
filename="1.jpg"
size = os.path.getsize(filename)

def child_cp():
    old_file = open(filename, 'rb')
    top = open("top.jpg", 'wb')
    data=old_file.read(int(size/2))
    top.write(data)
    top.close()
    old_file.close()
def child_cp2():
    old_file = open(filename, 'rb')
    new_file2=open("bot.jpg","wb")
    old_file.seek(int(size/2),0)
    data=old_file.read()
    new_file2.write(data)
    old_file.close()
    new_file2.close()
p=Process(target=child_cp2)
p.start()
child_cp()

p.join()