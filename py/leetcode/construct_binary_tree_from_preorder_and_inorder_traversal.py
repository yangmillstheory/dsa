# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        '''Recover a binary tree in O(n) time and O(h) space.'''
        index = {x: i for i, x in enumerate(inorder)}
        m, n = len(preorder), len(inorder)

        def _build_tree(pre_a, pre_b, in_a, in_b):
            if pre_a > pre_b or in_a > in_b:
                return None
            data = preorder[pre_a]
            root_index = index[data]
            root = TreeNode(data)
            root.left = _build_tree(pre_a+1, pre_a+(root_index-in_a), in_a, root_index-1)
            root.right = _build_tree(pre_a+(root_index-in_a)+1, pre_b, root_index+1, in_b)
            return root
        return _build_tree(0, m-1, 0, n-1)
