#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'

'''
 example 005
'''


def num_sort():
  array = []
  
  array.append(int(input("请输入第一个整数：")))
  array.append(int(input("请输入第二个整数：")))
  array.append(int(input("请输入第三个整数：")))
  
  sorted_array = sorted(array)
  
  print(sorted_array)
  
  
  
if __name__=='__main__':
  num_sort()
  
  