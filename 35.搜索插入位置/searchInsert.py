#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/23 17:32 
# @Author : Jovan
# @File : searchInsert.py
# @desc :
def searchInsert(nums, target):
    nums.append(target)
    nums.sort()
    index = nums.index(target)
    return index


nums = [1, 3, 5, 6]
target = 2
searchInsert(nums, target)
