#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 067
"""

if __name__ == '__main__':
    nums = []
    for i in range(6):
        nums.append(int(input("请输入数字：")))

    for i in range(len(nums)):
        if nums[i] == max(nums):
            nums[0], nums[i] = nums[i], nums[0]
            break
    for i in range(len(nums)):
        if nums[i] == min(nums):
            nums[i], nums[len(nums)-1] = nums[len(nums)-1], nums[i]
            break
    print(nums)
