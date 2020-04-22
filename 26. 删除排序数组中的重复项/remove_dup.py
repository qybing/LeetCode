#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/22 19:40 
# @Author : Jovan
# @File : remove_dup.py
# @desc :
#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/21 17:12
# @Author : Jovan
# @File : a.py
# @desc :
def removeDuplicates(nums):
    nums = [1, 1, 2]
    x = 0
    y = 1
    if len(nums) == 1 or len(nums) == 0:
        return nums
    for j in range(len(nums) - 1):
        if nums[x] == nums[y]:
            nums.pop(y)
        else:
            x += 1
            y += 1
    return nums


nums = [1, 1, 2]
a = removeDuplicates(nums)
print(a)
