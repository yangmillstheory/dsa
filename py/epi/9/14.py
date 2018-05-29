from collections import deque, namedtuple


ListNode = namedtuple('ListNode', ['data', 'next'])


def _iter_preorder(root):
    stack = deque()
    while root or stack:
        if root:
            if root.right:
                stack.append(root.right)
            yield root
            root = root.left
        else:
            root = stack.pop()


def _iter_leaves_preorder(root):
    for node in _iter_preorder(root):
        if not node.left and not node.right:
            yield node


def list_from_leaves(root):
    # represent a linked list node as a tuple
    head = node = ListNode()
    for leaf in _iter_leaves_preorder(root):
        node.next = ListNode(leaf.data, None)
        node = node.next
    return head.next
