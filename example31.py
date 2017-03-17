#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 031
'''

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

num = 0
inputed = ''
while True:
	num+=1
	if num > 8:
		print('找不到')
		break
	else:
		result= []
		tip = '请输入第'+str(num)+'个单词：'
		s = str(input(tip))
		if s!='':
			s = inputed + s
			for w in week:
				if s!='' and w.startswith(s):
					result.append(w)
			if len(result)==1:
				print(result[0])
				break
			inputed=s	