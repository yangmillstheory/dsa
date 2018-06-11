class Solution(object):
    def _walk(self, root):
        if not root:
            return 0
        l_max_sum = self._walk(root.left)
        r_max_sum = self._walk(root.right)
        # by design, the return values always include
        # root's value, hence, we can always try extending
        max_disjoint_path = max(
            root.val+max(l_max_sum, r_max_sum), root.val)
        self._max = max(self._max, max_disjoint_path, l_max_sum+r_max_sum+root.val)
        # never return the connected path!
        return max_disjoint_path

    def maxPathSum(self, root):
        '''Find the maximum of *all* paths, not just root-to-leaf.

            T(n) = O(n)
            S(n) = O(n)
        '''
        self._max = float('-inf')
        self._walk(root)
        return self._max
