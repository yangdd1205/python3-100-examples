#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 054
    
"""

if __name__ == '__main__':
    a = int(input('input a number:\n'))
    print('%d binary is  %s' % (a, bin(a)))
    b = a >> 3
    c = b & 0xF
    print("result ", bin(c))
