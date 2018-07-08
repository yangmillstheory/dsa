def tree_min(tree):
    while tree and tree.left:
        tree = tree.left
    return tree


def tree_max(tree):
    while tree and tree.right:
        tree = tree.right
    return tree


class Solution(object):
    def getMinimumDifference(self, tree):
        '''Get the minimum absolute difference between any two nodes in a BST in
        T(n) = O(n*2^n) time and O(h) space.
        '''
        if not tree:
            return float('inf')
        l, r, val = tree.left, tree.right, tree.val
        cands = []
        if l:
            cands.append(abs(val-tree_max(l).val))
        if r:
            cands.append(abs(val-tree_min(r).val))
        cands.append(self.getMinimumDifference(l))
        cands.append(self.getMinimumDifference(r))
        return min(*cands)
