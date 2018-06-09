class BSTIterator(object):
    def __init__(self, root):
        self._root = root
        self._stack = []

    def _fill_stack(self):
        while self._root:
            self._stack.append(self._root)
            self._root = self._root.left

    def hasNext(self):
        if (not self._stack) and self._root:
            self._fill_stack()
        return bool(self._stack)

    def next(self):
        if (not self._stack) and self._root:
            self._fill_stack()
        node = self._stack.pop()
        self._root = node.right
        return node.val
