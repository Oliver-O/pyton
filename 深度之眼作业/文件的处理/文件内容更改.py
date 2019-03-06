
"""
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数，求出本次购物花费的总钱数
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

2. 修改文件内容，把文件中的mac都替换成linux
"""

import os
with open("a.txt", "r") as read_f:
    read_f = read_f.read()
    items = read_f.replace("\n", " ")
    item_lst = items.split()
    s = 0
    for i in range(1, len(item_lst) + 1, 3):
        amount = int(item_lst[i]) * int(item_lst[i+1])
        s += amount
    print("本次购物总金额为：", s)

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('mac','linux')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')
