#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'

'''
 example 006
'''

## 
def fib(n):
	i,a,b = 0,1,1
	while i < n:
		yield a
		a,b = b,a+b
		i+=1
	return 'done'

def showFib():
	n = int(input("要查看第几位数？"))
	g = fib(n)
	while True:
		try:
			x = next(g)
			print(x)
		except StopIteration as e:
			print('Generator return value:', e.value)
			break

def recursionFib(n,b1=1,b2=1,c=3):
	if n<3:         
		return 1     
	else:         
		if n==c:             
			return b1+b2         
		else:             
			return recursionFib(n,b1=b2,b2=b1+b2,c=c+1)

def showRecursionFib():
	n = int(input("要查看第几位数？"))
	print(recursionFib(n))
if __name__=='__main__':
	
	# 方法一
	#  showFib()
	
	#  方法二
	showRecursionFib()