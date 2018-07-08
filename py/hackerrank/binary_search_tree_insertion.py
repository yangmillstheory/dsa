class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, info):
        # T(n) = O(h)
        # S(n) = O(1)
        root = self.root
        prev = None
        while root:
            prev = root
            if root.info == info:
                break
            elif root.info < info:
                root = root.right
            else:
                root = root.left
        node = Node(info)
        if prev:
            if prev.info < info:
                prev.right = node
            else:
                prev.left = node
        if not self.root:
            self.root = node
        return self.root
