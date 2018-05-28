# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node and node.next:
            if node.next.val == val:
                n = node.next
                while n.val == val:
                    # make sure that consecutive hits are deleted
                    n = n.next
                node.next = n
            node = node.next
        return dummy.next

    # this is someone else's cleaner implementation
    def removeElementsCleaner(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
