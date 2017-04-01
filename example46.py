#!/usr/bin/python3

'''
	example 046
	
	** 幂运算
	pow(a,b) a的b次方
	
'''

flag = True

while flag:
	
	num = int(input('Please input number:'))
	
	result = num ** 2
	print('结果：',result)
	if result < 50:
		flag = False
		print('结果小于50，则程序退出。')