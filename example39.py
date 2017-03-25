#!/usr/bin/python3

'''
	example 038
'''

if __name__ == '__main__':
	a = [1,4,6,9,13,16,19,28,40,100] # 顺序
	#a = a[::-1] # 倒叙
	print('original list is：')
	for i in range(len(a)):
		print(a[i])
		
	number = int(input('insert a new number:'))
	
	if a[0]<a[1]:
		if number < a[0]:
			a.insert(0,number)
		elif number > a[-1]:
			a.insert(len(a),number)
		else:
			for i in range(len(a)-1):
				if a[i]< number and a[i+1]> number:
					a.insert(i+1,number)
					break
	else:
		if number > a[0]:
			a.insert(0,number)
		elif number<a[-1]:
			a.insert(len(a),number)
		else:
			for i in range(len(a)-1):
				if a[i]>number and number>a[i+1]:
					a.insert(i+1,number)
					break
					
	print('new list is：')
	for i in range(len(a)):
		print(a[i])				