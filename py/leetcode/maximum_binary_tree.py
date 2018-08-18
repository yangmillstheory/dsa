class Solution(object):
    def constructMaximumBinaryTree(self, a):
        # T(n) = O(n^2)
        # S(n) = O(n)
        def dfs(lo, hi):
            if lo > hi:
                return
            v, i = max((a[i], i) for i in range(lo, hi+1))
            root = TreeNode(v)
            root.left, root.right = dfs(lo, i-1), dfs(i+1, hi)
            return root
        return dfs(0, len(a)-1)

    def _linear_time(self, a):
        # T(n) = O(n)
        # S(n) = O(n)
        stack = []
        for x in a:
            node = TreeNode(x)
            while stack and stack[-1].val < x:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
