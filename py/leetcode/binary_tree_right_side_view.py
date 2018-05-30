import collections


NodeWithDepth = collections.namedtuple('NodeWithDepth', ['node', 'depth'])


class Solution(object):
    def rightSideView(self, root):
        '''Right-side view of a binary tree in O(n) time and O(h) space.'''
        view = []
        seen = {}
        pair = NodeWithDepth(root, 1)
        stack = collections.deque()
        while stack or pair.node:
            if pair.node:
                if pair.depth not in seen:
                    view.append(pair.node.val)
                seen[pair.depth] = True
                if pair.node.left:
                    stack.append(NodeWithDepth(pair.node.left, pair.depth+1))
                pair = NodeWithDepth(pair.node.right, pair.depth+1)
            else:
                pair = stack.pop()
        return view
