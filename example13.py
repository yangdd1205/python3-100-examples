#!/usr/bin/python3

__author__ = 'yangdd'


'''
 example 013
'''

for i in range(100,1000):
	x = int(i / 100) 
	y = int(i / 10 % 10)
	z = int(i % 10)
	if i == ((x ** 3) + (y ** 3) + (z ** 3)):
		print(i)


