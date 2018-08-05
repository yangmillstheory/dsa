import collections
import operator


def inorder_it(root):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            yield node.val
            root = node.right


class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        counter = collections.Counter(inorder_it(root))
        _, max_count = counter.most_common(1)[0]
        res = []
        for val, count in counter.most_common():
            if count != max_count:
                break
            res.append(val)
        return res
