class Person:
    __name=""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    __sex=""
    def setsex(self,sex):
        self.__sex=sex
    def getsex(self):
        return self.__sex
    __age=0
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    __phone_money=0
    def setphone_money(self,phone_money):
        self.__phone_money=phone_money
    def getphone_money(self):
        return self.__phone_money
    #手机品牌
    __brand=""
    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand
    #电池容量
    __capacity=0
    def setcapacity(self,capacity):
        self.__capacity=capacity
    def getcapacity(self):
        return self.__capacity
    #手机屏幕大小
    __screen_size=0
    def setscreen_size(self,screen_size):
        self.__screen_size=screen_size
    def getscreen_size(self):
        return self.__screen_size
    #手机最大待机时长
    __wait=0
    def setwait(self,wait):
        self.__wait=wait
    def getwait(self):
        return self.__wait
    #积分
    __ingegral=0
    def setingegral(self,ingegral):
        self.__ingegral=ingegral
    def getingegral(self):
        return self.__ingegral

    #发短信
    def message(self,text):
        print("发送的内容为",text)
    #打电话
    def call(self,num,minute):
        if len(num)==0 or self.__phone_money<1:
            print("电话号码为空或话费不足")
        else:
            print("电话拨通了")
            if minute>0 and minute<=10:
                self.__phone_money=self.__phone_money-minute*1
                self.__ingegral=self.__ingegral+minute*39
            elif minute>10 and minute<=20:
                self.__phone_money = self.__phone_money - minute * 0.8
                self.__ingegral = self.__ingegral + minute * 39
            else:
                self.__phone_money = self.__phone_money - minute * 0.65
                self.__ingegral = self.__ingegral + minute * 48



