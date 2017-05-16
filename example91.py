#!/usr/bin/python3

import time
import calendar

__author__ = "yang.dd"

"""
    example 091
"""

if __name__ == "__main__":
    ticks = time.time();
    print("当前时间戳：", ticks)
    localtime = time.localtime(time.time())
    print("本地时间为：", localtime)
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为：", localtime)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
    cal = calendar.month(2017,5)
    print("以下是2017年5月的日历")
    print(cal)
