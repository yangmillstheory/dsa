# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def connect(self, root, right=None):
        '''Populate right siblings of a perfect binary tree in
        O(n) time and O(h) space.
        '''
        if not root:
            return
        root.nextf = right
        self.connect(root.left, root.right)
        self.connect(root.right, getattr(right, 'left', None))
        return root

    def connectIter(self, root):
        '''Populate right siblings of a perfect binary tree in
        O(n) time and O(1) space.
        '''
        while root:
            node = root
            while node:
                if node.left:
                    node.left.next = node.right
                if node.right:
                    node.right.next = getattr(node.next, 'left', None)
                node = node.next
            root = root.left
