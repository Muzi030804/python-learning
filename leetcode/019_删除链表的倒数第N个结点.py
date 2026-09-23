# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

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

def func( head: Optional[ListNode],n :int) -> Optional[ListNode]:
    if head is None:
        return None
    dummy = ListNode()
    dummy.next = head
    fast = dummy
    slow = dummy
    for i in range (n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
head = list_to_linked_list([1,2])

result = func(head,1)

print(linked_list_to_list(result))



