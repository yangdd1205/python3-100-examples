#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'yangdd'

'''
 example 007
 
 切片：
 list[start:stop:step]
 start:从哪开始 （不包含）
 stop:在哪结束（包含）
 step:步长 step>0 从左到右 step<0从右到左
 
 -1:代指最后一个元素
 -2:代指倒数第二个元素
 
'''


a=[1,2,3,4,5]
print(a)
#复制a
print('复制a')
print(a[:])

# 截取(1,3]
print('截取从1到3')
print(a[1:3])

# 从头到尾 间隔1位取
print('从头到尾 间隔1位取')
print(a[::2])

#倒叙
print('倒叙')
print(a[::-1])

