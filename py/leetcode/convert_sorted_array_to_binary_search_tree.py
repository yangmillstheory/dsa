# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _to_BST(self, a, lo, hi):
        if lo > hi:
            return None
        mid = int(lo + (hi-lo)/2)
        root = TreeNode(a[mid])
        root.left = self._to_BST(a, lo, mid-1)
        root.right = self._to_BST(a, mid+1, hi)
        return root

    def _iterative(self, a):
        root, stack = None, [(0, len(a)-1, None, None)]
        while stack:
            lo, hi, l_parent, r_parent = stack.pop()
            if lo > hi:
                continue
            mid = lo + (hi-lo)//2
            node = TreeNode(a[mid])
            root = root or node
            if l_parent:
                l_parent.right = node
            if r_parent:
                r_parent.left = node
            stack.append((lo, mid-1, None, node))
            stack.append((mid+1, hi, node, None))
        return root

    def sortedArrayToBST(self, a):
        '''Convert a sorted array to a BST in O(n) time and O(log n) space.'''
        # return self._to_BST(a, 0, len(a)-1)
        return self._iterative(a)
