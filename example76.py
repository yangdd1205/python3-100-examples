#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 076
"""


def peven(n):
    result = 0
    for i in range(2, n + 1, 2):
        result += 1 / i
    return result


def podd(n):
    result = 0
    for i in range(1, n + 1, 2):
        result += 1 / i
    return result;


def dcall(fp, n):
    result = fp(n)
    return result


if __name__ == '__main__':
    n = int(input("请输入一个大于零整数："))
    if n > 0:
        if n % 2 == 0:
            print(dcall(peven, n));
        else:
            print(dcall(podd, n));
    else:
        print("请输入一个大于零的整数。")
