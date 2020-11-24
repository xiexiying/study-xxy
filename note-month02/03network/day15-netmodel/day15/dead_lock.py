"""
死锁演示
"""
from threading import Thread,Lock
from time import sleep

# 交易类
class Account:
    def __init__(self,id,balance,lock):
        self._id = id #账号
        self.balance = balance # 存款
        self.lock = lock # 锁

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount

    # 存钱
    def deposit(self,amount):
        self.balance += amount

    # 查看
    def getBalance(self):
        return self.balance

# 生成两个账户
Abby = Account("Abby",50000,Lock())
Tom = Account("Tom",40000,Lock())

# 转账 from_ to 传入两个账户对象 amount转账金额
def transfer(from_,to,amount):
    from_.lock.acquire() # 锁住 from_账户
    from_.withdraw(amount) # 减少金额
    from_.lock.release()

    sleep(0.2) # 网络延迟时间
    to.lock.acquire() # to上锁
    to.deposit(amount) # to 增加钱
    to.lock.release()  # 分别解锁


t1 = Thread(target = transfer,args=(Abby,Tom,1000))
t2 = Thread(target = transfer,args=(Tom,Abby,1000))
t1.start()
t2.start()
t1.join()
t2.join()

# transfer(Abby,Tom,1000)
# print("Abby:",Abby.getBalance())
# print("Tom:",Tom.getBalance())