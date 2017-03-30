#!/usr/bin/python3

'''
 example 044
'''

X = [[12,7,3],[4,5,6],[7,8,9]]

Y = [[5,8,1],[6,7,3],[4,5,9]]

#result=[[],[],[]]

result = [([0] * 3) for i in range(3)]



for i in range(0,len(X)):
	temp = X[i]
	for j in range(0,len(temp)):
		result[i][j]=X[i][j]+Y[i][j]



for r in result:
   print(r)