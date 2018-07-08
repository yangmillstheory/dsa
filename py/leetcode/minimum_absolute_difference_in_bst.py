def tree_min(tree):
    while tree and tree.left:
        tree = tree.left
    return tree


def tree_max(tree):
    while tree and tree.right:
        tree = tree.right
    return tree


def min_max_index(tree, min_ind=None, max_ind=None):
    if not tree:
        return min_ind, max_ind
    if min_ind is None:
        min_ind = {None: float('inf')}
    if max_ind is None:
        max_ind = {None: float('-inf')}
    min_max_index(tree.left, min_ind, max_ind)
    min_max_index(tree.right, min_ind, max_ind)
    min_ind[tree] = min(min_ind[tree.left], min_ind[tree.right], tree.val)
    max_ind[tree] = max(max_ind[tree.left], max_ind[tree.right], tree.val)
    return min_ind, max_ind


class Solution(object):
    def _recursive(self, tree, min_ind, max_ind):
        '''Get the minimum absolute difference between any two nodes in a BST in
        T(n) = O(n) time and O(h) space.

        This relies on a prebuilt index of subtree minima and maxima, indexed by node;
        in tests, this is actually slower than calling tree_min and tree_max per node.
        '''
        if not tree:
            return float('inf')
        l, r, val = tree.left, tree.right, tree.val
        cands = []
        if l:
            cands.append(abs(val-max_ind[l]))
        if r:
            cands.append(abs(val-min_ind[r]))
        cands.append(self._recursive(l))
        cands.append(self._recursive(r))
        return min(*cands)

    def getMinimumDifference(self, tree):
        return self._recursive(tree, *min_max_index(tree))
