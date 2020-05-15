#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/14 18:23 
# @Author : Jovan
# @File : three_sum_closest.py
# @desc :
'''

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''


def threeSumClosest(nums, target):
    nums.sort()
    length = len(nums)
    ans = nums[0] + nums[1] + nums[2]
    for i in range(length):
        start = i + 1
        end = length - 1
        while end > start:
            sum_ = nums[i] + nums[start] + nums[end]
            if abs(target-sum_) < abs(target-ans):
                ans = sum_
            if target < sum_:
                end -= 1
            elif target > sum_:
                start += 1
            else:
                return ans
    return ans





nums = [0,2,1,-3]
target = 1
print(threeSumClosest(nums, target))
