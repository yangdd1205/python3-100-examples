#!/usr/bin/python3

from tkinter import *

__author__ = "yang.dd"


"""
    example 057
"""

if __name__ == '__main__':
    canvas = Canvas(width=300, height=300, bg='black')
    canvas.pack(expand=YES, fill=BOTH)
    x = 10
    y = 290
    for i in range(10, 300, 10):
        canvas.create_line(x, 10, y, 290, width=1, fill='red')
        x += 10
        y -= 10
    mainloop()