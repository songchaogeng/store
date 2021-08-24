class Air_conditioning:
    #品牌
    __brand=""
    def setbrand(self, brand):
        self.__brand = brand
    def getbrand(self):
        return self.__brand
    #价格
    __price=0
    def setprice(self, price):
        self.__price = price
    def getprice(self):
        return self.__price

    def open(self):
        print("空调开机了。。。")
    def close(self,min):
        print("空调将在",min,"分钟后自动关闭")

geli=Air_conditioning()
geli.setbrand("格力")
geli.setprice(1200)
#geli.getbrand()
print(geli.getbrand(),"牌的空调价格为：",geli.getprice())
geli.open()
geli.close(10)