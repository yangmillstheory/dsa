# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        '''Find the lowest common ancestor of two nodes in
        O(n) time and O(log n) space.
        '''
        if not root:
            return
        if root == p:
            return p
        if root == q:
            return q
        lca_l = self.lowestCommonAncestor(root.left, p, q)
        lca_r = self.lowestCommonAncestor(root.right, p, q)
        if lca_l and lca_r:
            return root
        return lca_l or lca_r
