"""
作者：Oliver
功能：练习
日期：20190120
版本：1.0
"""
# 集合交并补差
# pythons={'albert','孙悟空','周星驰','朱茵','林志玲'}
# ais={'猪八戒','郭德纲','林忆莲','周星驰'}
# print(pythons & ais)
# print(pythons | ais)
# print(pythons - ais)
# print(pythons ^ ais)
# # 1. 求出即报名python又报名ai课程的学员名字集合
# # 2. 求出所有报名的学生名字集合
# # 3. 求出只报名python课程的学员名字
# # 4. 求出没有同时这两门课程的学员名字集合

# 去重
# 1. 有列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，去重，得到新列表,且新列表无需保持列表原来的顺序
# 2.在上题的基础上，保存列表原来的顺序
# 3.去除文件中重复的行，肯定要保持文件内容的顺序不变(后面的章节会讲文件操作)
# 4.有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序

# l=['a','b',1,'a','a']
# s = set(l)
# l2 = list(s)
# print(l2)
# 去重且保持原先列表的顺序
# l=['a','b',1,'a','a']
# l2 = []
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)
# s='hello alex alex say hello sb sb'
# ls = s.split()
# words_sum = {}
# for i in ls:
#     if i in words_sum:
#         words_sum[i] += 1
#     else:
#         words_sum[i] = 1
# print(words_sum)
# s='hello alex alex say hello sb sb'
# dic={}
# words=s.split()
# for word in words: #word='alex'
#     dic.setdefault(word,s.count(word))
# print(dic)
"""
简单购物车,要求如下：
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
"""
# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
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


# name = " alberT"
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# result = name.startswith("al")
# result = name.endswith("T")
# print(result)
# print(name.replace("l", "p"))
# print(name.split("l"))
# print(name.upper())
# print(name.lower())
# print(name[1])
# print(name[:3])
# print(name[-2:])

# data=['albert',18,[2000,1,1]]
# name = data[0]
# age = data[1]
# birth_year = data[2][0]
# birth_month = data[2][1]
# birth_date = data[2][2]
#
# print(name,age,birth_year,birth_month,birth_date)
# """
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
#
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# """
# list_a = [11,22,33,44,55,66,77,88,99,90]
# a = {"k1":[], "k2":[]}
# for i in list_a:
#     if i > 66:
#         a["k1"].append(i)
#     else:
#         a["k2"].append(i)
# print(a)
# import os
#
# with open("a.txt", "r", encoding="utf-8") as f_a,\
#         open("data_2.txt", "w", encoding="utf-8") as f_b:
#     # data_2.txt 文件并不事先存在
#     set_a = set()
#     for line in f_a:
#         if line not in set_a:
#             set_a.add(line)
#             f_b.write(line)
#     os.remove("a.txt")
#     os.rename("data_2.txt", "a.txt")
# l=[
#     {'name':'albert','age':18,'sex':'male'},
#     {'name':'alex','age':73,'sex':'male'},
#     {'name':'albert','age':20,'sex':'female'},
#     {'name':'albert','age':18,'sex':'male'},
#     {'name':'albert','age':18,'sex':'male'},
# ]
# l2 = []
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)



