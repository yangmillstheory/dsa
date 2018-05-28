# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        '''Reverse a linked list in-place in O(n) time.'''
        if not head:
            return
        new_head = head
        tail = head
        node = head.next
        while node:
            temp = node.next
            node.next = new_head
            tail.next = temp
            new_head = node
            node = temp
        return new_head
