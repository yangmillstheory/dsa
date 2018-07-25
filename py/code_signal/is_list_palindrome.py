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
        if node.value != tail.value:
            is_pali = False
            break
        node, tail = node.next, tail.next
    reverse_sublist(head, s, n)
    return is_pali


def get_kth(head, k):
    '''Returns the kth node from head (inclusive), 1-indexed.'''
    for _ in range(k-1):
        head = head.next
    return head


def reverse_sublist(head, s, f):
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


def isListPalindrome(head):
    return is_linked_list_a_palindrome(head)
