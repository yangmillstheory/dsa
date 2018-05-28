# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _to_BST(self, xs, lo, hi):
        if lo > hi:
            return None
        mid = int(lo + (hi-lo)/2)
        root = TreeNode(xs[mid])
        root.left = self._to_BST(xs, lo, mid-1)
        root.right = self._to_BST(xs, mid+1, hi)
        return root

    def sortedArrayToBST(self, xs):
        '''Convert a sorted array to a BST in O(n) time and O(log n) space.'''
        return self._to_BST(xs, 0, len(xs)-1)
