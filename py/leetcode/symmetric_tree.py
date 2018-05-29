import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _is_symmetric(self, l, r):
        if not l and not r:
            return True
        if l and not r:
            return False
        if r and not l:
            return False
        if l.val != r.val:
            return False
        return self._is_symmetric(l.right, r.left) and \
            self._is_symmetric(l.left, r.right)

    def isSymmetricRecursive(self, root):
        return self._is_symmetric(root.left, root.right)

    def isSymmetric(self, root):
        '''Determine whether or not a binary tree is symmetric.
        This takes O(n) time and O(log n) space.'''
        if not root:
            return True
        q = collections.deque()
        q.append((root.left, root.right))
        while q:
            l, r = q.popleft()
            if not l and not r:
                continue
            if l and not r:
                return False
            if r and not l:
                return False
            if l.val != r.val:
                return False
            q.append((l.right, r.left))
            q.append((l.left, r.right))
        return True
