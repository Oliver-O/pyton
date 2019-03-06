"""
参考答案
"""


import os

product_list = [
    ['IphoneXR', 9800],
    ['Coffee', 30],
    ['疙瘩汤', 10],
    ['Python Book', 99],
    ['Bike', 199],
    ['ViVo X20', 2499],
]

shopping_cart = {}
current_user_info = []

db_file = r'db.txt'

while True:
    print('''
1：登陆
2：注册
3：购物
    ''')

    choice = input('>>: ').strip()

    if choice == '1':
        # 1、登陆
        tag = True
        count = 0
        while tag:
            if count == 3:
                print('\033[45m尝试次数过多，退出。。。\033[0m')
                break
            username = input('用户名：').strip()
            password = input('密码：').strip()

            with open(db_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip('\n')
                    user_info = line.split('|')  # 返回分割后的字符串列表

                    username_of_db = user_info[0]
                    password_of_db = user_info[1]

                    if username == username_of_db and password == password_of_db:
                        print('\033[48m登陆成功\033[0m')
                        if len(user_info) == 3:
                            balance_of_db = user_info[2]
                            balance = balance_of_db
                            balance = int(balance)
                        else:
                            while True:
                                salary = input('请输入工资：').strip()
                                if not salary.isdigit(): continue
                                salary = int(salary)
                                balance = salary
                                break

                        # 登陆成功则将用户名和余额添加到列表
                        current_user_info = [username_of_db, balance]
                        print('用户信息为：%s,请选择3开始购物' % current_user_info)
                        tag = False
                        break
                else:
                    print('\033[47m用户名或密码错误\033[0m')
                    count += 1

    elif choice == '2':
        username = input('请输入用户名：').strip()
        while True:
            password1 = input('请输入密码：').strip()
            password2 = input('再次确认密码：').strip()
            if password1 == password2:
                print('注册成功，请选1开始登陆')
                break
            else:
                print('\033[39m两次输入密码不一致，请重新输入！！!\033[0m')

        with open(db_file, 'a', encoding='utf-8') as file:
            file.write('%s|%s\n' % (username, password1))
            file.flush()

    elif choice == '3':
        if not current_user_info:
            print('\033[49m请先登陆...\033[0m')
        else:
            # 登陆成功后，开始购物
            username_of_db = current_user_info[0]
            balance = current_user_info[1]

            print('尊敬的用户[%s] 您的余额为[%s],祝您购物愉快' % (
                username_of_db,
                balance
            ))

            tag = True
            while tag:
                for index, product in enumerate(product_list):
                    print(index, product)
                choice = input('输入商品编号购物，输入q退出>>: ').strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice < 0 or choice >= len(product_list): continue

                    product_name = product_list[choice][0]
                    product_price = product_list[choice][1]

                    if balance > product_price:
                        if product_name in shopping_cart:  # 原来已经购买过
                            shopping_cart[product_name]['count'] += 1
                        else:
                            shopping_cart[product_name] = {'product_price': product_price, 'count': 1}

                        balance -= product_price  # 扣钱
                        current_user_info[1] = balance  # 更新用户余额
                        print(
                            "Added product " + product_name + " into shopping cart,\033[42;1myour current\033[0m balance " + str(
                                balance))

                    else:
                        print("买不起，穷逼! 产品价格是{price},你还差{lack_price}".format(
                            price=product_price,
                            lack_price=(product_price - balance)
                        ))
                    print('your shopping cart is %s' % shopping_cart)
                elif choice == 'q':
                    print("""
                    ---------------------------------已购买商品列表---------------------------------
                    id          商品                   数量             单价               总价
                    """)

                    total_cost = 0
                    for i, key in enumerate(shopping_cart):
                        print('%20s%18s%18s%18s%18s' % (
                            i,
                            key,
                            shopping_cart[key]['count'],
                            shopping_cart[key]['product_price'],
                            shopping_cart[key]['product_price'] * shopping_cart[key]['count']
                        ))
                        total_cost += shopping_cart[key]['product_price'] * shopping_cart[key]['count']

                    print("""
                    您的总花费为: %s
                    您的余额为: %s
                    ---------------------------------end---------------------------------
                    """ % (total_cost, balance))

                    while tag:
                        inp = input('确认购买(yes/no?)>>: ').strip()
                        if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']: continue
                        if inp in ['Y', 'y', 'yes']:

                            # 将余额写入文件
                            src_file = db_file
                            dst_file = r'%s.swap' % db_file
                            with open(src_file, 'r', encoding='utf-8') as read_file, \
                                    open(dst_file, 'w', encoding='utf-8') as write_file:
                                for line in read_file:
                                    if line.startswith(username_of_db):
                                        user_info_line_list = line.strip('\n').split('|')
                                        balance_of_db = balance
                                        balance_of_db = str(balance_of_db)
                                        if len(user_info_line_list) == 2:
                                            user_info_line_list.append(balance_of_db)
                                        else:
                                            user_info_line_list[-1] = balance_of_db
                                        line = '|'.join(user_info_line_list) + '\n'

                                    write_file.write(line)
                            os.remove(src_file)
                            os.rename(dst_file, src_file)

                            print('购买成功，请耐心等待发货')

                        shopping_cart = {}
                        current_user_info = []
                        tag = False

                else:
                    print('输入非法')

    else:
        print('\033[33m非法操作\033[0m')