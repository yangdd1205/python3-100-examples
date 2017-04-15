#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 061
    enumerate():返回index和value 
"""


def solution1():
    l = [1]
    while True:
        yield l
        l = [1] + [x + l[i + 1] for i, x in enumerate(l) if i < len(l) - 1] + [1]


def solution2():
    l = [1]
    while True:
        yield l
        l.append(0)
        l = [l[i - 1] + l[i] for i in range(len(l))]


if __name__ == "__main__":
    n = 0
    for t in solution1():
        print(t)
        n = n + 1
        if n == 10:
            break
