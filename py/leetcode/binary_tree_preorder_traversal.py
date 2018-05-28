from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def _pre_order_iter(self, root):
        stack = deque()
        while stack or root:
            if root:
                yield root.val
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()

    def preorderTraversal(self, root):
        return list(self._pre_order_iter(root))
