#!/use/bin/python3

__author__ = 'yangdd'

'''
	example 020
'''


# 每次下落的高度
fall = []
# 每次上升的高度
up=[]

height = 100;

tim = 10
for i in range(1,tim+1):
	fall.append(height)
	height/=2
	up.append(fall[-1]/2)
	


print('它在第%d次落地时，共经过%f米' % (tim,sum(fall)+sum(up[:-1])))
print('第%d次反弹%f米' % (tim,up[-1]))	