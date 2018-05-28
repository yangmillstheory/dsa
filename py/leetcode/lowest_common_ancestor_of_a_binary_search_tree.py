# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        '''Find the lowest common ancestor of two nodes in
        O(log n) time and O(log n) space.
        '''
        if not root:
            return
        elif root == p or root == q:
            return root
        elif not p or not q:
            return p or q
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def lowestCommonAncestorIter(self, root, p, q):
        '''Find the lowest common ancestor of two nodes in
        O(log n) time and O(1) space.
        '''
        while root:
            if root == p or root == q:
                return root
            elif not p or not q:
                return p or q
            elif max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                break
        return root
