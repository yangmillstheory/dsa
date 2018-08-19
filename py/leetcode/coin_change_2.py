class Solution(object):
    def _change_recursive(self, amt, coins, j, memo):
        if amt == 0:
            return 1
        if min(amt, j) < 0:
            return 0
        if (amt, j) not in memo:
            memo[(amt, j)] = (
                self._change_recursive(amt, coins, j-1, memo) +
                self._change_recursive(amt-coins[j], coins, j, memo)
            )
        return memo[(amt, j)]

    def change_recursive(self, amt, coins):
        return self._change_recursive(amt, coins, len(coins)-1, {})

    def change_dp_1(self, amt, coins):
        # T(a, c) = O(a*c)
        # S(a, c) = O(a*c)
        if amt == 0:
            return 1
        if not coins:
            return 0
        n_coins = len(coins)
        memo = [
            [1]+([0]*amt)
            for _ in range(n_coins)
        ]
        for i in range(n_coins):
            for j in range(1, amt+1):
                memo[i][j] = memo[i-1][j] + (memo[i][j-coins[i]] if j-coins[i] >= 0 else 0)
        return memo[-1][-1]

    def change(self, amt, coins):
        # T(a, c) = O(a*c)
        # S(a, c) = O(c)
        if amt == 0:
            return 1
        if not coins:
            return 0
        n_coins = len(coins)
        memo = [1]+([0]*amt)
        for i in range(n_coins):
            for j in range(1, amt+1):
                memo[j] += memo[j-coins[i]] if j-coins[i] >= 0 else 0
        return memo[-1]
