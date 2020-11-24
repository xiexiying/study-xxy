import os

print("获取文件大小：",os.path.getsize("../day03/my.log"))#重要
#一个.代表当前目录   上一级目录..
print("获取文件列表",os.listdir('.'))#重要
print('查看文件是否存在',os.path.exists("../day03/my.log"))
print('查看文件是否是普通文件',os.path.isfile("../day03/my.log"))#文件是true，文件夹是false
os.remove("../day03/myfile.py")#删除文件

