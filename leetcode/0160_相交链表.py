# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null
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

def func( headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curA = headA
    curB = headB
    lengthA = 0
    lengthB = 0
    while curA:
        lengthA += 1
        curA = curA.next
    while curB:
        lengthB +=1
        curB = curB.next
    curA = headA
    curB = headB
    if lengthA > lengthB:
        for i in range(lengthA - lengthB):
            curA = curA.next
    else:
        for i in range(lengthB - lengthA):
            curB = curB.next
    while curA and curB:
        if curA == curB:
            return curA
        else:
            curA = curA.next
            curB = curB.next
    return None




    return None

headA = list_to_linked_list([4,1,8,4,5])
headB = list_to_linked_list([5,6,1])

result = func(headA, headB)

print(linked_list_to_list(result))