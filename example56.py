#!/usr/bin/python3

from tkinter import *

__author__ = "yang.dd"


"""
    example 056
"""

if __name__ == '__main__':
    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3
    mainloop()