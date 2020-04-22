#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/22 19:40 
# @Author : Jovan
# @File : strStr.py
# @desc :
def strStr(haystack, needle):
    exist = -1
    if needle in haystack:
        exist = haystack.find(needle)
    return exist
