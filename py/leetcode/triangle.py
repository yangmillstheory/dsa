class Solution(object):
    def min_path_sum_dp_1(self, tri):
        # T(m,n) = S(m,n) = O(m*n)
        m = len(tri)
        dp = [[None]*len(tri[i]) for i in range(m)]
        dp[0][0] = tri[0][0]
        for i in range(1, m):
            n = len(tri[i])
            for j in range(n):
                cand = []
                if j > 0:
                    cand.append(tri[i][j]+dp[i-1][j-1])
                if j < n-1:
                    cand.append(tri[i][j]+dp[i-1][j])
                dp[i][j] = min(cand)
        return min(dp[-1])

    def minimumTotal(self, tri):
        # T(m,n) = O(m*n)
        # S(m,n) = O(n)
        m, prev = len(tri), [tri[0][0]]
        for i in range(1, m):
            n = len(tri[i])
            curr = [None]*n
            for j in range(n):
                cand = []
                if j > 0:
                    cand.append(tri[i][j]+prev[j-1])
                if j < n-1:
                    cand.append(tri[i][j]+prev[j])
                curr[j] = min(cand)
            prev = curr
        return min(prev)
