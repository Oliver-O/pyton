"""
姓名:oliver
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
时间: 2019/03/08

"""


def str_analysis(key_in):
    num_count = 0
    alp_count = 0
    spa_count = 0
    other_count = 0
    for i in key_in:
        if i.isnumeric():
            num_count += 1
        elif i.isalpha():
            alp_count += 1
        elif i.isspace():
            spa_count += 1
        else:
            other_count += 1

    print("该段文字中，总计字符{}个，其中：\n【数字】{}个，\n【字母】{}个，\n【空格】{}个，\n【其他】{}个！". \
          format(num_count + alp_count + spa_count + other_count, num_count, alp_count, spa_count, other_count))


def len_check(key_in):
    key = eval(key_in)
    if len(key) > 5:
        print("输入内容长度大于5")
    else:
        print("输入内容长度不大于5")


def lst_in_check(key_in):
    try:
        lst_in = eval(key_in)
        while type(lst_in) == list:
            if len(lst_in) > 2:
                lst_out = lst_in[:2]
                print(lst_out)
                exit()
            else:
                print("列表长度不大于2！")
                exit()
        else:
            print("输入内容非列表！")
    except SyntaxError:
        print("输入内容非列表！")


def odd_items(key_in):
    try:
        key = eval(key_in)
        out_put = []
        while type(key) == list or type(key) == tuple:
            for i in key:
                if key.index(i) % 2 == 0:
                    continue
                else:
                    out_put.append(i)
            print(out_put)
            exit()
        else:
            print("输入内容非列表或元组！")
    except SyntaxError:
        print("输入内容非列表或元组！")


def len_dic_value(key_in):
    try:
        item = eval(key_in)
        out_put = {}
        while type(item) == dict :
            if len(item) > 2:
                for k in item.keys():
                    if type(item[k]) == str or type(item[k]) == list:
                        out_put[k] = item[k]
                        if len(out_put) < 2:
                            continue
                        elif len(out_put) == 2:
                            print(out_put)
                            exit()
                        else:
                            exit()
                    else:
                        print("字典中的值包含，非字符串或列表元素！")
                        exit()
            else:
                print("字典长度不大于2！")
                exit()
        else:
            print("输入内容不是字典！")
            exit()
    except SyntaxError:
        print("输入内容不是字典！")
        exit()


def main():
    key_in = input("请输入需分析的内容：")
    # str_analysis(key_in)
    # len_check(key_in)
    # lst_in_check(key_in)
    # odd_items(key_in)
    len_dic_value(key_in)


if __name__ == "__main__":
    main()

