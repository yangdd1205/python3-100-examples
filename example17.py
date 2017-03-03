#!/usr/bin/python3

__author__ = 'yangdd' 


'''
	example 017
'''

str = input('input a String:')

letters=0
space =0
digit=0
others=0

for s in str:
	if s.isalpha():
		letters+=1
	elif s.isspace():
		space+=1
	elif s.isdigit():
		digit+=1
	else:
		others+=1
		
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))		