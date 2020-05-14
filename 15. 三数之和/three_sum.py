#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/13 18:53 
# @Author : Jovan
# @File : three_sum.py
# @desc :
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


def threeSum(nums):
    length = len(nums)
    nums.sort()
    b = set()
    for i in range(length):
        l = i + 1
        r = length - 1
        while r > l:
            sum_ = nums[i] + nums[l] + nums[r]
            if sum_ == 0:
                b.add((nums[i], nums[l], nums[r], ))
                l += 1
                r -= 1
            elif sum_ < 0:
                l += 1
            else:
                r -= 1
    c = []
    for j in b:
        c.append(list(j))
    return c

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
