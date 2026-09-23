# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def list_to_linked_list(nums):
    dummy = ListNode()
    cur = dummy

    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next
def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result

def func( head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        cur = pre.next
        pre.next = pre.next.next
        cur.next = cur.next.next
        pre.next.next = cur
        pre = pre.next.next
    return dummy.next

head = list_to_linked_list([])

result = func(head)

print(linked_list_to_list(result))