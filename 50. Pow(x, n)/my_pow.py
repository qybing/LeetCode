#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/11 18:25 
# @Author : Jovan
# @File : my_pow.py
# @desc :
'''

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
'''


def myPow(x, n):
    return x ** n


print(myPow(2.00000, 10))
