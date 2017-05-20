#!/usr/bin/python3

import time

__author__ = "yang.dd"

"""
    example 095
    python3 好像没有 dateutil
"""

if __name__ == "__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
