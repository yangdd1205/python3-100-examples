#!/use/bin/python3

__author__ = 'yangdd'

'''
	example 024
'''


a = 2
b =1

total = 0.0

for i in range(1,21):
	total += a/b
	a,b=a+b,a
	
print(total)
