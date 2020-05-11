#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/11 18:07 
# @Author : Jovan
# @File : remove_element.py
# @desc :
def removeElement(nums, val):
    l = len(nums)
    for i in range(l - 1, -1, -1):
        if val == nums[i]:
            nums.pop(i)
    return len(nums)


def removeElement_1(nums, val):
    while val in nums:
        nums.remove(val)
    print(nums)
    return len(nums)


nums = [2, 2, 3]
val = 2
print(removeElement_1(nums, val))
