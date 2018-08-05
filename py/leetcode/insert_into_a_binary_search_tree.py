class Solution(object):
    def insertIntoBST(self, root, x):
        prev, curr = None, root
        while curr:
            prev = curr
            if curr.val < x:
                curr = curr.right
            else:
                curr = curr.left
        if prev:
            if prev.val < x:
                prev.right = TreeNode(x)
            else:
                prev.left = TreeNode(x)
        else:
            root = TreeNode(x)
        return root
