#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 079
"""

if __name__ == '__main__':
    s = []
    for i in range(3):
        s.append(input("请输入一个字符串："))

    print("排序前")
    print(s)
    s.sort();
    print("排序后")
    print(s)
