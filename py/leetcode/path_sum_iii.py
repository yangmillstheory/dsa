import collections

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

        This runs in O(h) space and O(n*log n) to O(n^2) time (see https://leetcode.com/problems/path-sum-iii/discuss/91889/Simple-Java-DFS).
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

    def __init__(self):
        # memo of partial sums seen so far
        self.dp = collections.defaultdict(int)
        self.dp[0] = 1
        self.n = 0

    def pathSum2(self, root, q):
        '''Runs in O(n) time and O(n) space.'''
        def depth_first_walk(node, q, partial):
            if not node:
                return
            l, r, val = node.left, node.right, node.val
            partial += val
            self.n += self.dp[partial-q]
            self.dp[partial] += 1
            depth_first_walk(l, q, partial)
            depth_first_walk(r, q, partial)
            self.dp[partial] -= 1

        depth_first_walk(root, q, 0)
        return self.n
