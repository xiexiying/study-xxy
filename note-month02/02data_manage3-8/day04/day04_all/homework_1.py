"""
练习4： 编写一个程序， 运行后在my.log文件中不间断写入
如下内容：
    1. 2020-01-01  10:10:10
    2. 2020-01-01  10:10:12
    3. 2020-01-01  10:10:14
    4. 2020-01-01  10:10:16
    5. 2020-01-01  10:11:29
    6. 2020-01-01  10:11:31
每隔2s写入一次,要求实时显示每次写入的内容，程序不间断循环
执行,当程序结束后，如果重新启动，序号能够衔接

提示： 生成当前时间  import time   localtime() sleep()
      用什么方式打开？  重新启动后序号怎么确定？
"""
import time

# 初始文件偏移在结尾
file = open("my.log","a+",buffering=1)

n = 1 # 行数 + 1
file.seek(0,0) # 文件偏移量在开头
for i in file:
    n += 1

while True:
    tm = "%d-%d-%d %d:%d:%d\n"%time.localtime()[:6]
    msg = "%d. "%n + tm
    file.write(msg)
    time.sleep(2)
    n += 1








