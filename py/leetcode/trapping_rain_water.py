class Solution(object):
    def trap(self, hs):
        # T(n) = S(n) = O(n)
        if not hs:
            return 0
        n, res = len(hs), 0
        l_heights = [hs[0]] + [float('-inf') for _ in range(n-1)]
        r_heights = [float('-inf') for _ in range(n-1)] + [hs[-1]]
        for i in range(1, n):
            if hs[i] < l_heights[i-1]:
                l_heights[i] = l_heights[i-1]
            elif hs[i] < hs[i-1]:
                l_heights[i] = hs[i-1]
        for i in range(n-2, -1, -1):
            if hs[i] < r_heights[i+1]:
                r_heights[i] = r_heights[i+1]
            elif hs[i] < hs[i+1]:
                r_heights[i] = hs[i+1]
        for i in range(1, n-1):
            l_height, r_height = l_heights[i], r_heights[i]
            if r_height != float('-inf') and l_height != float('-inf'):
                res += min(r_height, l_height)-hs[i]
        return res
