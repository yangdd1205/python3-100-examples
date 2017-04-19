#!/usr/bin/python3

from tkinter import *

__author__ = "yang.dd"

"""
    example 059
"""

if __name__ == '__main__':
    width = 600
    height = 400
    root = Tk()
    root.title('红旗')
    root.resizable(False, False);
    root['width'] = width
    root['height'] = height
    canvas = Canvas(width=width, height=height, bg='#F40002 ')  # china red = F40002 , star yellow =  FAF408
    canvas.pack(expand=NO, fill=BOTH)
    width_half = width / 2
    height_half = height / 2
    canvas.create_line(width_half, 0, width_half, height_half)
    canvas.create_line(0, height_half, width_half, height_half)
    x = y = 0
    for i in range(0, 15):
        canvas.create_line(x, 0, x, height_half)
        x += width_half / 15
    for i in range(0, 10):
        canvas.create_line(0, y, width_half, y)
        y += height_half / 10

    a = width_half / 15
    # 在从原点开始长为8a，宽为8a的矩形中，画椭圆 2a,2a 分别为椭圆左上角x,y的坐标
    canvas.create_oval(2 * a, 2 * a, 8 * a, 8 * a, width=1)

    mainloop()
