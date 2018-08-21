class Solution(object):
    def integerBreak(self, n):
        dp = [1]*(n+1)
        for j in range(2, n+1):
            for i in range(2, j):
                x = max(dp[i], i)
                y = max(dp[j-i], j-i)
                dp[j] = max(dp[j], x*y)
        return dp[-1]
