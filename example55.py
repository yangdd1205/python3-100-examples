#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 055
       ~ 运算符 转为二进制 按补码计算 取反 1为0,0为1
    0000 0010
    ——————————
    1111 1101 
"""

if __name__ == '__main__':
    a = 2   # 0000 0010
    b = ~a  # 1111 1101
    print('a = %d，~a=%d' % (a, b))
    a = -2  # 1111 1110
    b = ~a  # 0000 0001
    print('a = %d，~a=%d' % (a, b))
