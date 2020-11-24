"""
编写一个函数，传入一个列表，列表中为之前几天的
课上文档（含路径） ,将列表中文件合成1个 union.txt
"""

files = [
"../day01/1.txt",
"../day02/2.txt",
"../day03/3.txt"
]


def union(list_):
    new = open("union.txt",'w')
    # 循环打开那些要合并的文件
    for file in list_:
        with open(file,'r') as f:
            new.write(f.read())
    new.close()

union(files)