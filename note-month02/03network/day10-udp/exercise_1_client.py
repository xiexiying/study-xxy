from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

def main():
    # 创建与服务端相同的套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)

    while True:
        # 发送单词
        word = input("Word:")
        # 直接回车，客户端结束
        if not word:
            break
        udp_socket.sendto(word.encode(),ADDR)
        data,addr = udp_socket.recvfrom(1024)
        print("%s : %s"%(word,data.decode()))

    udp_socket.close()

if __name__ == '__main__':
    main()