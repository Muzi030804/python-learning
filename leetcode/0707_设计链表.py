"""
你可以选择使用单链表或者双链表，设计并实现自己的链表。
单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。
实现 MyLinkedList 类：

MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，
那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self,head=None,length = 0):
        self.head = ListNode(head,None)
        self.length = length

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val,None)
        new_head.next = self.head.next
        self.head.next = new_head
        self.length += 1

    def get(self, index: int) -> int:
        curr = self.head.next
        if index < 0 or index >= self.length:
            return -1
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtTail(self, val: int) -> None:
        curr = self.head
        new_tail = ListNode(val, None)
        while curr.next is not None:
            curr = curr.next
        curr.next = new_tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        new_node = ListNode(val,None)
        curr_length = self.length
        if index < 0 or index > self.length:
            return None
        self.length +=1
        while 0 < index <= curr_length:
            curr = curr.next
            index -= 1
        new_node.next = curr.next
        curr.next = new_node
        return None

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        curr_length = self.length
        if 0 <= index < self.length:
            self.length -= 1
        while 0 < index < curr_length:
            curr = curr.next
            index -= 1

        curr.next = curr.next.next
l = MyLinkedList()
l.addAtIndex(0,1)
print(l.length)
l.addAtIndex(1,2)
print(l.length)
l.addAtIndex(2,3)
print(l.length)
# l.addAtTail(4)
# print(l.length)
# l.deleteAtIndex(3)
# print(l.length)
# l.deleteAtIndex(2)
# print(l.length)
# l.deleteAtIndex(3)
# l.addAtIndex(2,3)
# print(l.length)
print("------------")
print(l.get(0))
print(l.get(1))
print(l.get(2))
print(l.get(3))
print(l.get(4))
print(l.get(5))

