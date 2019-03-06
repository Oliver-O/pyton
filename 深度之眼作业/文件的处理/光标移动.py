
"""
练习：基于seek实现动态监测文件中是否有新内容的添加
"""


import time
with open('a.txt', 'rb') as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if line:
            print(line.decode('utf-8'))
            print(f.tell())
        else:
            time.sleep(2)
            print(f.tell())
