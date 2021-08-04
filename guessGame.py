'''
    猜数字：
        需求：系统随机产生一个数字，让用户从键盘输入您要的数字。(0~10000)
            1.如果猜中，则恭喜
            2.如果猜的数字比系统的数字大，温馨提示：大了
            3.如果猜小了，温馨提示：小了。
            一直到用户猜中为止。
        技术选型：
            1.random
            2.input
            3.if....else
            4.while
    金币功能：
        0.先登录，若登录成功！
        1.玩家初始化5000硬币，猜错扣500,金币不够，系统锁定。
        2.猜中，奖励10000硬币，是否进行第二轮游戏。

'''



import random
# 1.实现步骤
user="admin"
password="123456"

for i in range(3):
    name = input('请输入用户名: ')
    passwd = input('请输入密码: ')
    if name == user and passwd ==password:
        print('登录成功！')
        num = random.randint(0, 1000)
        count = 0
        coin = 5000
        while True:
            count = count + 1
            chose = input("亲输入您要的猜的数字：")
            chose = int(chose)
            if coin <= 0:
                print("您已经猜错了",count,"次,金币不够了,系统已退出，请重新登录" )
                break
            else:
                if chose > num:
                    print("大了！")
                    coin = coin - 500
                elif chose < num:
                    print("小了！")
                    coin = coin - 500
                else:
                    coin = coin + 10000
                    print("恭喜，您猜中了，本次数字为：", num, "，您本次输入了", count, "次！")
                    input_figure = input("如果想要重新开始游戏输入1，结束游戏输入2")
                    input_figure = int(input_figure)
                    if input_figure == 1:
                        continue
                    elif input_figure == 2:
                        break  # 跳出循环
                    else:
                        print("您输入的数据有误，请重新输入")
    else:
        print('登录失败')
        print('您还剩余%d次机会' % (2 - i))
else:
    print('失败超过3次，请稍后再试！')




