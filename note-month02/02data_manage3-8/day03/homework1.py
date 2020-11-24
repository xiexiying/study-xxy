"""
函数，传列表，列表为前几天的课程文档（含路径），将列表文件合并一个为union.txt
"""
list_txt=["buffer.py","1.py"]
def fun(list_):
    new=open("union.txt",'a+')
    for i in range(len(list_)):
        file=open(list_[i],'r')
        data=file.read()
        new.write(data)
    new.close()

fun(list_txt)

