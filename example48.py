#!/usr/bin/python3

'''
	example 048
'''

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))

if a > b:
	print('%d > %d' % (a,b))
elif a < b:
	print('%d < %d' % (a,b))
else:
	print('%d = %d' % (a,b))