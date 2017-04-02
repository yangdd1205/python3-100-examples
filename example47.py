#!/usr/bin/python3

'''
	example 047
'''

def change(a,b):
	a,b=b,a
	return (a,b)
	
	
if __name__ == '__main__':
	
	a = 10
	b = 20
	print('a = %d, b = %d' % (a,b))
	a,b = change(a,b)
	print('a = %d, b = %d'  % (a,b))