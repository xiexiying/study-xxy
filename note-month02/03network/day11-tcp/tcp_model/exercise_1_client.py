from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)
filename = input("File:")

def main():
    tcp_socket = socket()
    tcp_socket.connect(ADDR) # 连接服务端
    file = open(filename,'rb') # 打开要上传的文件
    # 边读边发送
    while True:
        data = file.read(1024) # data-》bytes
        if not data:
            break
        tcp_socket.send(data)
        
    tcp_socket.close()

if __name__ == '__main__':
    main()