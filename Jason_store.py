'''
    任务：
        优化购物小条
        10张机械革命优惠券，打0.5
        20张卫龙辣条优惠券  打0.3
        15张HUA WEI WATCH   打0.8
        随机抽取一张优惠券。


    商城：
        1.准备一些商品
        2.有空的购物车
        3.钱包
        4.结算
    流程：
        看你输入的产品存不存在，
            若存在
                若钱够了：
                    将商品添加到购物车
                    钱包余额减去商品的钱
                若钱不够
                    温馨：
            若不存在
                温馨提示：
            非法输入：
        退出：
            打印购物小条
'''

import random

num=random.randint(1,3)
if num==1:
    print("恭喜您获得一张机械革命优惠券，凭此券买机械革命可打5折")
    num=num+3
    k=1
    pass
elif num==2:
    print("恭喜您获得一张卫龙辣条优惠券，凭此券买卫龙辣条可打3折")
    num=num+3
    k=1
    pass
elif num==3:
    print("恭喜您获得一张HUA WEI WATCH，凭此券买HUA WEI WATCH可打3折")
    num=num-2
    k=1
    pass


shop = [
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["洗衣机",3000],
    ["机械革命",5000],
    ["卫龙辣条",4.5],
    ["老干妈辣酱",20],
]

# 1.准备好钱包

money = input("亲输入您的初始余额：")
money = int(money)

# 2. 准备一个空的购物车
mycart = []


# 3.开始购物
sum_money=0
i  = 0
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop) or chose < 0: # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
            #如果有该商品的优惠券
            if (chose==num==1 or chose==num==4 or chose==num==5) and k>0:
                if chose==num==1:
                    if money>0.8 * shop[chose][1]:
                        money = money - 0.8*shop[chose][1]
                        sum_money=sum_money+0.8*shop[chose][1]
                        mycart.append(shop[chose])
                        k=k-1
                        print("您本次成功使用了一张优惠券")
                        print("恭喜，商品添加成功！您的余额为：￥", money)
                        pass
                    else:
                        print("温馨提示：即使使用优惠券您卡里的余额也不够！请买其他商品！")

                elif chose==num==4:
                    if money > 0.5 * shop[chose][1] :
                        money = money - 0.5*shop[chose][1]
                        sum_money = sum_money + 0.5 * shop[chose][1]
                        mycart.append(shop[chose])
                        k = k - 1
                        print("您本次成功使用了一张优惠券")
                        print("恭喜，商品添加成功！您的余额为：￥", money)
                        pass
                    else:
                        print("温馨提示：即使使用优惠券您卡里的余额也不够！请买其他商品！")
                elif chose==num==5:
                    if money > 0.3 * shop[chose][1]:
                        money = money - 0.3*shop[chose][1]
                        sum_money = sum_money+ 0.3* shop[chose][1]
                        mycart.append(shop[chose])
                        k = k - 1
                        print("您本次成功使用了一张优惠券")
                        print("恭喜，商品添加成功！您的余额为：￥", money)
                        pass
                    else:
                        print("温馨提示：即使使用优惠券您卡里的余额也不够！请买其他商品！")

            #如果没有该商品优惠券
            else:
                if money  > shop[chose][1]:
                    money = money - shop[chose][1]
                    sum_money = sum_money + shop[chose][1]
                    mycart.append(shop[chose])
                    print("恭喜，商品添加成功！您的余额为：￥",money)
                else:
                    print("温馨提示：您的银行卡余额不足，穷鬼！请买其他商品！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")

    i = i + 1

# 4. 打印结算购物小条

print("以下是您的购物小条，请拿好！！！！么么哒！")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    #sum_money=sum_money+value[1]
    print(key,value)
print("".center(30,"-"))
print("总计消费",sum_money)



'''
    登录系统，自动获得弹出获得的优惠券
    输入钱包金额
    输入要买的商品

    如果商品存在
        如果有该商品优惠券
            如果money>=商品价格*折扣
                可以购买商品
            如果money<商品价格*折扣
                不可以购买
        如果没有优惠券：
            如果money>=商品价格
                可以购买
            else：
                不可购买
    else：
        请重新输入



'''






