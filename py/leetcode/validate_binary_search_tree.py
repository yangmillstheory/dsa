class Solution(object):
    def isValidBST(self, root, key_min=float('-inf'), key_max=float('inf')):
        # T(n) = S(n) = O(n)
        if not root:
            return True
        l, r, val = root.left, root.right, root.val
        if val <= key_min or val >= key_max:
            return False
        return self.isValidBST(l, key_min, min(key_max, val)) and self.isValidBST(r, max(key_min, val), key_max)
