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


def swapPairs(head: ListNode) -> ListNode:
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # If the list has no node or has only one node left.
    if not head or not head.next:
        return head

    # Nodes to be swapped
    first_node = head
    second_node = head.next

    # Swapping
    first_node.next = swapPairs(second_node.next)
    second_node.next = first_node
    return second_node


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
swapPairs(node1)
