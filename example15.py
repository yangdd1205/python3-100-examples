#!/usr/bin/python3

__author__ = 'yangdd'

'''
 example 015
'''

score = int(input('请输入成绩：'))

if score >= 90:
	grade = 'A'
elif score >= 60:
	grade = 'B'
else:
	grade = 'C'
	
print('%d belongs to %s' % (score,grade))	