# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _is_balanced(self, root):
        if not root:
            return True, 0
        is_bal_l, height_l = self._is_balanced(root.left)
        if not is_bal_l:
            return False, -1
        is_bal_r, height_r = self._is_balanced(root.right)
        if not is_bal_r:
            return False, -1
        return abs(height_l-height_r) <= 1, max(height_l, height_r)+1

    def isBalanced(self, root):
        '''Returns True if and only if root is a height-balanced binary tree.

        O(n) time
        O(log(n)) space
        '''
        return self._is_balanced(root)[0]
