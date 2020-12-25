#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/26 18:33 
# @Author : Jovan
# @File : permute.py
# @desc :
'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))
if __name__ == '__main__':
    a = Solution()
    a.permute([1,2,3])