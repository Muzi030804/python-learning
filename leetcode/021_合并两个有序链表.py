#将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
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

def func( list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    cur1 = list1
    cur2 = list2
    while cur1 and cur2:
        if cur1.val <= cur2.val:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
    if cur1 is None:
        cur.next = cur2
    else:
        cur.next = cur1
    return dummy.next


            
            
head1 = list_to_linked_list([1,2])
head2 = list_to_linked_list([1,2])

result = func(head1,head2)

print(linked_list_to_list(result))

