#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/6/1 10:36 
# @Author : Jovan
# @File : kids_with_candies.py
# @desc :
def kidsWithCandies(candies, extraCandies):
    max_number = max(candies)
    return [True if i + extraCandies >= max_number else False for i in candies]


candies = [4, 2, 1, 1, 2]
extraCandies = 1
kidsWithCandies(candies, extraCandies)
