#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 019
'''

import math



# 先构造一个从3开始的奇数序列

def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n

		
# 定义一个筛选函数
def _not_divisible(n):
	return lambda x : x % n >0
  
#  定义一个生成器，不断返回素数
def primes():
	yield 2
	it = _odd_iter() # 初始化序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
		
		
list=[]

for p in primes():
	if p < 1000:
		list.append(p)
	else:
		break

'''
如果p是质数，且2^p-1也是质数，那么（2^p-1）X2^（p-1）便是一个完全数。
'''
for p in range(1,10):
	if (p in list) and (pow(2,p)-1 in list):
		num1 = pow(2,p)-1
		num2 = pow(2,p-1)
		print('完数：',num1*num2)