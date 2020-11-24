from socket import *
import time
# 服务端地址
ADDR = ("127.0.0.1", 8888)
filename = input("File:")


def main():

    tcp_socket = socket()
    tcp_socket.connect(ADDR)  # 连接服务端
    file = open(filename, 'rb')  # 打开要上传的文件
    # 边读边发送
    while True:
        data = file.read(1024)  # data-》bytes
        if not data:
            break
        tcp_socket.send(data)
    time.sleep(0.1)  # 防止粘包
    tcp_socket.send(b"##")  # 传输结束
    # 接收 “上传完成”
    data = tcp_socket.recv(1024)
    print(data.decode())

    tcp_socket.close()


if __name__ == '__main__':
    main()