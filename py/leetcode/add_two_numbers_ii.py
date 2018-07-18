def length(x):
    n = 0
    while x:
        n += 1
        x = x.next
    return n


class Solution(object):
    def addTwoNumbers(self, x, y):
        # T(n) = S(n) = O(max(m, n))
        m, n = length(x), length(y)
        if m <= n:
            # WLOG x is the longer list
            x, y, m, n = y, x, n, m
        stack = []
        dummy = node = ListNode(0)
        for _ in range(m-n):
            node.next = ListNode(x.val)
            node, x = node.next, x.next
            stack.append(node)
        for _ in range(n):
            s = x.val + y.val
            if s >= 10:
                last_j = float('inf')
                for j in range(len(stack)-1, -1, -1):
                    _node = stack[j]
                    _node.val += 1
                    if _node.val < 10:
                        break
                    else:
                        _node.val -= 10
                        last_j = j
                if last_j == 0 or not stack:
                    prev = dummy.next
                    dummy.next = ListNode(1)
                    dummy.next.next = prev
                    if node is dummy:
                        node = node.next
                s -= 10
            node.next = ListNode(s)
            node, x, y = node.next, x.next, y.next
            stack.append(node)
        return dummy.next
