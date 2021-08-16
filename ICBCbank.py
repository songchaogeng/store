#bank={}
from bank.bank88 import Bank

class ICBC(Bank):
    def __init__(self):
        self.dic = {}
        self.size = 0
        self.maxSize = 100
        pass

    def mainPage(self):
        print("""
            **********************
            *     中国工商银行      *
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
    abc = ICBC()
    abc.main()