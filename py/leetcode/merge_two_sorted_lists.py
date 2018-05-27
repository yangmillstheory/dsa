# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, p, q):
        '''Merge two sorted linked lists in O(1) space and O(m+n) time.'''
        if not p:
            return q
        if not q:
            return p
        dummy = ListNode(0)
        cur = dummy
        while p or q:
            nxt = None
            if not p:
                nxt, q = q, q.next
            elif not q:
                nxt, p = p, p.next
            elif p.val < q.val:
                nxt, p = p, p.next
            else:
                nxt, q = q, q.next
            cur.next = nxt
            cur = cur.next
        return dummy.next
