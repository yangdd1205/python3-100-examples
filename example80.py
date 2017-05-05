#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 080
"""

if __name__ == '__main__':
    '''
        从第五只猴子拿1个的桃子开始算
        如果有一只不满足条件，则从头开始计算，直到满足
    '''
    monkey = 5
    peach5th = 1
    peach = 1

    while monkey > 1:
        total = peach * 5 + 1
        if total % 4 == 0:
            monkey -= 1
            peach = total / 4
        else:
            # 从第5只猴开始算
            peach5th += 1
            peach = peach5th
            monkey = 5

    print("沙滩上最少有：%d个桃子。" % (int(peach * 5 + 1)))
