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
时间：2019/02/17

"""
import os

goods_dic = {"1": ("进口凤梨", 25),
             "2": ("荷兰青啤梨", 5),
             "3": ("椰青泰国椰子", 10),
             "4": ("新西兰红玫瑰Queen苹果", 6),
             "5": ("南非夏橙", 3)}


# 获取白名单和黑名单
with open("white_list.txt", "r", encoding="utf-8") as white_r, \
        open("black_list.txt", "r", encoding="utf-8") as black_r:
    account_dic_b = {}
    balance_account_b = {}
    account_dic_w = {}
    balance_account_w = {}
    balance_account_0 = {}
    # 获取黑名单
    for line in black_r.readlines():
        l = line.strip().split("|")
        for i in range(2):
            # 将账户信息放入字典
            name_b = l[0]
            account_dic_b[name_b] = l[1]
            balance_account_b[name_b] = l[2]
    # 获取白名单
    for line in white_r.readlines():
        l = line.strip().split("|")
        for i in range(2):
            # 将账户信息放入字典
            name_w = l[0]
            account_dic_w[name_w] = l[1]
            balance_account_w[name_w] = l[2]
    account_0 = tuple(balance_account_w.keys())
    balance_0 = tuple(balance_account_w.values())


def write_in_white(name):
    """非黑,非白,写白"""
    # 判定账户名不在黑名单
    while name not in account_dic_b.keys() and len(name) > 0:  # 账户确认，非空
        while name not in account_dic_w.keys():  # 不在白名单,加入白名单
            code = input("请输入密码：")
            while len(code) > 0:
                code_1 = input("请再输入一次密码！")
                while code_1 == code:  # 密码确认
                    account_dic_w[name] = code
                    print("注册成功!")
                    balance = top_up(name)  # 充值
                    balance_account_w[name] = balance
                    code, balance, tag = pur_process(name, float(balance))
                    return code, balance, tag
                else:
                    print("两次密码不一致,请重新输入！")
                    break
            else:
                print("密码不能为空！")
                continue
        else:
            print("账户已存在")
            password, balance, tag = account_process(name)
        return password, balance, tag
    else:
        print("账户已锁定")
        exit()


def top_up(name):
    while True:
        key_in = input("请输入充值金额:")
        if key_in.isnumeric():
            money_plus = eval(key_in)
            while money_plus >= 0:
                save_in = input("您当前充值金额为：{} RMB, 确认充值请输：1, 更改充值金额请输入：2 !".format(key_in))
                if save_in == "1":  # 充值金额确认
                    balance_account_w[name] = balance_account_w.get(name, 0) + eval(key_in)
                    balance = balance_account_w[name]
                    print("您的账户:{}成功充值金额{}RMB".format(name, balance_account_w[name]))
                    return balance
                elif save_in == "2":
                    break
            else:
                print("充值金额，不能为负数，请请确认！")
                break
        else:
            print("输入内容有误，请确认！")
            continue


def account_process(name):
    """非黑,白, 读白写黑"""
    while name not in account_dic_b.keys() and len(name) > 0:  # 非黑
        # 三次验证
        try_times = 3
        while try_times > 0:
            if name in account_dic_w.keys():  # 账户在白名单
                code = input("请输入密码：")
                if code == account_dic_w[name]:  # 密码正确
                    balance = eval(balance_account_w[name])
                    print("您的账户余额为：{}RMB".format(balance_account_w[name]))
                    code, balance, tag = pur_process(name, balance)      # 开始购物
                    return code, balance, tag
                else:  # 密码不正确
                    try_times -= 1
                    print("密码错误！请确认！")
                    continue
            else:       # 非白
                print("账户名不存在!")
                choice = input("重新输入请输：1 ，注册新账户请输：2 ！")
                if choice == "1":
                    name = input("请输入账户名：")
                if choice == "2":
                    password, balance, tag = write_in_white(name)  # 注册账户
                    return password, balance, tag
        # 密码验证失败
        if try_times <= 0:
            print("密码输错次数达到上限,该账户已被锁定！")
            # 写入黑名单
            tag = "3"
            password = account_dic_w[name]
            balance = balance_account_w[name]
            return password, balance, tag
    else:
        print("账户已锁定")
        exit()


def pur_process(name, balance):
    amount_s = 0
    purchase_dic = {}
    while amount_s <= balance:
        print("商品编号及单价\n", goods_dic)
        check_tag = input("选购请输入：1，结束选购并结账请输入：2，\
                         放弃所有选购退出请输入：3")
        while check_tag == "1":
            good_no = input("请输入商品编号")
            good = goods_dic[good_no][0]  # 编号对应的商品
            amount = purchase_goods(good_no)  # 此次购买费用
            purchase_dic[good] = purchase_dic.get(good, 0) + amount  # 这一商品总费用
            if purchase_dic[good] > 0:  # 选购某一商品总数不能为负数
                amount_s = 0
                for i in purchase_dic.values():  # 已经购买商品及其总价格
                    amount_s += i
                if amount_s <= balance:     # 判断余额够，扣款，不够提醒
                    check_tag_1 = input("选购请输入：1，结束选购并结账请输入：2，\
                     放弃所有选购退出请输入：3")
                    if check_tag_1 == "1":
                        continue
                    elif check_tag_1 == "2":
                        for x, y in purchase_dic.items():
                            for key in goods_dic.values():
                                if x == key[0]:
                                    print("{},数量{}个，金额{}RMB".format(x, y / key[1], y))
                                else:
                                    continue
                        print("本次消费{}RMB,当前账户余额{}RMB,谢谢惠顾！".format(amount_s, balance - amount_s ))
                        # 更改白名单账户余额内容
                        balance = balance - amount_s
                        password = account_dic_w[name]
                        tag = "2"
                        return password, balance, tag

                    elif check_tag_1 == "3":
                        print("谢谢惠顾！")
                        password = account_dic_w[name]
                        balance = balance_account_w[name]
                        tag = "2"
                        return password, balance, tag

                else:       # 余额不够提醒
                    print("账户余额不足！")
                    purchase_dic[good] = purchase_dic.get(good, 0) - amount
                    check_tag_2 = input("重新选购请输入：1，结束选购并结账请输入：2，\
                                     放弃所有选购退出请输入：3， 充值请输入：4")
                    if check_tag_2 == "1":
                        continue
                    elif check_tag_2 == "2":
                        for x, y in purchase_dic.items():
                            for key in goods_dic.values():
                                if x == key[0]:
                                    print("{},数量{}，金额{}RMB".format(x, y / key[1], y))
                                else:
                                    continue
                        print("本次消费{}RMB,当前账户余额{}RMB,谢谢惠顾！".format(amount_s - amount, balance - amount_s + amount))
                        # 更改白名单账户余额内容
                        balance = balance - amount_s + amount
                        password = account_dic_w[name]
                        tag = "2"
                        return password, balance, tag
                    elif check_tag_2 == "3":
                        print("谢谢惠顾！")
                        password = account_dic_w[name]
                        balance = balance_account_w[name]
                        tag = "2"
                        return password, balance, tag
                    elif check_tag_2 == "4":
                        balance_account_w[name] = balance - amount_s + amount
                        balance = top_up(name)
                        break
            else:
                print("选购某一商品总数不能为负,请再次确认！")
                purchase_dic[good] = purchase_dic.get(good, 0) - amount
                break
        while check_tag == "2":
            for x, y in purchase_dic.items():
                for key in goods_dic.values():
                    if x == key[0]:
                        print("{},数量{}，金额{}RMB".format(x, y / key[1], y))
                    else:
                        continue
            print("本次消费{}RMB,当前账户余额{}RMB,谢谢惠顾！".format(amount_s, balance - amount_s))
            # 更改白名单账户余额内容
            balance = balance - amount_s
            password = account_dic_w[name]
            tag = "2"
            return password, balance, tag
        while check_tag == "3":
            print("谢谢惠顾！")
            password = account_dic_w[name]
            balance = balance_account_w[name]
            tag = "2"
            return password, balance, tag


def purchase_goods(good):
    amount = 0
    while good in goods_dic.keys():
        number = input("请输入数量:")
        if number.isnumeric():     # 无法识别负数
            amount += goods_dic[good][1] * eval(number)
            return amount
        else:
            print("输入内容有误，请确认！")
            continue


def main():
    name = input("请输入账户名：")

    password, balance, tag = account_process(name)

    if tag == "2":     # 账户内容变更
        with open("white_list.txt", "r", encoding="utf-8") as read_w, \
                open("white_w.txt", "w", encoding="utf-8") as write_w:
            read_w.seek(0)
            f = read_w.read()
            if name in f:
                s = f.replace("{}|{}|{}\n".format(name, password, balance_0[account_0.index(name)]),
                              "{}|{}|{}\n".format(name, password, balance))
            else:
                s = f + "{}|{}|{}\n".format(name, password, balance)
            write_w.write(s)
        os.remove("white_list.txt")
        os.rename("white_w.txt", "white_list.txt")
        exit()

    elif tag == "3":     # 密码错误黑名单
        with open("white_list.txt", "r", encoding="utf-8") as read_w, \
                open("white_w.txt", "w+", encoding="utf-8") as write_w, \
                open("black_list.txt", "a", encoding="utf-8") as write_b:
                #  写入黑名单
                write_b.write("{}|{}|{}\n".format(name, account_dic_w[name], balance_account_w[name]))
                # 白名单删除
                f = read_w.read()
                s = f.replace("{}|{}|{}\n".format(name, account_dic_w[name], balance_account_w[name]), "")
                write_w.write(s)
        # 更改名字
        os.remove("white_list.txt")
        os.rename("white_w.txt", "white_list.txt")
        exit()


if __name__ == "__main__":
    main()



