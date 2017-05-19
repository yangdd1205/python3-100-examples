#!/usr/bin/python3

import time
import random

__author__ = "yang.dd"

"""
    example 094
"""

if __name__ == "__main__":
    print("*" * 5 + "猜数字游戏" + "*" * 5)
    play = input("你准备好了么？（Y OR N）")
    while play in ("Y", "y"):
        c = input("请输入任意字符开始")
        i = random.randint(0, 2 ** 32) % 100
        start = time.clock()
        a = time.time()
        guess = int(input("请输入你的答案："))
        while guess != i:
            if guess > i:
                print("请输入一个小一点的数。")
                guess = int(input("请输入你的答案："))
            else:
                print("请输入一个大一点的数。")
                guess = int(input("请输入你的答案："))
        end = time.clock()
        b = time.time()

        var = (end - start) / 18.2
        if var < 15:
            print('you are very clever!')
        elif var < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
        play = play = input("你准备好了么？（Y OR N）")
