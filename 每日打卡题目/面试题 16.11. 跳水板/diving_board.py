#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/7/8 19:06 
# @Author : Jovan
# @File : diving_board.py
# @desc :
'''
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
返回的长度需要从小到大排列。
示例：
输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：
0 < shorter <= longer
0 <= k <= 100000
'''

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int):
        sum = []
        if k == 0:
            return []
        if shorter == longer:
            return [shorter*k]
        for i in range(k+1):
            sum.append(longer*i+shorter*(k-i))
        return sorted(list(set(sum)))


s = Solution()
shorter = 2
longer = 1118596
k = 979
print(s.divingBoard(shorter, longer, k))