#!/usr/bin/python3


__author__ = "yang.dd"

"""
    example 100
"""

if __name__ == "__main__":
    print("*****两个List转Dict****")
    keys = ['key1', 'key2', 'key3']
    print("第一个List: ", keys)
    values = ['value1', 'value2', 'value3']
    print("第二个List: ", values)
    result = dict(zip(keys, values))
    print("Dict: ", result)
