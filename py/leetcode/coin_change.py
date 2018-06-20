class Solution(object):
    def __init__(self):
        self.n = float('inf')

    def coinChange(self, xs, target):
        # T(n,t) = O(n*t)
        # S(n,t) = O(t)
        dp = [0]+([float('inf')]*target)
        for i in range(1, target+1):
            cands = [
                dp[i-x] for x in xs
                if i-x >= 0
            ]
            if cands:
                dp[i] = min(cands)+1
        return -1 if dp[-1] == float('inf') else dp[-1]

    def _coin_change_recursive(self, xs, target, j, n):
        if target == 0:
            self.n = min(self.n, n)
        elif target < 0 or j == -1 or self.n < n:
            return
        else:
            x = xs[j]
            for freq in range(target/x, -1, -1):
                if freq+n > self.n:
                    break
                self._coin_change_recursive(xs, target-(freq*x), j-1, freq+n)

    def coin_change_recursive(self, xs, target):
        xs.sort()
        self._coin_change_recursive(xs, target, len(xs)-1, 0)
        return -1 if self.n == float('inf') else self.n


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 100))
