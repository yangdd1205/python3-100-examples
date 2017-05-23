#!/usr/bin/python3


__author__ = "yang.dd"

"""
    example 098
"""

if __name__ == "__main__":
    fp = open("test.txt", "w")
    string = input("请输入一个字符串：")
    string = string.upper();
    fp.write(string)
    fp = open("test.txt", "r")
    print(fp.read())
    fp.close()
