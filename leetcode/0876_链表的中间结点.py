# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
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
    if head == None:
        return None
    dummy = ListNode()
    dummy.next = head
    cur = dummy
    fast = dummy
    while fast.next:

        if fast.next.next:
            fast = fast.next.next
            cur = cur.next
        else:
            fast = fast.next
    return cur.next

head = list_to_linked_list([1,2,3,4,5])

result = func(head)

print(linked_list_to_list(result))
