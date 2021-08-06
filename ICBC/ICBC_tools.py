Bank=[] #存放用户字典的列表

def show_menu():
    print("*"*50)
    print("*           中国工商银行                         *")
    print("*           账户管理系统                         *")
    print("*           V1.0                                 *")
    print("*" * 50)
    print("*           1.开户                               *")
    print("*           2.存钱                               *")
    print("*           3.取钱                               *")
    print("*           4.转账                               *")
    print("*           5.查询                               *")
    print("*           6.Bye！                              *")
    print("*" * 50)


def open_account():
    """开户"""
    #检查用户库是否已满，若满了则返回“用户库已满”
    if len(Bank)>=100:
        print("3 用户库已满，无法再添加用户")
    else:
        account=input("请输入账号：")
        name=input("请输入用户名：")
        password=input("请输入账号密码：")
        address=input("请输入用户地址：")
        money=input("请输入用户存款：")
        open_bank=input("请输入开户行：")
        user_dict={"account":account,
                   "name":name,
                   "password":password,
                   "address":address,
                   "money":money,
                   "open_bank":open_bank}
        for card_dict in Bank:
            if card_dict["account"]==account:
                print("2  该用户已经存在")
                break
        else:
            Bank.append(user_dict)
            print("1  您已经成功添加该用户！")


def save_money():
    """存钱"""
    account=input("请输入您的账号：")
    for dict in Bank:
        if dict["account"]==account:
            money=input("请输入您的存款金额：")
            dict["money"]=int(dict["money"])+int(money)
            print("存款成功")
            break
    else:
        print("没有您的账户信息")


def withdraw_money():
    """取钱"""
    account=input("请输入您的账号：")
    for dict in Bank:
        if dict["account"]==account:
            password = input("请输入您的账号密码：")
            if dict["password"]==password:
                money=input("请输入您的取款金额：")
                if int(dict["money"])>=int(money):
                    dict["money"]=int(dict["money"])-int(money)
                    print("取款成功")
                    break
                else:
                    print("余额不足！")
                    break
            else:
                print("您输入的密码不正确！")
                break
    else:
        print("您的账户信息不存在！")


def transfer_accounts():
    """转账"""
    out_account=input("请输入转出账号：")
    in_account=input("请输入转入账号：")
    for dict1 in Bank: # for dict in bank：
        # if all(i["account"]==out_account, i["account"] == in_account) is True:
        if dict1["account"]==out_account:
            for dict2 in Bank:
                if dict2["account"]==in_account:
                    password=input("请输入转出账号的密码：")
                    if dict1["password"]==password:
                        money=input("请输入要转出的金额：")
                        if int(money)<=int(dict1["money"]):
                            dict1["money"]=int(dict1["money"])-int(money)
                            dict2["money"]=int(dict2["money"])+int(money)
                            print("您已经成功将金额转出！当前账户余额为：",int(dict1["money"]))
                            return
                            #exit()
                        else:
                            print("当前账户余额不足！ 账户余额为：",int(dict1["money"]))
                            break
                    else:
                        print("密码错误！")
                        break
            else:
                print("转入账户不存在！")
                break
    else:
        print("转出账户不存在")

# def transfer_accounts():
#     """转账"""
#     out_account=input("请输入转出账号：")
#     in_account=input("请输入转入账号：")
#     for dict1,dict2 in Bank:
#         if (dict1["account"]==out_account and dict2["account"] == in_account) is True:
#             password=input("请输入转出账号的密码：")
#             if dict1["password"]==password:
#                 money=input("请输入要转出的金额：")
#                 if int(money)<=int(dict["money"]):
#                     dict1["money"]=int(dict1["money"])-int(money)
#                     dict2["money"]=int(dict2["money"])+int(money)
#                     print("您已经成功将金额转出！当前账户余额为：",int(dict1["money"]))
#                     break
#                 else:
#                     print("当前账户余额不足！ 账户余额为：",int(dict1["money"]))
#                     break
#             else:
#                 print("密码错误！")
#                 break
#     else:
#         print("转入或转出账号不存在！")


def querry():
    """查询"""
    account=input("请输入账号：")
    for dict in Bank:
        if dict["account"]==account:
            password=input("请输入账号密码：")
            if dict["password"]==password:
                print(dict)
                break
            else:
                print("密码错误！")
                break
    else:
        print("该用户不存在！")