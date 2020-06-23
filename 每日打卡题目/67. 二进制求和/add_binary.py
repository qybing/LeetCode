#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/6/23 18:48 
# @Author : Jovan
# @File : add_binary.py
# @desc :
'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"

'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

s = Solution()
a = "1010"
b = "1011"
print(s.addBinary(a, b))
