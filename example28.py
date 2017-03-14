#!/use/bin/python3

__author__ = 'yangdd'

'''
	example 028
'''

def age(age):
	return age_inter(age,5);

def age_inter(age,num):
	if num ==1:
		return age	
	return age_inter(age+2,num-1)
	

	
	
print(age(10))	