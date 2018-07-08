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
    def _iterative(self, tree, min_ind, max_ind):
        # T(n) = O(n)
        # S(n) = O(h)
        res, stack = float('inf'), []
        while stack or tree:
            if tree:
                l, r, val = tree.left, tree.right, tree.val
                cands = [res]
                if l:
                    cands.append(abs(val-max_ind[l]))
                if r:
                    cands.append(abs(val-min_ind[r]))
                    stack.append(r)
                res = min(cands)
                tree = tree.left
            else:
                tree = stack.pop()
        return res

    def _recursive(self, tree, min_ind, max_ind):
        # T(n) = O(n)
        # S(n) = O(h)
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

    def _in_order(self, tree):
        # T(n) = O(n)
        # S(n) = O(h)
        def it(tree):
            stack = []
            while stack or tree:
                if tree:
                    stack.append(tree)
                    tree = tree.left
                else:
                    tree = stack.pop()
                    yield tree
                    tree = tree.right
        res, prev = float('inf'), None
        for node in it(tree):
            if prev:
                res = min(res, abs(node.val-prev.val))
            prev = node
        return res

    def getMinimumDifference(self, tree):
        # return self._iterative(tree, *min_max_index(tree))
        return self._in_order(tree)
