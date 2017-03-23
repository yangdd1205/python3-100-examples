#!/usr/bin/python3

'''
	example 037
	选择排序
'''

l = [5,3,23,67,2,56,45,89,239,9]

for i in range(10-1):
	min = i
	for j in range(i+1,10):
		if l[min]>l[j]:
			min = j
	print(i,min)
	l[i],l[min]=l[min],l[i]
	

for i in range(10):
	print(l[i])