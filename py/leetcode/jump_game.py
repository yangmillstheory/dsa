class Solution(object):
    def canJump(self, a):
        best = float('-inf')
        for i, jump in enumerate(a):
            if best != float('-inf') and i > best:
                return False
            if i+jump >= len(a)-1:
                return True
            best = max(best, i+jump)
        raise ValueError(a)
