class Solution(object):
    def convertBST(self, root):
        '''Convert a BST to a Greater Tree in O(n) time and O(h) space.'''
        def _rev_order(tree):
            stack = []
            while stack or tree:
                if tree:
                    stack.append(tree)
                    tree = tree.right
                else:
                    tree = stack.pop()
                    yield tree
                    tree = tree.left
        prev = 0
        for tree in _rev_order(root):
            tree.val += prev
            prev = tree.val
        return root
