#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/19 9:58 
# @Author : Jovan
# @File : four_sum.py
# @desc :
def fourSum(nums, target):
    nums.sort()
    length = len(nums)
    result = []
    for i in range(length):
        if i >= 1 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, length):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            start = j + 1
            end = length - 1
            while start < end:
                sum_ = nums[i] + nums[j] + nums[start] + nums[end]
                if sum_ < target:
                    start += 1

                elif sum_ > target:
                    end -= 1
                else:
                    result.append([nums[i], nums[j], nums[start], nums[end]])
                    while start < end and nums[start+1] == nums[start]:
                        start += 1
                    while start < end and nums[end-1] == nums[end]:
                        end -= 1
                    end -= 1
                    start += 1
    return result


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
