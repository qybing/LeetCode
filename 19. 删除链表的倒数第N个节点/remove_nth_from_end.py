#! python3
# _*_ coding: utf-8 _*_
# @Time : 2020/5/21 18:51 
# @Author : Jovan
# @File : remove_nth_from_end.py
# @desc :
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    node = ListNode(-1)
    node.next = head
    first = second = node
    for i in range(n):
        first = first.next
    b = first
    while first.next:
        first = first.next
        second = second.next
    second.next = second.next.next
    return node.next


def removeNthFromEnd1(head: ListNode, n: int) -> ListNode:
    if not head or n <= 0:
        return head
    # 增加一个特殊节点，方便边界处理
    p = ListNode(-1)
    p.next = head
    a = p
    b = p
    k = 0
    # 第一次遍历，计算链表总长度
    while a.next:
        a = a.next
        k = k + 1
    # 如果链表总长度小于n，那就直接返回
    if k < n:
        return head
    # 计算第二次遍历多少个节点
    num = k - n
    # 第二次遍历，找到要删除节点的前一个节点
    while num > 0:
        b = b.next
        num = num - 1
    # 删除节点，并返回
    b.next = b.next.next
    return p.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
a = removeNthFromEnd1(node1, 2)
print(a)
