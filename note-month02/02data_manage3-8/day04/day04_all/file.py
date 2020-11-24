"""
os 模块
"""
import os

print("文件大小（字节）:",os.path.getsize("./my.log"))
print("获取文件列表:",os.listdir("."))
print("查看文件是否存在:",os.path.exists("./my.log"))
print("查看文件是否是普通文件:",os.path.isfile("./my.log"))
os.remove("./union.txt") # 删除普通文件

