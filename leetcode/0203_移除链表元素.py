# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
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

def func(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head

    pre = dummy
    cur = dummy.next
    while cur:
        if cur.val == val:
            pre.next = cur.next
            cur = pre.next
        else:
            pre = cur
            cur = cur.next
    return dummy.next
def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result
head = list_to_linked_list([])

result = func(head, 6)

print(linked_list_to_list(result))


