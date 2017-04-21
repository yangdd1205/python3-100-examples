#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 066
"""

if __name__ == '__main__':
    nums = []
    for i in range(3):
        nums.append(int(input("请输入一个数字：")))
    nums.sort()
    print("按顺序排列：", nums)
    nums.reverse()
    print("按倒叙排列：", nums)
