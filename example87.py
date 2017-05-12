#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 087
    python是按值传递参数
"""

if __name__ == "__main__":
    class student:
        x = 0
        c = 0


    def f(stu):
        stu.x = 20
        stu.c = 'c'


    a = student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x, a.c)
