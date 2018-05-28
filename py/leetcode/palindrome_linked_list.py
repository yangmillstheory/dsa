# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverse_list(self, head):
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

    def _get_midpoint(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head):
        '''Check if a linked list is a palindrome in O(n)
        time and O(1) space.
        '''
        mid = self._get_midpoint(head)
        rev = self.reverse_list(mid)
        is_palindrome = True
        p, q = head, rev
        while p and q and p != q:
            if p.val != q.val:
                is_palindrome = False
                break
            else:
                p = p.next
                q = q.next
        self.reverse_list(mid)
        return is_palindrome
