import pymysql
import random
from day10.DBUtils import select
from day10.DBUtils import update

class Bank:
    def __init__(self,bank_name="中国工商银行昌平支行",max_user=100):
        self.bank_name=bank_name
        self.max_user=max_user

    #添加用户
    def adduser(self):
        parm=[]
        account=random.randint(00000000,99999999)
        name=input("请输入用户名：")
        password=input("请输入密码：")
        address=input("请输入地址：")
        money=input("请输入存款余额：")
        parm=[account,name,password,address,money,self.bank_name]
        #print(parm)
        return parm
    #1.开户A
    def open_account(self,parm):
        sql="select count(*) from user"
        data=select(sql,[])
        print(data)
        if data[0][0]>self.max_user:
            #用户库已满
            return 3
        sql1="select * from user where account=%s"
        data1=select(sql1,parm[0])
        if len(data1)!=0:
            #用户已存在
            return 2
        sql2 = "insert into user values(%s,%s,%s,%s,%s,%s)"
        update(sql2,parm)
        #添加成功
        return 1
        pass
    #2.存钱
    def savemoney(self,account,num):
        sql="select * from user where account=%s"
        data1=select(sql,account)
        print(data1)
        if len(data1)==0:
            #账户不存在
            return False
        sql1="update user set money=money+%s WHERE account=%s"
        update(sql1,(num,account))
    #3.取钱
    def withdraw(self,account,num):
        sql = "select * from user where account=%s"
        data1 = select(sql, account)
        print(data1)
        if len(data1) == 0:
            # 账户不存在
            return False
        sql1 = "update user set money=money-%s WHERE account=%s"
        update(sql1, (num, account))
    #4.转账
    def transfer(self,account1,account2,num):
        sql = "select * from user where account=%s AND  account=%s"
        data1 = select(sql, (account1,account2))
        print(data1)
        if len(data1) != 2:
            # 某一个账户不存在
            return False
        sql1="update user set money=money+%s WHERE account=%s"
        update(sql1, (num, account2))
        sql2 = "update user set money=money-%s WHERE account=%s"
        update(sql2, (num, account1))
    #5.查询
    def find(self,account):
        sql = "select * from user where account=%s"
        data1 = select(sql, account)
        print(data1)
        if len(data1) == 0:
            # 账户不存在
            return False

icbc=Bank()
icbc.adduser()
icbc.open_account(icbc.adduser())
#填入注册账户信息
icbc.savemoney(9365343,20)
icbc.withdraw(9365343,30)