#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/19 9:01 
# @Author : Jovan
# @File : letterc_ombinations.py
# @desc :
def letterCombinations(digits):
    number_dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    if digits == '':
        return []
    ans = ['']
    for num in digits:
        # for suf in number_dic[num]:
        #     for pre in ans:
        #         ans.append(pre + suf)
        ans = [pre + suf for pre in ans for suf in number_dic[num]]
    return ans


print(letterCombinations("234"))
