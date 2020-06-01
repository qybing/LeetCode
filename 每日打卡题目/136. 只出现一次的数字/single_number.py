#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/14 14:14 
# @Author : Jovan
# @File : single_number.py
# @desc :
'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
'''
def singleNumber(nums):
    length = len(nums)
    for i in range(length):
        if nums.count(nums[i]) == 1:
            return nums[i]


def singleNumber_1(nums):
    ret = 0
    for num in nums:
        ret = ret ^ num
    return ret

nums = [4,1,2,1,2]
print(singleNumber(nums))
