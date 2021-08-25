from threading import Thread
import time

bread_basket=500

class Cooker(Thread):
    name=""

    def run(self):
        global bread_basket
        while True:
            if bread_basket==500:
                time.sleep(2)
            else:
                bread_basket+=1




class Person(Thread):
    name=""
    money=3000
    #global bread_basket
    def run(self):
        while True:
            global bread_basket
            if bread_basket==0:
                time.sleep(3)
            else:
                bread_basket-=1
                self.money-=3
                print(self.name,"当前还有",self.money,"钱")
                if self.money==0:
                    print("钱花完了")
                    break


cooker1=Cooker()
cooker1.name="cooker1"
cooker2=Cooker()
cooker2.name="cooker2"
cooker3=Cooker()
cooker3.name="cooker3"
cooker1.start()
cooker2.start()
cooker3.start()



per1=Person()
per1.name="per1"
per2=Person()
per2.name="per2"
per3=Person()
per3.name="per3"
per4=Person()
per4.name="per4"
per5=Person()
per5.name="per5"
per6=Person()
per6.name="per6"
per1.start()
per2.start()
per3.start()
per4.start()
per5.start()
per6.start()








