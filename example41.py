#!/usr/bin/python3

'''
	example 041
'''

class Static():
	staticNum=1
	def add(self):
		self.staticNum+=1
		print(self.staticNum)
		


s = Static()
for i in range(3):
	s.add()