import bisect


class Solution(object):
    def length_of_lis_dp(self, xs):
        # T(n) = O(n^2)
        # S(n) = O(n)
        if not xs:
            return 0
        n = len(xs)
        # dp[i] is the length of a max LIS ending at xs[i]
        dp = [1]*n
        for i in range(n):
            dp[i] = max([dp[j]+1 for j in range(i) if xs[j] < xs[i]] + [1])
        return max(dp)

    def lengthOfLIS(self, xs):
        # T(n) = O(n*log n)
        # S(n) = O(n)
        # see http://qr.ae/TUp4ph
        lis = []
        for x in xs:
            i = bisect.bisect_left(lis, x)
            if i == len(lis):
                lis.append(x)
            else:
                lis[i] = x
        return len(lis)
