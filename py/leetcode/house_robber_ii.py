class Solution:
    def rob(self, houses):
        n = len(houses)
        if n == 0:
            return 0
        if n <= 2:
            return max(houses)
        a = b = c = d = 0
        best = 0
        for i, x in enumerate(houses):
            if i < n-1:
                a, b = b, max(houses[i]+a, b)
            if i > 0:
                c, d = d, max(houses[i]+c, d)
            best = max(best, b, d)
        return best
