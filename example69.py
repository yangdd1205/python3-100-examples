#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 069
"""

if __name__ == '__main__':
    n = int(input("请输入参与的人数："))
    # p = list(range(1, n + 1))
    p = [x for x in range(1, n + 1)]

    i = 0
    s = 1
    while len(p) > 1:
        if i > len(p) - 1:
            i = 0
        if s % 3 == 0:
            p.pop(i)
            s = 1
            continue
        s += 1
        i += 1
    print(p.pop())
