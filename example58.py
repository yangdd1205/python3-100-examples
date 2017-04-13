#!/usr/bin/python3

from tkinter import *

__author__ = "yang.dd"


"""
    example 058
"""

if __name__ == '__main__':
    canvas = Canvas(width=300, height=300, bg='purple')
    canvas.pack(expand=YES, fill=BOTH)
    x = 145
    y = 155
    for i in range(1, 20):
        canvas.create_rectangle(x, x, y, y, width=2, outline='yellow')
        x -= 5
        y += 5

    mainloop()