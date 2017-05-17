#!/usr/bin/python3

import time

__author__ = "yang.dd"

"""
    example 093
"""

if __name__ == "__main__":
    start = time.clock()
    for i in range(3000):
        print(i)
    end = time.clock()

    print(end-start)