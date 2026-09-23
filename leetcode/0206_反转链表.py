# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

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
    if head is None:
        return None
    dummy = ListNode()
    cur = head

    while cur:
        last = cur.next
        cur.next = dummy.next
        dummy.next = cur
        cur = last

    return dummy.next


head = list_to_linked_list([1,2,3,4,5])

result = func(head)

print(linked_list_to_list(result))


