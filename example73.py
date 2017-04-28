#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 073
"""

if __name__ == '__main__':
    num = []
    for i in range(3):
        num.append(int(input("请输入一个数字：")))
    print(num)
    num.reverse()
    print(num)
    print(num[::-1])