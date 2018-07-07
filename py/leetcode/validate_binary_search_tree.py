from collections import deque


class Solution(object):
    def _preorder(self, tree, key_min=float('-inf'), key_max=float('inf')):
        # T(n) = S(n) = O(n)
        if not tree:
            return True
        l, r, val = tree.left, tree.right, tree.val
        if val <= key_min or val >= key_max:
            return False
        return self._preorder(l, key_min, min(key_max, val)) and self._preorder(r, max(key_min, val), key_max)

    def _inorder(self, tree):
        stack, prev = [], float('-inf')
        while stack or tree:
            if tree:
                stack.append(tree)
                tree = tree.left
            else:
                tree = stack.pop()
                if tree.val <= prev:
                    return False
                prev = tree.val
                tree = tree.right
        return True

    def _bfs(self, tree):
        if not tree:
            return True
        q = deque([(tree, float('-inf'), float('inf'))])
        while q:
            tree, key_min, key_max = q.popleft()
            l, r, val = tree.left, tree.right, tree.val
            if val <= key_min or val >= key_max:
                return False
            if l:
                q.append((l, key_min, min(key_max, val)))
            if r:
                q.append((r, max(key_min, val), key_max))
        return True

    def isValidBST(self, root):
        return self._bfs(root)
