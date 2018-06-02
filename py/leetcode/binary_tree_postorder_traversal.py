import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def _post_order_iter(root):
    stack, last = collections.deque(), None
    while stack or root:
        if root:
            stack.append(root)
            if root.right:
                stack.append(root.right)
            root = root.left
        else:
            root = stack.pop()
            if not root.left and not root.right:
                yield root.val
                last, root = root, None
            elif last and (last == root.right or last == root.left):
                # coming up from left or right child
                yield root.val
                last, root = root, None


class Solution(object):
    def postorderTraversal(self, root):
        '''O(n) time and O(h) space non-recursive post-order traversal.'''
        return list(_post_order_iter(root))
