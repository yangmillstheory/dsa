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


def reverse_sublist(head, s, f):
    '''Reverse a sublist of a singly-linked list in O(f) time.'''
    dummy = ListNode(0)
    dummy.next = head
    prev_s = walk(dummy, s-1)
    s_node = prev_s.next
    f_node = walk(s_node, f-s)
    while s_node != f_node:
        next_s_node, s_node.next = s_node.next, f_node.next
        f_node.next = s_node
        s_node = s_node.next
        s_node = next_s_node
    prev_s.next = f_node
    return dummy.next


def get_length(head):
    n = 0
    while head:
        head, n = head.next, n+1
    return n


def walk(head, n_steps):
    for _ in range(n_steps):
        head = head.next
    return head


def is_linked_list_a_palindrome(head):
    # T(n) = O(n)
    # S(n) = O(1)
    n = get_length(head)
    if n <= 1:
        return True
    s, n_steps = n//2 + 1, n//2
    if n % 2 != 0:
        s += 1
        n_steps += 1
    reverse_sublist(head, s, n)
    tail = walk(head, n_steps)
    is_pali = True
    node = head
    while node and tail:
        if node.val != tail.val:
            is_pali = False
            break
        node, tail = node.next, tail.next
    reverse_sublist(head, s, n)
    return is_pali

class SolutionBetter(object):
    def isPalindrome(self, head):
        return is_linked_list_a_palindrome(head)
