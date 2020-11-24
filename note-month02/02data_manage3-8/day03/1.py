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
file=open("my.log",'ab+')

while True:
    com = file.read()
    if not com:
        count = 1
    else:
        file.seek(0, 0)
        temp_list = file.readlines()
        temp = temp_list[-1].decode()
        count = temp[0]
        count = int(count)
        count += 1

    tuple_time=time.localtime()
    ss_time=time.strftime("%y-%m-%d %H:%M:%S",tuple_time)
    data=f"{str(count)}.{ss_time}\n".encode()
    file.write(data)
    file.flush()
    time.sleep(2)
    # count+=1
