#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/4/21 18:28 
# @Author : Jovan
# @File : b.py
# @desc :
F = 9.81


def bin_search(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


li = [2, 8,2, 9, 3, 5, 50, 69, 21, 32]
# bin_search(li)
heigt = 2
def select_sort(li):
    for i in range(len(li)):
        min_pos = i
        for j in range(i+1, len(li)):
            if li[min_pos] > li[j]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]


select_sort(li)
print(li)
