import collections
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def _count_linked_list(self, head):
        n_nodes = 0
        node = head
        while node:
            n_nodes += 1
            node = node.next
        return n_nodes

    def sortedListToBST(self, head):
        '''Convert a sorted linked list to a complete binary
        tree in O(n) time and O(log n) space.
        '''
        if not head:
            return
        self.head = head
        self._build_tree(0, self._count_linked_list(head))

    def _build_tree(self, lo, hi):
        if lo > hi:
            return
        mid = lo + (hi-lo)//2
        node = TreeNode(0)
        node.left = self._build_tree(lo, mid-1)
        node.val = self.head.val
        self.head = self.head.next
        node.right = self._build_tree(mid+1, hi)
        return node


class Solution:
    def _get_complete_tree(self, n_nodes):
        if not n_nodes:
            return
        root = TreeNode(0)
        n_nodes -= 1
        q = collections.deque((root,))
        while q:
            node = q.popleft()
            if n_nodes:
                node.left = TreeNode(0)
                n_nodes -= 1
                q.append(node.left)
            if n_nodes:
                node.right = TreeNode(0)
                n_nodes -= 1
                q.append(node.right)
            if not n_nodes:
                break
        return root

    def _in_order_iter(self, root):
        stack = collections.deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                yield root
                root = root.right

    def _count_linked_list(self, head):
        n_nodes = 0
        node = head
        while node:
            n_nodes += 1
            node = node.next
        return n_nodes

    def sortedListToBST(self, head):
        '''Convert a sorted linked list to a complete binary
        tree in O(n) time and O(n) space.
        '''
        if not head:
            return
        root = self._get_complete_tree(self._count_linked_list(head))
        for node in self._in_order_iter(root):
            node.val = head.val
            head = head.next
        return root


