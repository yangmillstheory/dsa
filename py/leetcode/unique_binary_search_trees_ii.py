def _gen_trees(start, end):
    if start > end:
        yield None
    for j in range(start, end+1):
        for l_tree in _gen_trees(start, j-1):
            for r_tree in _gen_trees(j+1, end):
                root = TreeNode(j)
                root.left = l_tree
                root.right = r_tree
                yield root


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return list(_gen_trees(1, n))
