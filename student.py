class Student:
    #姓名
    __name=""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    #年龄
    __age=0
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age

    def showme(self):
        print("大家好，我叫",self.__name,"今年",self.__age,"岁了")
    def compare_age(self,age1):
        if self.__age==age1:
            print("我和同桌一样大")
        elif self.__age>age1:
            print("我比同桌大",self.__age-age1,"岁")
        else:
            print("我比同桌小",age1-self.__age,"岁")
        pass

    pass

xiaoming=Student()
xiaoming.setage(23)
xiaoming.setname("小明")
xiaoming.showme()


xiaohong=Student()
xiaohong.setage(25)
xiaohong.setname("小红")

xiaoming.compare_age(xiaohong.getage())