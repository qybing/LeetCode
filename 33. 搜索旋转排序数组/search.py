#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/6/12 19:37 
# @Author : Jovan
# @File : search.py
# @desc :
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''


def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1


def search2(nums, target):
    right = len(nums) - 1
    left = 0
    while right >= left:
        mid = (right + left) / 2
        if nums[mid] == target:
            return mid
        elif nums[left] < nums[mid]:
            pass


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
search(nums, target)
