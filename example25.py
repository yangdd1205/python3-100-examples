#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 025
'''

s = 1
total = 0
for i in range(1,21):
	s *= i # 每个阶乘的值
	total += s
	

	
print(total)