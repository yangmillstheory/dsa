def length(x):
    n = 0
    while x:
        n += 1
        x = x.next
    return n


def walk(head, n_steps):
    for _ in range(n_steps):
        head = head.next
    return head


def cyclically_right_shift_list(head, k):
    # T(n) = O(n)
    # S(n) = O(1)
    n = length(head)
    if not n:
        return head
    k = k % n
    if not k:
        return head
    dummy = tail = ListNode(0)
    dummy.next = head
    fast = walk(tail, k)
    while fast and fast.next:
        fast, tail = fast.next, tail.next
    fast.next, dummy.next, tail.next = dummy.next, tail.next, None
    return dummy.next


class Solution(object):
    def rotateRight(self, head, k):
        return cyclically_right_shift_list(head, k)
