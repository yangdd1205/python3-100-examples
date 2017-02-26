#!/usr/bin/python3


__author__ = 'yangdd'

'''
 example 012
	
  这里我们用filter求质数（素数）
	
  假如求 101 到200之间的素数 可以 用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
	
 '''

# 先构造一个从3开始的奇数序列

def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n

		
# 定义一个筛选函数
def _not_divisible(n):
	return lambda x : x % n >0
'''
  Python的filter要求接受一个参数，但事实上我们筛选过程中有两个参数：待筛的元素和当前筛选所用因数。
  由于每轮筛选时因数是一定的，所以我们可以通过每轮生成一个携带因数的闭包来变两个参数为一个参数
  
  等同于下面的代码
  def _not_divisible(n):
	def anonymous(x):
		return x % n >0
  return anonymous
  
  
  
'''	

#  定义一个生成器，不断返回素数
def primes():
	yield 2
	it = _odd_iter() # 初始化序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
		
		
# 打印1000以内的素数
for n in primes():
	if n <1000:
		print(n)
	else:
		break
	
		
		


