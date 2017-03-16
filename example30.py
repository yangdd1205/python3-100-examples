#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 030
'''

a = int(input("请输入一个数字："))

s = str(a)

if s == s[::-1]:
	print(s,"是回文数")
else:
	print(s,'不是回文数')