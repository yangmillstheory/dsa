def length(x):
    n = 0
    while x:
        n += 1
        x = x.next
    return n


def _overlapping_equal_length_lists(p, q):
    while p or q:
        if p is q:
            return p
        p = p and p.next
        q = q and q.next


def overlapping_no_cycle_lists(p, q):
    m, n = length(p), length(q)
    if m <= n:
        p, q, m, n = q, p, n, m
    for _ in range(m-n):
        p = p.next
    return _overlapping_equal_length_lists(p, q)


class Solution(object):
    def getIntersectionNode(self, p, q):
        # T(n) = O(max(m, n))
        # S(n) = O(1)
        return overlapping_no_cycle_lists(p, q)
