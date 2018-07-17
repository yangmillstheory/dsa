# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        # T(n) = O(n)
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy.next
        while p and q:
            while q.next and q.next.val == q.val:
                p.next = q.next
                q = q.next
            p, q = p.next, q.next
        return dummy.next

    def deleteDuplicatesSlower(self, head):
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
