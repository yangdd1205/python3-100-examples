#!/usr/bin/python3

__author__ = 'yangdd'


'''
 example 014
'''

import math  
number = int(input("Enter a number: "))  
  
list = []  
  
def getChildren(num):  
    print('*'*30)  
    isZhishu = True  
    i = 2  
    square = int(math.sqrt(num)) + 1  #判断一个数n是否是质数时候，只需要2到n的平方根就行了
    while i <= square:
       	if num % i == 0:  
            list.append(i)  
            isZhishu = False					
            getChildren(num / i)  # 不是质数 继续分解 该数
            i += 1  
            break  
        i += 1  
    if isZhishu:  
        list.append(int(num))  # 是质数 加入list
  
getChildren(number)  
print(list)  