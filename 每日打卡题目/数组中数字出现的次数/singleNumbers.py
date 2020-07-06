#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/28 22:41 
# @Author : Jovan
# @File : singleNumbers.py
# @desc :
# def singleNumbers(nums):
#     result = []
#     if len(nums) <= 2:
#         return nums
#     for i in range(len(nums)):
#         if i == 0:
#             if nums[i] in nums[1:]:
#                 continue
#         else:
#             if nums[i] in nums[0:i] or nums[i] in nums[i+1:]:
#                 continue
#         result.append(nums[i])
#     return result


def singleNumbers(nums):
    dic = {}
    for num in nums:
        if num in dic.keys():
            del dic[num]
        else:
            dic[num] = 1
    return list(dic.keys())

nums = [1,2,10,4,1,4,3,3]
print(singleNumbers(nums))
