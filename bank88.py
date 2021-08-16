# 用户：账号(id)（str：系统随机产生8位数字）
# 姓名(name)(str)、密码(pwd)(int:6位数字)、地址(address)、存款余额(balance)(int)
# 开户行(opening_bank)（银行的名称（str））
# 地址：国家(str)、省份(str)、街道(str)、门牌号(str)
# 银行：能存储100用户的库(字典)


import random


class Bank:

    def __init__(self):
        self.dic = {}
        self.size = 0
        self.maxSize = 100

    # 添加用户（传入参数：用户的所有信息。
    # 返回值：整型值（1：成功，2：用户已存在，3：用户库已满））
    def addUsr(self,**user):
        if self.size >= self.maxSize:
            print("user library is full")
            return 3
        if user['id'] in self.dic:
            print("user already exists")
            return 2
        self.dic[str(user['id'])] = user
        return 1

    # 存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
    def saveMoney(self,id,money):
        if id in self.dic:
            self.dic[id]['balance'] += money
            return True
        else:
            print("user not exists")
            return False

    # 取钱（传入值：用户的账号，用户密码，取钱金额。
    # 返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够）
    def withDraw(self,id,pwd,money):
        if id not in self.dic:
            print("user not exists")
            return 1
        if self.dic[id]['pwd'] != pwd:
            print("wrong password")
            return 2
        if self.dic[id]['balance'] < money:
            print("dont have enough money")
            return 3
        self.dic[id]['balance'] -= money
        return 0

    # 转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。
    # 返回值：0：正常，1：账号不对，2密码不对，3钱不够）
    def transfer(self,send,receive,pwd,money):
        if send not in self.dic:
            print("sender not exists")
            return 1
        if receive not in self.dic:
            print("receiver not exists")
            return 1
        result = self.withDraw(send,pwd,money)
        if result:
            return result
        if self.saveMoney(id=receive,money=money):
            return 0

    # 查询账户功能（传入值：账号，账号密码，返回值：空）
    def query(self,id,pwd):
        id = str(id)
        if id not in self.dic:
            print("user not exists")
            return
        if self.dic[id]['pwd'] != pwd:
            print("wrong pwd")
            return
        # for key,value in self.__dic[id].items():
        #     print(key,value)
        data = self.dic[id]
        print("用户名:"+data['name'])
        print("密码:"+data['pwd'])
        address = data['address']
        print("""
    地址:
        国家:%s
        省份:%s
        街道:%s
        门牌号:%s
        """%(address['country'],address['province'],address['street'],address['door']))
        print("账户余额:"+str(data['balance']))
        print("开户行:"+data['opening_bank'])

    # 开户
    def open_an_account(self):
        dic = {}
        # 用户：账号(id)（str：系统随机产生8位数字）
        # 姓名(name)(str)、密码(pwd)(int:6位数字)、地址(address)、存款余额(balance)(int)
        # 开户行(opening_bank)（银行的名称（str））
        # 地址：国家(str)、省份(str)、街道(str)、门牌号(str)
        dic['name'] = input("输入用户名\n")
        dic['pwd'] = input("设置密码\n")
        address = {}
        address['country'] = input("国家\n")
        address['province'] = input("省份\n")
        address['street'] = input("街道\n")
        address['door'] = input("门牌号\n")
        dic['address'] = address
        dic['balance'] = 1000000
        dic['opening_bank'] = input("请输入开户行(1为工行，2为农行)")
        if int(dic['opening_bank'])==2:
            dic['type']=input("请输入账户类型(1为一类卡，2为二类卡)")
        id = random.randint(10000000,99999999)
        dic['id'] = id

        return id,dic


    def main(self):
        while True:
            self.mainPage()
            flag = int(input("请输入你希望执行的操作："))
            # 开户
            if flag == 1:
                id,dic = self.open_an_account()
                if self.addUsr(**dic) == 1:
                    print("添加用户成功,id为"+str(id))
                continue
            # 存钱
            elif flag == 2:
                id = input("请输入账号\n")
                money = int(input("请输入存款金额\n"))
                if self.saveMoney(id, money):
                    print("存款成功")
                continue
            # 取钱
            elif flag == 3:
                id = input("请输入账号\n")
                pwd = input("请输入密码\n")
                money = int(input("请输入取款金额\n"))
                if not self.withDraw(id, pwd, money):
                    print("取款成功\n")
                continue
            #转账
            elif flag == 4:
                send = input("请输入账号\n")
                pwd = input("请输入密码\n")
                receive = input("请输入转账账号\n")
                money = int(input("请输入转账金额\n"))
                if not self.transfer(send, receive, pwd, money):
                    print("转账成功")
                continue
            # 查询
            elif flag == 5:
                id = input("输入用户id\n")
                pwd = input("输入密码\n")
                self.query(id,pwd)
                continue
                pass
            elif flag == 6:
                break

    def mainPage(self):
        print("""
            **********************
            *     中国XX银行      *
            *     账号管理系统      *
            *      V1.0           *
            ***********************
            *   1.开户             *
            *   2.存钱             *
            *   3.取钱             *
            *   4.转账             *
            *   5.查询             *
            *   6.bye             *
            ***********************
        """)




if __name__ == '__main__':
    bank = Bank()
    bank.main()