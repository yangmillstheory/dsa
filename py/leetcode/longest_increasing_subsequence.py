class Solution(object):
    def lengthOfLIS(self, a):
        # T(n) = O(n^2)
        # S(n) = O(n)
        if not a:
            return 0
        n = len(a)
        # dp[i] is the length of a max LIS ending at a[i]
        dp = [1]*n
        for i in range(n):
            dp[i] = max([dp[j]+1 for j in range(i) if a[j] < a[i]] + [1])
        return max(dp)
