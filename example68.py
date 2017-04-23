#!/usr/bin/python3

from collections import deque

__author__ = "yang.dd"

"""
    example 068
"""


def move1(number, m):
    m -= 1
    after = number[0:m]
    before = number[m:len(number)]
    return before + after


def move2(number, m):
    d = deque(number)
    d.rotate(m)
    return list(d)


if __name__ == '__main__':
    n = int(input("请输入数字总个数："))
    m = int(input("请输入要移动的结束位置："))
    number = []
    for i in range(n):
        number.append(int(input("请输入一个数字：")))
    print("原数据：", number)
    number = move1(number, m)
    # number = move2(number, m)
    print("移动过后：", number)
