#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 034
'''

def hello_world():
	print('Hello World')
	
	
def three_hello():
	for i in range(3):
		hello_world()
		

if __name__ == '__main__':
	three_hello()