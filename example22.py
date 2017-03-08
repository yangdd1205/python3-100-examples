#!/usr/bin/python3

__author__ = 'yangdd'

'''
	example 022
'''

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
							