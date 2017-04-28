#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 074
"""

if __name__ == '__main__':
    a = list(range(1, 4))
    print(a)
    b = list(range(4, 8))
    print(b)
    print('使用+：', a + b)
    a.extend(b)
    print("使用extend方法：", a)
    a = list(range(1, 4))
    b = list(range(4, 8))
    a.append(b)
    print("使用append方法：", a)
    a = list(range(1, 4))
    b = list(range(4, 8))
    a[len(a):len(a)] = b
    print("使用切面：", a)
