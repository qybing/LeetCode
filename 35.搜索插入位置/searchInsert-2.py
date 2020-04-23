#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/23 17:39 
# @Author : Jovan
# @File : searchInsert-1.py
# @desc :
def searchInsert(nums, target):
    length = len(nums)
    for i in range(length):
        if nums[i] >= target:
            return i
    return length


nums = [1, 3, 5, 6]
target = 0
a = searchInsert(nums, target)
print(a)
