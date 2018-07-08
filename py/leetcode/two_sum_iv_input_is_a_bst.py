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


def _in_order(tree):
    stack = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            yield tree
            tree = tree.right


class Solution(object):
    def findTarget(self, tree, k):
        '''Answer the Two-Sum query in O(h) time and O(h) space.'''
        if not tree:
            return False
        fwd, rev = _in_order(tree), _rev_order(tree)
        lo, hi = next(fwd), next(rev)
        while lo != hi:
            cand = lo.val + hi.val
            if cand < k:
                lo = next(fwd)
            elif cand > k:
                hi = next(rev)
            else:
                return True
        return False
