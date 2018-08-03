class Solution:
    def robUnoptimized(self, xs):
        '''Robbing a house in O(n) time and O(n) space.'''
        if not xs:
            return 0
        n = len(xs)
        dp = [0 for _ in range(n)]
        for j in range(n):
            cont = xs[j]
            if j >= 2:
                cont += dp[j-2]
            stop = dp[j-1] if j >= 1 else 0
            dp[j] = max(cont, stop)
        return dp[-1]

    def rob(self, xs):
        '''Robbing a house in O(n) time and O(1) space.'''
        a, b = 0, 0
        for i, x in enumerate(xs):
            a, b = b, max(x+a, b)
        return b
