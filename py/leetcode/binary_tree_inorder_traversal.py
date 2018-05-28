from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _in_order_iter(self, root):
        stack = deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                yield root.val
                root = root.right

    def inorderTraversal(self, root):
        '''Iterative in-order traversal of a binary tree in O(n) time and O(h) space.'''
        return list(self._in_order_iter(root))
