#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 078
"""

if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    values = sorted(person.values(),reverse=True)
    for key in person.keys():
        if person[key] == values[0]:
            print('%s,%d' % (key,person[key]))
