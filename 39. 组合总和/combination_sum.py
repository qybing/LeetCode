#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/7/8 19:28 
# @Author : Jovan
# @File : combination_sum.py
# @desc :
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        length = len(candidates)
        res = []
        for i in range(length):
            if candidates[i] > target:
                break
            if candidates[i] == target:
                res.extend([candidates[i]])
            if candidates[i] < target:
                if target % candidates[i] == 0:
                    res.extend([candidates[i] * (target / candidates[i])])


s = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(s.combinationSum(candidates, target))
