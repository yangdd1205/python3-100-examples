#!/usr/bin/python3
# -*- coding: UTF-8 -*-


__author__ = 'yangdd'

'''
 example 011
'''

month = int(input('第几个月的兔子总数：'))
a,b=0,1
for i in range(1,month):
    a,b=b,a+b

	
print('第%d个月，兔子总数是：%d' %(month,b*2))
	
	