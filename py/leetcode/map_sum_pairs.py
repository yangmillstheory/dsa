from collections import defaultdict, deque


class MapSum:

    def __init__(self):
        self.children = defaultdict(self.__class__)
        self.val = 0

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self
        for ch in key:
            node = node.children[ch]
        node.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        res = 0
        q = deque()
        q.append(node)
        while q:
            node = q.popleft()
            res += node.val
            for _, child in node.children.items():
                q.append(child)
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
