#!/usr/bin/python
# -*- coding: UTF-8 -*-*

__author__ = 'yangdd'

'''
 example 004
'''

def day():
 year = int(input("请输入年："))
 month = int(input("请输入月："))
 day = int(input("请输入日："))
 
 days = [31,28,31,30,31,30,31,31,30,31,30,31]
  
 if (year % 400 ==0) or ((year % 4 == 0) and (year % 100 !=0)):
  days[1]=29
 
  the_day= sum(days[:month-1]) 
 
 the_day += day
 
 print('it is the %dth day.' % the_day)
 
 
 
 
if __name__ =='__main__':
   day() 
 
  