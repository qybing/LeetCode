#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/23 17:39 
# @Author : Jovan
# @File : searchInsert-1.py
# @desc :
def searchInsert(nums, target):
    index = 0
    length = len(nums)
    for i in range(length):
        if nums[i] >= target:
            if i == 0:
                index = 0
            else:
                index = i
            nums.insert(index, target)
            break
    if length == len(nums):
        nums.append(target)
        index = length
    return index


nums = [1, 3, 5, 6]
target = 7
a = searchInsert(nums, target)
print(a)
