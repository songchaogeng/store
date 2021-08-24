class Computer:
    #属性-屏幕大小
    __screen_size=0
    def setscreensize(self,screen_size):
        self.__screen_size=screen_size
    def getscreensize(self):
        return self.__screen_size
    #属性-价格
    __price=0
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    #属性-cpu型号
    __cpu=""
    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
    #属性-内存大小
    __ram_size=0
    def setramsize(self,ram_size):
        self.__ram_size=ram_size
    def getramsize(self):
        return self.__ram_size
    #属性-待机时长
    __standby_time=0
    def setstandbytime(self,standby_time):
        self.__standby_time=standby_time
    def getstandbytime(self):
        return self.__standby_time
    #行为-打字
    def typewriting(self):
        print("我是一台计算机，使用我可以打字")
    #行为-打游戏
    def playgame(self):
        print("开启你的游戏人生")
    #行为-看视频
    def watch_videos(self):
        print("欣赏一段视频吧")