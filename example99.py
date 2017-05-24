#!/usr/bin/python3


__author__ = "yang.dd"

"""
    example 099
"""

if __name__ == "__main__":
    f1 = open("test.txt", "r")
    f2 = open("test1.txt", "r")
    result = f1.read()
    result += f2.read()
    print(result)
    merge = open("merge.txt", "w")
    merge.write("".join(sorted(result)))
    print("合并结果已写入merge.txt文件中")
