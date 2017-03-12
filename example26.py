#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 026
'''



def fact(num):
	return fact_inter(num,1);

def fact_inter(num,product):
	if num ==1:
		return product	
	return fact_inter(num-1,num*product)
	

	
	
print("5!=",fact(5))	