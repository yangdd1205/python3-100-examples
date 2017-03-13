#!/use/bin/python3

__author__ = 'yangdd'

'''
	example 027
'''

def output(str):
	if len(str)>0:
		print(str[-1])
		output(str[0:-1])


string = str(input('请输入一个字符串：'))
output(string)		