from bank.ABCbank import ABC
from bank.bank88 import Bank
from bank.ICBCbank import ICBC




class Move(Bank):



    def saveMoney1(self, id, money):
        if id in self.dic:
            self.dic[id]['balance'] += 0.8*money
            return True
        else:
            print("user not exists")
            return False



    def withDraw1(self, id, pwd, money):
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


    def transfer(self, send, receive, pwd, money):
        if send not in self.dic:
            print("sender not exists")
            return 1
        if receive not in self.dic:
            print("receiver not exists")
            return 1
        if self.dic[send]['opening_bank']==2 and self.dic[send]['type']==1 and money>50000:
            print("because type is 1,money must <=50000")
            return 1
        elif self.dic[send]['opening_bank']==2 and self.dic[send]['type']==2 and money>20000:
            print("because type is 2,money must <=20000")
            return 1
        result = self.withDraw(send, pwd, money)
        if result:
            return result
        if self.dic[send]['opening_bank'] != self.dic[receive]['opening_bank']:
            if self.saveMoney1(id=receive, money=money):
                return 0
        else:
            if self.saveMoney(id=receive, money=money):
                return 0
    pass


if __name__ == '__main__':
    bank = Move()
    bank.main()