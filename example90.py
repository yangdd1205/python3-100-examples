#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 090
"""
# list
# 新建list
testList = [10086, "中国移动", [1, 2, 3, 4]]

# 访问列表长度
print("list len: ", len(testList))

# 切片
print("切片（slice）:", testList[1:])

# 追加

print("追加一个元素")
testList.append("i'm new here!");

print("list len: ", len(testList))
print("last item :", testList[-1])

print("pop: ", testList.pop())
print("list len: ", len(testList))
print(testList)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

print(matrix[1])

col2 = [x[1] for x in matrix]
print(col2)

col2even = [x[1] for x in matrix if x[1] % 2 == 0]
print(col2even)