#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/20 14:03 
# @Author : Jovan
# @File : effective_brackets.py
# @desc : 括号的有效性,采用栈的方式
class Solution:
    def isVaild(self, s: str) -> bool:
        d = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for i in s:
            if i in d:
                stack.append(i)
            elif d[stack.pop()] != i:
                return False
        return len(stack) == 1
