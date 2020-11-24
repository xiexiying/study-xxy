"""
练习1： 编写一个程序删除 /home/tarena/图片
文件夹中所有 大小不到 10kb的 普通文件
"""
import os

DIR = "/home/tarena/图片/"

# 遍历列表
for file in os.listdir(DIR):
    filename = DIR + file
    if os.path.isfile(filename) and os.path.getsize(filename) < 1024 * 10:
        os.remove(filename)