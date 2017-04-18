#!/usr/bin/python3

from tkinter import *

__author__ = "yang.dd"

"""
    example 063
"""

if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width="600", height="800", bg="white")
    canvas.pack()
    x = 100
    y = 200
    width = 500
    height = 600
    for i in range(40):
        u = 5 * i
        canvas.create_oval(x + u, y - u, width - u, height + u)
    mainloop()
