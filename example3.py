#!/use/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'

'''
 example 003
'''

import math

def show():
 for i in range(10000):
  x = int(math.sqrt(i+100))
  y = int(math.sqrt(i+268))
  if (x*x == i+100) and (y*y==i+268):
   print(i)


if __name__ == '__main__':
  show()   