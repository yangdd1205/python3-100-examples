#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 018
'''

from functools import reduce

def add(x,y):
	n = x*10+y
	list.append(n)
	return n

n = int(input('请输入一个数值：'))

leap= int(input('请输入需要相加的次数：'))

list=[n]

basicList=[n]*leap

# 生成需要相加的list
reduce(add,basicList)

total = sum(list)

print('total:',total)	