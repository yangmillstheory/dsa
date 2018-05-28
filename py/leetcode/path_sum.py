# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, query, partial_sum=0):
        '''Determine whether or not a root-to-leaf path exists with
        sum query in O(n) time and O(h) space.
        '''
        if not root:
            return False
        partial_sum += root.val
        l, r = root.left, root.right
        if partial_sum == query and not l and not r:
            return True
        return self.hasPathSum(l, query, partial_sum) or self.hasPathSum(r, query, partial_sum)
