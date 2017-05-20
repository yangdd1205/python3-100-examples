#!/usr/bin/python3


__author__ = "yang.dd"

"""
    example 096
"""

if __name__ == "__main__":
    str1 = input("请输入一个字符串：")
    str2 = input("请输入一个子字符串：")
    print("%s中出现%s共%s次" % (str1,str2,str1.count(str2)))