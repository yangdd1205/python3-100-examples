#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 062
"""

if __name__ == "__main__":
    string = "abcdef"
    s = "bc"
    print("method: count(), result: ", string.count(s))  # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    print("method: find(), result: ",
          string.find(s))  # 检测 str 是否包含在字符串中 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
    print("method: index(), result: ", string.index(s))  # 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
    print("method: rfind(), result: ", string.rfind(s))  # 类似于 find()函数，不过是从右边开始查找.
    print("method: rindex(), result: ", string.rindex(s))  # 类似于 index()，不过是从右边开始.
    print("method: in, result: ", s in string)
