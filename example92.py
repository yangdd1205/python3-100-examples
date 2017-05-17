#!/usr/bin/python3

import time

__author__ = "yang.dd"

"""
    example 092
"""

if __name__ == "__main__":
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()

    print(end-start)