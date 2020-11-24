"""
【2】 解析客户端发送的请求
【3】 根据请求组织数据内容
【4】 将数据内容形成http响应格式返回给浏览器
"""
from socket import *
from select import *
import re
class WebSever:
    def __init__(self,*,host="0.0.0.0",port=80,html=None):
        self.host=host
        self.port=port
        self.html=html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()
    def create_socket(self):
        self.sock=socket()
        self.sock.setblocking(False)
    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)
    def connect(self, sockfd):#连接客户端
        connfd, addr = sockfd.accept()
        print("connect from", addr)
        connfd.setblocking(False)
        # 每连接一个客户端就多监听一个
        self.rlist.append(connfd)  # 关注连接套接字的读事件
    def handle(self,connfd):# 具体处理客户端请求
        resquest=connfd.recv(1024*10).decode()#接收请求
        #提取请求内容 GET   /xxx.html  HTTP/1.1
        pattern=r"[A-Z]+\s+(?P<info>/\S*)"
        result=re.match(pattern,resquest)#只匹配开头
        if result:
            info=result.group("info")#请求内容
            self.send_html(connfd,info)
        else:
            return#匹配失败则结束函数
    def start(self):#启动网络服务--IO并发模型
        self.sock.listen(5)
        self.rlist.append(self.sock)
        while True:  # 里边不能出现死循环
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            # 对监控的套接字分情况讨论(总共俩种情况，监听套接字和连接套接字)
            for r in rs:
                if r is self.sock:  # 监听套接字情况
                    self.connect(r)
                else:  # 客户端连接套接字就绪，可以发消息了
                    try:
                        self.handle(r)#走到else这一步，其实已经是连接套接字了，直接传r就可
                    except:
                        pass
                    finally:#无论是否异常都执行
                        r.close()
                        self.rlist.remove(r)

    def send_html(self, connfd, info):#发送网页数据给浏览器
        if info=="/":
            filename=self.html+"/index.html"
        else:
            filename=self.html+info
        try:
            file=open(filename,"rb")#有可能访问图片用二进制打开
        except:#网页不存在
            with open (self.html+"/404.html", 'rb') as f:
                data=f.read()
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response = response.encode()+ data
        else:#网页存在
            data=file.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response =response.encode()+ data#字节串
            file .close() 
        finally:
            connfd.send(response)
if __name__ == '__main__':
    #使用者怎么用？
    #用户自己决定的需要传参，（地址、网页）
    httpd=WebSever(host="0.0.0.0",port=8888,html="./static")
    httpd.start()