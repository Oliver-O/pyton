"""
姓名:oliver
1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
"""


def file_alter(name):
    import os

    try:
        with open("{}.txt".format(name), "r", encoding="utf-8") as read_f, \
            open("temp.txt", "w", encoding="utf-8") as write_f:
                read_f.seek(0)
                source_str = read_f.read()
                while True:
                    str_0 = input("请输入，您要修改的文字内容：")
                    str_1 = input("您要把这些文字改为：")
                    check = input("您要把“{}”修改为“{}”？确认修改请输入1，变更修改内容请输入2，放弃修改请输入3.".format\
                                      (str_0, str_1))
                    if check == "3":
                        print("您取消了对文件{}的修改。".format(name))
                        exit()
                    elif check == "2":
                        continue
                    elif check == "1":
                        target_str = source_str.replace(str_0, str_1)
                        write_f.write(target_str)
                        print("修改成功！")
                        break
        os.remove("{}.txt".format(name))
        os.rename("temp.txt", "{}.txt".format(name))
        exit()
    except FileNotFoundError:
        print("无此文件！")
        exit()



def main():
    name = input("请输入您要修改内容的文件名：")
    file_alter(name)


if __name__ == "__main__":
    main()

