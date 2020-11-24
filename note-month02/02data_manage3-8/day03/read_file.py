file=open("buffer.py","r")
# data=file.read(8)
# data1=file.read(8)
# data2=file.read(80)
# data3=file.read(2)
# print("gfk",data3)
#----------------read每次读取指定长度-------------------------
#循环读取内容，直到文件读完结束
# while True:
#     data = file.read(8)
#     print(data,end='')
#     if data=='':#等同if not data:
#         break
# file.close()
#--------------readline一次读取一行---------------------------
# line=file.readline()
# line1=file.readline()
#
# print(line1)
#--------------迭代读取---------------------------
for line in file:
    print(line)
file.close()