class Solution(object):
    def PredictTheWinner(self, a):
        memo = {}
        def max_profit(i, j):
            if i > j:
                return 0
            key = (i, j)
            if key not in memo:
                if j-i <= 1:
                    memo[key] = max(a[k] for k in range(i, j+1))
                else:
                    memo[key] = max(
                        a[i] + min(max_profit(i+2, j), max_profit(i+1, j-1)),
                        a[j] + min(max_profit(i, j-2), max_profit(i+1, j-1))
                    )
            return memo[key]
        n = len(a)
        return max_profit(0, n-1) >= min(max_profit(1, n-1), max_profit(0, n-2))
