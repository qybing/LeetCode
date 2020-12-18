#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/12/18 15:38 
# @Author : Jovan
# @File : inorderTraversal.py
# @desc :
'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：
输入：root = []
输出：[]
示例 3：
输入：root = [1]
输出：[1]
'''
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
