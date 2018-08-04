class Solution:
    def rob(self, houses):
        def rob_straight(lo, hi):
            a, b = 0, 0
            for i in range(lo, hi+1):
                a, b = b, max(houses[i]+a, b)
            return b
        n = len(houses)
        if n == 0:
            return 0
        if n <= 2:
            return max(houses)
        return max(rob_straight(0, n-2), rob_straight(1, n-1))
