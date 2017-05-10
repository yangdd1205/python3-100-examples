#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 085
"""

if __name__ == "__main__":
    b = int(input("请输入一个数字："))
    n = 9
    count = 1
    while True:
        if (n % b == 0):
            break
        else:
            n = n * 10 + 9
            count += 1
    print("%d可以被%d个9整除" % (b, count))
