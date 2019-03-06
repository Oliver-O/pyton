"""
作者:Oliver
功能：金字塔星星
日期：20190120
版本：1.0
"""
level = 5
for current_level in range(1, level + 1):
    for i in range(level - current_level):
        print(" ", end="")
    for j in range(2 * current_level - 1):
        print("*", end="")
    print()





