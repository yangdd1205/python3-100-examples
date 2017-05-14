#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 089
"""

if __name__ == "__main__":
    n = input("请输入原文：")
    a = []
    for i in n:
        a.append((int(i) + 5) % 10)
    a[0], a[3] = a[3], a[0]
    a[1], a[2] = a[2], a[1]
    result = "".join(str(x) for x in a)
    print("密文：" + result)
