import math


class Solution:
    def numSquares(self, n):
        # T(n) = O(n*sqrt(n))
        # S(n) = O(n)
        # oddly this is TLE in Python3, but 62th percentile in Python2
        dp = [0]+([float('inf')]*n)
        pows = [pow(j, 2) for j in range(int(math.sqrt(n)+1))]
        sqrt = [int(math.sqrt(i)) for i in range(n+1)]
        for i in range(1, n+1):
            dp[i] = 1 + min(
                dp[i-pows[j]]
                for j in range(sqrt[i], 0, -1))
        return dp[-1]
