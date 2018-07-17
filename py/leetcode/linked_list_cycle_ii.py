def walk(head, n_steps):
    for _ in range(n_steps):
        head = head.next
    return head


def get_cycle_length(head):
    node, n = head, 0
    while node:
        n += 1
        node = node.next
        if id(node) == id(head):
            break
    return n


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if id(slow) == id(fast):
            break
    if not fast or not fast.next:
        return None
    fast = walk(head, get_cycle_length(slow))
    slow = head
    while id(fast) != id(slow):
        slow, fast = slow.next, fast.next
    return slow


class Solution(object):
    def detectCycle(self, head):
        return has_cycle(head)
