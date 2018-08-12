class Solution(object):
    def _trap_ugly(self, a):
        # T(n) = S(n) = O(n)
        if not a:
            return 0
        n, res = len(a), 0
        l_heights = [a[0]] + [float('-inf') for _ in range(n-1)]
        r_heights = [float('-inf') for _ in range(n-1)] + [a[-1]]
        for i in range(1, n):
            if a[i] < l_heights[i-1]:
                l_heights[i] = l_heights[i-1]
            elif a[i] < a[i-1]:
                l_heights[i] = a[i-1]
        for i in range(n-2, -1, -1):
            if a[i] < r_heights[i+1]:
                r_heights[i] = r_heights[i+1]
            elif a[i] < a[i+1]:
                r_heights[i] = a[i+1]
        for i in range(1, n-1):
            l_height, r_height = l_heights[i], r_heights[i]
            if r_height != float('-inf') and l_height != float('-inf'):
                res += min(r_height, l_height)-a[i]
        return res

    def trap(self, a):
        i, j = 0, len(a)-1
        max_l, max_r, area = float('-inf'), float('-inf'), 0
        while i < j:
            if a[i] < a[j]:
                if a[i] < max_l:
                    area += max_l-a[i]
                else:
                    max_l = a[i]
                i += 1
            else:
                if a[j] < max_r:
                    area += max_r-a[j]
                else:
                    max_r = a[j]
                j -= 1
        return area
