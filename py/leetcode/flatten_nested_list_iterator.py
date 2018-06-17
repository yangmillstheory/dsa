_sentinel = object()


class NestedIterator(object):
    def __init__(self, nested_list):
        self._stack = [(nested_list, 0)]

    def _peek(self):
        while self._stack:
            root, i = self._stack.pop()
            if i >= len(root):
                continue
            ch = root[i]
            if ch.isInteger():
                self._stack.append((root, i))
                return root, i
            else:
                self._stack.append((root, i+1))
                self._stack.append((ch.getList(), 0))
        return _sentinel, None

    def next(self):
        root, i = self._peek()
        self._stack.pop()
        self._stack.append((root, i+1))
        return root[i]

    def hasNext(self):
        return self._peek()[0] is not _sentinel


class NestedIteratorEager(object):
    def __init__(self, nested_list):
        self._flat_list = self._flatten(nested_list)
        self._j = 0

    def _flatten(self, nested_list):
        res, stack = [], [(nested_list, 0)]
        while stack:
            root, i = stack.pop()
            if i >= len(root):
                continue
            ch = root[i]
            stack.append((root, i+1))
            if ch.isInteger():
                res.append(ch)
            else:
                stack.append((ch.getList(), 0))
        return res

    def hasNext(self):
        return self._j < len(self._flat_list)

    def next(self):
        x = self._flat_list[self._j]
        self._j += 1
        return x
