#!/usr/bin/python3

'''
	example 045
'''

# solution 1

from functools import reduce

print(sum(range(1,101)))

print(reduce(lambda a,b:a+b,range(1,101)))


n = 0

for x in range(101):
	n = x + n
	

print(n)