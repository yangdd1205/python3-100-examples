#!/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'

'''
  example 010
'''

import time


print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 这个参数在表示当前时间的时候可以省略 time.localtime()