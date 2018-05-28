# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, query, partial_sum=0, cur=None, res=None):
        '''Find all root-to-leaf paths that sum to query in
        O(n) time and O(h) space.'''
        if res is None:
            res = []
        if cur is None:
            cur = []
        if not root:
            return res
        l, r, val = root.left, root.right, root.val
        partial_sum += val
        cur.append(val)
        if l is None and r is None and partial_sum == query:
            res.append(list(cur))
        self.pathSum(l, query, partial_sum, cur, res)
        self.pathSum(r, query, partial_sum, cur, res)
        cur.pop()
        partial_sum -= val
        return res
