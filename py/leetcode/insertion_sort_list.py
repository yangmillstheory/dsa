from io import StringIO


def insertion_sort(xs):
    '''Insertion sort for arrays.'''
    j = 0
    while j < len(xs):
        i = j
        while i >= 1 and xs[i] < xs[i-1]:
            xs[i], xs[i-1] = xs[i-1], xs[i]
            i -= 1
        j += 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __repr__(self):
        s = ''
        cur = self
        first = True
        while cur:
            if not first:
                s += '->'
            first = False
            s += str(cur.val)
            cur = cur.next
        return s


class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                targ = head.next
                prev = dummy
                while prev.next.val < targ.val:
                    prev = prev.next
                temp = prev.next
                prev.next = targ
                head.next = targ.next
                targ.next = temp
        return dummy.next


if __name__ == '__main__':
    xs = [4, 1, 3, 2]
    insertion_sort(xs)
    assert xs == [1, 2, 3, 4]

    h = ListNode(4, ListNode(1, ListNode(3, ListNode(2))))
    print(Solution().insertionSortList(h))
