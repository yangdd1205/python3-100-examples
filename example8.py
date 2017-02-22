#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'

'''
 example 008
 
 如何让print不换行
 print('',end='')
'''

for i in range(1,10):
	print()
	for j in range(1,i+1):
		print('%d*%d=%d' % (j,i,i*j),end='\t')