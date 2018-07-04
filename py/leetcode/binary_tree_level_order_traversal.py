from collections import deque, namedtuple

NodeWithDepth = namedtuple('NodeWithDepth', ['node', 'depth'])


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        # T(n) = S(n) = O(n)
        #
        # note that this works for
        #
        #   https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
        #
        # as well
        levels = []
        if not root:
            return levels
        q = deque([NodeWithDepth(root, 0)])
        while q:
            node, depth = q.popleft()
            if len(levels) == depth:
                levels.append([])
            levels[depth].append(node.val)
            if node.left:
                q.append(NodeWithDepth(node.left, depth+1))
            if node.right:
                q.append(NodeWithDepth(node.right, depth+1))
        return levels
