#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/25 18:44 
# @Author : Jovan
# @File : merge_two_lists.py
# @desc :
'''
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    c = []
    while l1:
        c.append(l1.val)
        l1 = l1.next
    while l2:
        c.append(l2.val)
        l2 = l2.next
    c.sort()
    ans = ListNode(0)
    re = ans
    for i in c:
        ans.next = ListNode(i)
        ans = ans.next
    return re.next


def mergeTwoLists1(l1: ListNode, l2: ListNode) -> ListNode:
    prehead = ListNode(-1)
    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    prev.next = l1 if l1 is not None else l2
    return prehead.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4

node5.next = node6
node6.next = node7
mergeTwoLists(node1, node5)
