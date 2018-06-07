class Solution:
    def _walk(self, root):
        if not root:
            return 0, 0
        l_diam, l_depth = self._walk(root.left)
        r_diam, r_depth = self._walk(root.right)
        return max(l_diam, r_diam, l_depth+r_depth), max(l_depth, r_depth)+1

    def diameterOfBinaryTree(self, root):
        '''T(n) = S(n) = O(n) time algorithm to find the diameter of a binary tree.'''
        return self._walk(root)[0]
