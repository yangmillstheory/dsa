# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, q, partial=0, is_start=True):
        '''Return the count of all paths in the binary tree (not
        necessarily root-to-leaf) that sum to q.

        This runs in exponential time and O(h) space.

        FIXME optimize this!
        '''
        n = 0
        if not root:
            return n
        l, r, val = root.left, root.right, root.val
        partial += val
        if partial == q:
            n += 1
        n += self.pathSum(l, q, partial, False)
        n += self.pathSum(r, q, partial, False)
        if is_start:
            n += self.pathSum(l, q, partial=0, is_start=True)
            n += self.pathSum(r, q, partial=0, is_start=True)
        return n
