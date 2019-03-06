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
版本：2.0
时间：2019/02/15

"""

account_dic = {"张三": "123456", "李四": "23456", "王二": "34567" }
balance_account = {"张三": 10000, "李四": 10000, "王二": 10000 }
goods_dic = {"1": ("进口凤梨", 25),
            "2": ("荷兰青啤梨", 5),
            "3": ("椰青泰国椰子", 10),
            "4": ("新西兰红玫瑰Queen苹果", 6),
            "5": ("南非夏橙", 3)}


def account_reg(name):
    """非会员注册"""
    while name not in account_dic and len(name) > 0:  # 账户确认，非空
        code = input("请输入密码：")
        while len(code) > 0:
            code_1 = input("请再输入一次密码！")
            while code_1 == code:  # 密码确认
                account_dic[name] = code
                print("注册成功!")
                account_in = input("请输入充值金额:")
                while account_in.isnumeric():  # 确定输入值是数字
                    save_in = input("您当前充值金额为：{} RMB, 确认请输：1，更改请输入：2 !".format(account_in))
                    if save_in == "1":  # 充值金额确认
                        balance_account[name] = eval(account_in)
                        account = balance_account[name]
                        print("您的账户:{}成功充值金额{}".format(name, balance_account[name]))
                        return account
                    else:
                        account_in = input("请输入充值金额:")
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
        account = member(name)
    return account


def member(name):
    """会员显示账户余额"""
    try_times = 3
    while try_times > 0:
        if name in account_dic:    # 账户存在
            code = input("请输入密码：")
            if code == account_dic[name]:  # 密码正确
                account = balance_account[name]
                print("您的账户余额为：{}".format(balance_account[name]))
                return account
            else:   # 密码不正确
                try_times -= 1
                print("密码错误！请确认！")
                continue
        else:
            print("账户名不存在!")
            choice = input("重新输入请输：1 ，注册新账户请输：2 ！")
            if choice == "1":
                name = input("请输入账户名：")
            if choice == "2":
                account = account_reg(name)  # 注册账户
                return account
    if try_times <= 0:
        print("密码输错次数达到上限,该账户已被锁定！")
        exit()


def purchase_goods(good):
    amount = 0
    while good in goods_dic.keys():
        number = input("请输入数量:")
        if number.isnumeric():
            amount += goods_dic[good][1] * eval(number)
            return amount
        else:
            print("输入内容有误，请确认！")
            continue


def account_check(is_reg):  # 是否已注册
    while True:
        if is_reg == "Y":
            name = input("请输入账户名：")
            account = member(name)
            print("商品编号及单价\n", goods_dic)
            return account
        while is_reg == "N":
            name = input("请输入账户名：")
            account = account_reg(name)
            print("商品编号及单价\n",goods_dic)
            return account
        else:
            print("输入不符合要求，请重新输入！")
            is_reg = input("是否已注册会员?\n 是请输入:Y，否请输入: N")
            continue


def main():

    amount = 0
    purchase_dic = {}
    print("是否已注册会员?")
    is_reg = input("是请输入:Y，否请输入: N")
    account = account_check(is_reg)
    while amount <= account:
        good_no = input("请输入商品编号")
        good = goods_dic[good_no][0]    #编号对应的商品
        purchase_dic[good] = purchase_dic.get(good, 0) + purchase_goods(good_no)
        # 购买商品及其总价格
        for i in purchase_dic.values():
            amount += i
        check_tag = input("继续选购请输入：1，结束选购并结账请输入：2，\
        更改选购商品请输入：3，放弃选购退出请输入：4")
        if check_tag == "1":
            continue
        elif check_tag == "2":
            for x, y in purchase_dic.items():
                for key in goods_dic.values():
                    if x == key[0]:
                        print("{},数量{}，金额{}RMB".format(x, y / key[1], y))
                    else:
                        continue
            print("本次消费{}RMB,当前账户余额{}RMB,谢谢惠顾！".format(amount, account - amount))
            exit()
        elif check_tag == "4":
            print("谢谢惠顾！")
            exit()
        while check_tag == "3":
            print("您已选购{},合计{}RMB".format(purchase_dic, amount))
            print(goods_dic)
            good_no = input("请输入商品编号")
            good = goods_dic[good_no][0]
            purchase_dic[good] = purchase_dic.get(good, 0) - purchase_goods(good_no)
            for i in purchase_dic.values():
                amount += i
            check_tag_2 = input("继续选购请输入：1，结束选购并结账请输入：2,\
                    更改选购商品请输入：3，放弃选购退出请输入：4")
            if check_tag_2 == "1":
                break
            elif check_tag_2 == "2":
                # 显示购买商品和数量，以及总金额！！
                for x, y in purchase_dic.items():
                    for key in goods_dic.values():
                        if x == key[0]:
                            print("{},数量{}，金额{}RMB".format(x, y/key[1], y))
                        else:
                            continue
                print("本次消费{}RMB,当前账户余额{}RMB,谢谢惠顾！".format(amount, account - amount))
                exit()
            elif check_tag_2 == "4":
                print("谢谢惠顾！")
                exit()
            elif check_tag_2 == "3":
                continue
    else:
        print("账户余额不足！")
        exit()


if __name__ == "__main__":
    main()






