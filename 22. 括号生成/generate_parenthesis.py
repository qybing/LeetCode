#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/29 16:51 
# @Author : Jovan
# @File : generate_parenthesis.py
# @desc :
def parenthess(sublist, reslut, leftnum, rightnum):
    if leftnum == 0 and rightnum == 0:
        reslut.append(sublist)
    if rightnum > leftnum:
        parenthess(sublist + ')', reslut, leftnum, rightnum - 1)
    if leftnum > 0:
        parenthess(sublist + '(', reslut, leftnum - 1, rightnum)


def generateParenthesis_1(n):
    leftnum = rightnum = n
    reslut = []
    parenthess('', reslut, leftnum, rightnum)
    for i in reslut:
        print(i)


def generateParenthesis(n):
    lists = []

    def helper(tmp='', open=0, close=0):
        if open == n and close == n:
            lists.append(tmp)
            return
        if open < n:
            helper(tmp + '(', open + 1, close)
        if close < open:
            helper(tmp + ')', open, close + 1)

    helper()
    return lists


generateParenthesis(n=3)
