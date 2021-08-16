#bank={}
from bank.bank88 import Bank
import random
class ABC(Bank):
    def __init__(self):
        self.dic = {}
        self.size = 0
        self.maxSize = 100
        pass

    def mainPage(self):
        print("""
            **********************
            *     中国农业银行      *
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

    def open_an_account(self):
        dic = {}
        # 用户：账号(id)（str：系统随机产生8位数字）
        # 姓名(name)(str)、密码(pwd)(int:6位数字)、地址(address)、存款余额(balance)(int)
        # 开户行(opening_bank)（银行的名称（str））
        # 地址：国家(str)、省份(str)、街道(str)、门牌号(str)
        dic['name'] = input("输入用户名\n")
        dic['pwd'] = input("设置密码\n")
        dic['type']=input("账户类型\n")
        address = {}
        address['country'] = input("国家\n")
        address['province'] = input("省份\n")
        address['street'] = input("街道\n")
        address['door'] = input("门牌号\n")
        dic['address'] = address
        dic['balance'] = 1000
        dic['opening_bank'] = input("请输入开户行")
        id = random.randint(10000000, 99999999)
        dic['id'] = id

        return id, dic

    def transfer(self, send, receive, pwd, money):
        if send not in self.dic:
            print("sender not exists")
            return 1
        if receive not in self.dic:
            print("receiver not exists")
            return 1
        if self.dic[send]['tpye']==1 and money>=50000:
            print("because type is i,money must <=50000")
            return 1
        elif self.dic[send]['tpye']==2 and money>=20000:
            print("because type is i,money must <=20000")
            return 1
            pass
        result = self.withDraw(send, pwd, money)
        if result:
            return result
        if self.saveMoney(id=receive, money=money):
            return 0



if __name__ == '__main__':
    abc = ABC()
    abc.main()