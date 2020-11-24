from socket import *
def main():
    sock=socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen(5)
    connfd,addr=sock.accept()
    print("connect from",addr)
    recv_res(connfd)
    send_res(connfd)
    connfd.close()
    sock.close()


def send_res(connfd,filename):
    with open("zhihu.html","r") as zh:
        data=zh.read()
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += data
        connfd.send(response.encode())


def recv_res(connfd):
    data = connfd.recv(1024)
    print(data.decode())
if __name__ == '__main__':
    main()