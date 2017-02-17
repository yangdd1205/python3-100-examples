#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'yangdd'

'''
 example 001
'''

def show():
 for i in range(1,5):
  for j in range(1,5):
   for k in range(1,5):
    if(i!=j) and (i!=k) and (j!=k):
     print(i,j,k)
	 
	 
if __name__ == '__main__':
   show()
