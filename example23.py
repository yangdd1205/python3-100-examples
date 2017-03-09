#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 023
	
	Python的内置方法 str.center(width [, fillchar]) 
	str最中心的字符 ，width即打印的最大宽度，fillchar：其他位置填充的字符，默认填充字符就是空格。 如果width小于或等于len（s），则返回原始字符串
'''

s = '*'
for i in range(1, 8, 2):
    print((s*i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s*i).center(7))