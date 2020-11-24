"""
编写程序，在my.log文件中不间断写入如下内容，每两秒写入一次，
实时显示每次写入的内容flush，程序不间断执行（死循环）
当程序结束后，如果重新启动，序号可以衔接(确定之前的行数，+1)
1.2020-01-01  10:10:10（当前时间）
2.2020-01-01  10:10:12
3.2020-01-01  10:10:14
4.2020-01-01  10:10:16
localtime()  sleep()
"""
import time
file=open("my.log",'a+')#a+打开，初始偏移量在结尾

while True:
    file.seek(0, 0)#偏移量从头开始
    temp_list = file.readlines()
    if not temp_list:
        count = 1
    else:
        temp = temp_list[-1]
        count = temp[0]
        count = int(count)
        count+=1
    tuple_time=time.localtime()
    ss_time=time.strftime("%y-%m-%d %H:%M:%S",tuple_time)
    data=f"{str(count)}.{ss_time}\n"
    file.write(data)
    file.flush()#实时显示每次写入的内容，也可以用buffering=1  行缓冲
    time.sleep(2)

#-----------老师的做法-------------------
import time

# 初始文件偏移在结尾
file = open("my.log","a+",buffering=1)

n = 1 # 行数 + 1
file.seek(0,0) # 文件偏移量在开头
for i in file:#遍历行数，n每次加1，获得最新的行数
    n += 1

while True:
    tm = "%d-%d-%d %d:%d:%d\n"%time.localtime()[:6]
    msg = "%d. "%n + tm
    file.write(msg)
    time.sleep(2)
    n += 1