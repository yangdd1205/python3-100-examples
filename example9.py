#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'


'''
 example 009
'''

import time


d={1:'张三',2:'李四'}

for k,v in d.items():
	print('%s:%s' % (k,v))
	time.sleep(2)


