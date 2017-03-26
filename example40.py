#!/usr/bin/python3

'''
	example 040
'''
a = [9,6,5,4,1]

def solution1():
	print(a)
	N = len(a)
	for i in range(N >> 1):
		a[i],a[N-1-i]=a[N-1-i],a[i]
	
	print(a)
	
def solution2():
	print(a[::-1])
	
	
if __name__ == '__main__':
	solution2()