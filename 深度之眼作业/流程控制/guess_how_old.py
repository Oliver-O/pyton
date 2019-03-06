"""
作者:Oliver
功能：猜年龄,
日期：20190120
版本：1.0
"""
answer = 36
guess_times = 3
while guess_times > 0:
    guess_in = eval(input("请输入你认为的当前中国人口劳动力平均年龄："))
    if guess_in == answer:  # 猜对退出
        print("《中国人力资本报告2018》显示：截止2016年，中国劳动力人口的平均年龄已经达到35.9岁！你猜对了！")
        exit()
    else:
        guess_times -= 1
        if guess_times <= 0:    # 猜错三次，询问是否继续？
            print("抱歉，你的猜测与近期调查结果不一致！还要再猜吗？")
            try_again = input("继续 请输入：Y, 退出 请输入：N")
            if try_again == "Y" or try_again == "y":
                guess_times = 3     # 继续，则猜测次数重置
                continue
            elif try_again == "N" or try_again == "n":
                print("结束游戏！")
                exit()





