def get_kth(head, k):
    '''Returns the kth node from head (inclusive), 1-indexed.'''
    for _ in range(k-1):
        head = head.next
    return head


class Solution(object):
    def reverseBetween(self, head, s, f):
        '''Reverse a sublist of a singly-linked list in O(f) time.'''
        dummy = ListNode(0)
        dummy.next = head
        prev_s = get_kth(dummy, s)
        s_node = prev_s.next
        f_node = get_kth(s_node, f-s+1)
        while s_node != f_node:
            next_s_node, s_node.next = s_node.next, f_node.next
            f_node.next = s_node
            s_node = s_node.next
            s_node = next_s_node
        prev_s.next = f_node
        return dummy.next
