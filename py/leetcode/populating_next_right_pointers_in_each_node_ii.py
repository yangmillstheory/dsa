# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def connect(self, root):
        '''Populate right siblings for a not necessarily perfect
        binary tree in T(n) = O(n) and S(n) = O(1).
        '''
        while root:
            node = root
            while node:
                if node.left and node.right:
                    node.left.next = node.right
                _next = node.next
                # find the next non-leaf
                while _next and _next.left is None and _next.right is None:
                    _next = _next.next
                if _next:
                    use_next = _next.left if _next.left else _next.right
                    if node.right:
                        node.right.next = use_next
                    elif node.left:
                        node.left.next = use_next
                node = _next
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = root.next
