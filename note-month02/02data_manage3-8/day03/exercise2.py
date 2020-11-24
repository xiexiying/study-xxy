"""
编写函数，传入一个文件名，将这个文件拷贝到函数的执行目录下
不确定拷贝的文件类型  open两次
"""


def cp(file_name):
    name = file_name.split("/")[-1]
    old_file = open(file_name, 'rb')
    new_file = open(name, 'wb')
    while True:  # 边读边写
        data=old_file.read(1024)
        if data == '':  # 等同if not data:
            break
        new_file.write(data)
    new_file.close()
    old_file.close()
cp("myfile.py")