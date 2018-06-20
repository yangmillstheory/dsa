class Solution(object):
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


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 100))
