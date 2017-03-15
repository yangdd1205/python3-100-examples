#!/use/bin/python3

__author__ = 'yangdd'

'''
	example 029
'''

x = int(input('请输入一个数：'))

#a = int(num / 10000)
#b = int(num / 1000 % 10)
#c = int(num / 100 % 10)
#d = int(num / 10 % 10)
#e = int(num % 10)

a = int(x / 10000)
b = int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e = int(x % 10)

if a!=0:
	print('5 位数：',a,b,c,d,e)