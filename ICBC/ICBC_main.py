import ICBC.ICBC_tools

while True:
    #显示功能菜单
    ICBC.ICBC_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是是【%s】" % action_str)

    if action_str in ["1","2","3","4","5","6"]:
        if action_str=="1":
            ICBC.ICBC_tools.open_account()
        elif action_str=="2":
            ICBC.ICBC_tools.save_money()
        elif action_str == "3":
            ICBC.ICBC_tools.withdraw_money()
        elif action_str == "4":
            ICBC.ICBC_tools.transfer_accounts()
        elif action_str == "5":
            ICBC.ICBC_tools.querry()
        elif action_str == "6":
            print("退出系统！")
            break
    else:
        print("您输入的不正确，请重新输入：")


