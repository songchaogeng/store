class Cup:
    #高度
    __high=0
    def sethigh(self,high):
        self.__high=high
    def gethight(self):
        return self.__high

    #容积
    __volume = 0
    def setvolume(self,volume):
        self.__volume=volume
    def getvolume(self):
        return self.__volume

    #颜色
    __color=""
    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color

    #材质
    __material=""
    def setmaterial(self,material):
        self.__material=material
    def getmaterial(self):
        return self.__material

    def save_liquid(self):
        print("杯子的材质为",self.__material,"颜色为",self.__color,"高度为",self.__high,"容积为",self.__volume)


cup1=Cup()
cup1.sethigh(15)
cup1.setcolor("黑色")
cup1.setmaterial("不锈钢")
cup1.setvolume(100)
cup1.save_liquid()