"""
作者：Oliver
功能实现要求：
    用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
    启动程序后：
        已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
                     登录过程中，用户密码输入超过三次则退出程序,
                     并将用户名添加到黑名单，再次启动程序登陆改用户名，提示用户禁止登陆
        未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
                     注册过程中，用户密码输入两次一样才可以注册
    允许用户根据商品编号购买商品，比如：
        1 iPhone
        2 mac book
        3 bike
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    可随时退出，退出时，打印已购买商品和余额
版本：1.0
时间：2019/01/31

超市：会员名称，密码，账户余额
account_dic = {"name": {"code":22}, }
三个列表:
name = [""]
pass_word = []
account_balance = []

name in dic1
    input code
    code in dic1[name]
        output: balance
    print(商品清单)

goods = {1:apple, 2: pear, 3: banana}
s= 0
item, qty = input 1,2,3和数量
s = goods[]
# name,code = input("请输入账户名和密码(以空格分开)：").split()
        # account = member(name, code)
        # print(account)
"""


# def member(name, code):
#     try_times = 3
#     while try_times > 0:
#         if name in name_lst:    # 账户存在
#             if code == code_lst[name_lst.index(name)]:  # 密码正确
#                 account = balance_account[name_lst.index(name)]
#             else:   # 密码不正确
#                 try_times -= 1
#                 name, code = input("请输入账户名和密码(以空格分开)：").split()
#                 continue
#         else:
#             print("账户名不存在!")
#             choice = input("重新输入请输：1 ，注册新账户请输：2 ！")
#             if choice == "1":
#                 name, code = input("请输入账户名和密码(以空格分开)：").split()
#                 member(name, code)
#             if choice == "2":
#                 account = account_reg(name, code)
#             break
#         return account
#     if try_times <= 0:
#         print("密码输错次数达到上限,该账户已被锁定！")
#         exit()


def main():
    name_lst = ["张三", "李四", "王五"]
    code_lst = ["123456", "456789", "789012"]
    balance_account = [10000, 10000, 10000]

    print("是否已注册会员?")
    is_reg = input("是请输入:Y，否请输入: N")
    if is_reg == "Y":
        pass
    while is_reg == "N":
        name = input("请输入账户名：")
        while name not in name_lst and len(name) > 0:  # 账户确认，非空
            code = input("请输入密码：")
            while len(code) > 0:
                code_1 = input("请再输入一次密码！")
                while code_1 == code :  # 密码确认
                    name_lst.append(name)
                    code_lst.append(code)
                    print("注册成功!")
                    account = input("请输入充值金额:")
                    while account.isnumeric():  # 确定输入值是数字
                        save_in = input("您当前充值金额为：{} RMB, 确认请输：1，更改请输入：2 !".format(account))
                        if save_in == "1":  # 充值金额确认
                            balance_account.append(float(account))
                            print(name_lst, code_lst, balance_account, balance_account[name_lst.index(name)])
                            exit()
                        else:
                            account = input("请输入充值金额:")
                            continue
                    else:
                        print("输入内容有误，请确认！")
                        continue
                        # 格式出错，会再次判断两次密码一致，再次把name和code加入两个列表
                else:
                    print("两次密码不一致,请重新输入！")
                    break
            else:
                print("密码不能为空！")
                continue
        else:
            print("账户已存在")
            exit()




# goods = []
# while True:
#     good = input("请输入商品名：")
#     numb = eval(input("请输入购买数量："))
#
#     if good in msg_dic and numb.isnumric():
#         goods.append((good, msg_dic[good],numb ))
#     else:
#         print("请重新输入！")
#         continue
if __name__ == "__main__":
    main()






