#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/26 18:58 
# @Author : Jovan
# @File : find_duplicate.py
# @desc :
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
示例 1:
输入: [1,3,4,2,2]
输出: 2
示例 2:
输入: [3,1,3,4,2]
输出: 3
'''
def findDuplicate(nums):
    hash_map = {}
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] = hash_map[i] + 1
    for i in nums:
        if hash_map[nums[i]] >= 2:
            return nums[i]

nums = [1,3,4,2,2]
print(findDuplicate(nums))