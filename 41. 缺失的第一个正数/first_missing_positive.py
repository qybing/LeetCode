#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/7/16 19:32 
# @Author : Jovan
# @File : first_missing_positive.py
# @desc :
'''
41. 缺失的第一个正数
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]

输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1
'''
from typing import List


class Solution(object):
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        new_num = [i for i in nums if i > 0]
        if len(new_num) == 0 or new_num[0] > 1:
            return 1
        else:
            for i in range(len(new_num)-1):
                if new_num[i+1] - new_num[i] >= 2:
                    return new_num[i]+1
            else:
                return new_num[-1]+1


nums = [0]
s = Solution()
r = s.firstMissingPositive(nums)
print(r)
