"""
作者：Oliver
功能实现要求：
    打印三级菜单如省，市，县，可以自由发挥
    可返回上一级
    可随时退出程序
版本：1.0
时间：2019/01/29

暂时放弃！列表结构，没考虑清楚，[str, [str,...]]怎么根据输入值，判定输出同一层后面的值
输出值的下标是：index(input()) + 1
"""

menu = ['蜥臀类恐龙(蜥臀目)',
            ['蜥脚类恐龙',
                ['马门溪龙', '迷惑龙(雷龙)', '腕龙', '梁龙', '峨嵋龙'],
             '兽脚类恐龙',
                ['霸王龙', '伶盗龙(迅猛龙)', '异特龙', '棘龙', '永川龙']
             ],
        '鸟臀类恐龙(鸟臀目)',
            ['鸟脚类恐龙',
                ['青岛龙', '慈母龙', '山东龙', '副栉龙', '禽龙'], '甲龙类恐龙',
                ['包头龙', '楯甲龙', '森林龙'], '剑龙类恐龙',
                ['剑龙', '华阳龙', '棘甲龙'], '角龙类恐龙',
                ['三角龙', '戟龙', '独角龙', '五角龙', '剑角龙'], '肿头龙类恐龙',
                ['冥河龙', '河神龙', '肿头龙']
             ]
        ]
# for i in menu:
#     print(i[0])
#     for j in i[1:]:
#         print(j[0])
#         for v in j[1:]:
#             print(v)
# with open("menu.txt", "r", encoding="utf-8") as f:
#     f = f.read().encode("utf-8").decode("utf-8-sig") # 文本文档有BOM头处理方法
#     f_lst = f.split("\n")
#     for item in f_lst:
#         menu.append(item.strip().split(" "))
#     print(menu)

tag = True
while tag:
    menu1 = menu
    for mu in menu1[:-1:2]:
        print(mu)   # 打印第一层,恐龙目

    choice1 = input('恐龙目>>: ').strip()   # 选择第一层
    if choice1 == "b":  # 输入b，则返回上一级
        break
    if choice1 == "q":  # 输入q，则退出整体
        tag = False
    if choice1 not in menu1:    # 输入内容不在menu1内，则继续输入
        continue

    while tag:  # 打印第2层,恐龙类
        menu2 = menu1[menu1.index(choice1) + 1]
        # 根据输入的目，后面一个列表元素的偶数序号为这个目的类
        for lei in menu2[:-1:2]:
            print(lei)

        choice2 = input('恐龙类>>: ').strip()  # 选择第2层
        if choice2 == "b":  # 输入b，则返回上一级
            break
        if choice2 == "q":  # 输入q，则退出整体
            tag = False
        if choice2 not in menu2:  # 输入内容不在menu2内，则继续输入
            continue

        while tag:  # 打印第3层,恐龙名
            menu3 = menu2[menu2.index(choice2) + 1]
            # 根据输入的类，后面一个列表元素的偶数序号为这个类的种
            for kind in menu3:
                print(kind)

            choice3 = input('恐龙名>>: ').strip()  # 选择第2层
            if choice3 == "b":  # 输入b，则返回上一级
                break
            if choice3 == "q":  # 输入q，则退出整体
                tag = False
            if choice3 not in menu3:  # 输入内容不在menu2内，则继续输入
                continue



