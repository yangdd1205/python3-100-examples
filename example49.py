#!/usr/bin/python3

'''
	example 049
'''


add = lambda x,y:x+y;
hello = lambda who:'hello,'+who
compare =  lambda x, y: x if x < y else y

print(add(1,2))
print(hello('Lee'))
print(compare(1,2))