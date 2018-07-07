def in_order(tree):
    stack = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            yield tree.val
            tree = tree.right


class Solution(object):
    def kthSmallest(self, root, k):
        '''Finds the kth smallest value in a BST in O(h+k) time.'''
        it = in_order(root)
        for _ in range(k-1):
            next(it)
        return next(it)
