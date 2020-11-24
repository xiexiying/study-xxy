"""
在主目录下/home/tarena/图片
删除大小不到50kb的文件
"""
import os
mydir="/home/tarena/图片/"
list_file=os.listdir(mydir)
for item in list_file:#获得的是文件名字
    filename=mydir+item
    if os.path.isfile(filename) and os.path.getsize(filename)<1024*50:
        os.remove(filename)
print(list_file)



