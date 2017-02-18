#!/usr/bin/python
# -*- coding: UTF-8 -*-*

__author__ = 'yangdd'

'''
 example 002
'''

def bonus():
 profites = int(input('请输入利润（元 ）：'))
 arr = [100*10000,60*10000,40*10000,20*10000,10*10000,0]
 rat = [0.01,0.015,0.03,0.05,0.075,0.1]
 bonus = 0
 for i in range(0,6):
     if profites>arr[i]:
        bonus += (profites-arr[i])*rat[i]
        profites = arr[i]		
 print('奖金是：%s' % (format(bonus,'.2f')))


if __name__ == '__main__':
  bonus()
	