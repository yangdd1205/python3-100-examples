#!/usr/bin/python3

from sys import stdout

__author__ = "yang.dd"

"""
    example 097
"""

if __name__ == "__main__":
    filename = input("请输入一个文件名：")
    fp = open(filename, "w")
    ch = input("请输入内容：")
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()
