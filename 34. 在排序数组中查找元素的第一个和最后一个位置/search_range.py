#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/6/11 9:42 
# @Author : Jovan
# @File : search_range.py
# @desc :
def searchRange(nums, target):
    res = []
    for index, num in enumerate(nums):
        if num == target:
            if len(res) >= 2:
                res.pop()
            res.append(index)
    if len(res) == 0:
        return [-1, -1]
    if len(res) == 1:
        res.append(res[0])
        return res
    return res


nums = [1]
target = 1
print(searchRange(nums, target))
