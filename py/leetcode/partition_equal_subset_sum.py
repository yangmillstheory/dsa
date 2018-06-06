class Solution:
    def canPartition(self, xs):
        if not xs:
            return True
        n, s = len(xs), sum(xs)
        if s % 2 != 0:
            return False
        s //= 2
        dp = [False for _ in range(s+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(s, xs[i-1]-1, -1):
                dp[j] |= dp[j-xs[i-1]]
        return dp[s]
