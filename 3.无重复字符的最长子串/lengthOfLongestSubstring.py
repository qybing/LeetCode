#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/6 17:57 
# @Author : Jovan
# @File : lengthOfLongestSubstring、.py
# @desc :
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        temp = ""
        for ch in s:
            if ch in temp:
                count = max(count, len(temp))
                temp = temp[temp.find(ch) + 1:]
            temp += ch
        return max(count, len(temp))


def lengthOfLongestSubstring(s):
    length = r = l = 0
    while r < len(s):
        if s[r] not in s[l:r]:
            r += 1
            length = max(length, r - l)
        else:
            l += 1
    return length


s = 'pwwkew'
print(lengthOfLongestSubstring(s))
