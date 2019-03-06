"""
作者:Oliver
功能：用户输入密码比对账户信息
日期：20190120
版本：1.0
"""
name_tup = ("a", "b", "c")
password_tup = ("123", "234", "345")
input_times = {"a": 0, "b": 0, "c": 0}
name = input("请输入你的账户：")
while input_times[name] < 3:
    password = input("请输入你的密码：")
    if name in name_tup:
        if password == password_tup[name_tup.index(name)]:
            print("登陆成功！")
            exit()
        else:
            print("密码错误！")
            input_times[name] = input_times.get(name, 0) + 1

if input_times[name] >= 3:
    print("错误次数达到上限，账户已锁定！")




