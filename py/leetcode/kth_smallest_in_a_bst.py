import collections


class Solution:
    def kthSmallest(self, root, k):
        '''In-order traversal to return the kth smallest node
        with T(n) = O(n) and S(n) = O(h).
        '''
        stack = collections.deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if not k:
                    return root
                root = root.right
