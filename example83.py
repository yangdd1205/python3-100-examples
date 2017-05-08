#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 083

    排列组合
    1位数：只有1,3,5,7。4种情况
    2位数：有 4 * 7 种情况（首位数字不为0）。
    3位数：有 4 * 8 * 7 种情况。
    4位数：有 4 * 8 * 8 *7 种情况
    ......
"""

if __name__ == "__main__":
    sum, count = 0, 0
    for i in range(1, 9):
        if i == 1:
            count = 4
        elif i == 2:
            count *= 7
        else:
            count *= 8
        sum += count
    print(sum)
