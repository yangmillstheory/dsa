class Solution(object):
    def _change_recursive(self, amt, coins, j, memo):
        if amt == 0:
            return 1
        if min(amt, j) < 0:
            return 0
        if (amt, j) not in memo:
            memo[(amt, j)] = self._change_recursive(amt, coins, j-1) + self._change_recursive(amt-coins[j], coins, j)
        return memo[(amt, j)]

    def change_recursive(self, amt, coins):
        return self._change_recursive(amt, coins, len(coins)-1)

    def change_dp_1(self, amt, coins):
        # T(a, c) = S(a, c) = O(a*c)
        if amt == 0:
            return 1
        if not coins:
            return 0
        n_coins = len(coins)
        prev = [1]+([0]*amt)
        curr = [1]+([0]*amt)
        for i in range(n_coins):
            for j in range(1, amt+1):
                incl_c_i = curr[j-coins[i]] if j-coins[i] >= 0 else 0
                excl_c_i = prev[j] if i-1 >= 0 else 0
                curr[j] = incl_c_i+excl_c_i
            prev = curr
            curr = [1]*([0]*amt)
        return curr[-1]

    def change(self, amt, coins):
        # T(a, c) = O(a*c)
        # S(a, c) = O(c)
        if amt == 0:
            return 1
        if not coins:
            return 0
        n_coins = len(coins)
        prev = [1]+([0]*amt)
        curr, init = [1]+([0]*amt), True
        for i in range(n_coins):
            if not init:
                curr = [1]+([0]*amt)
            for j in range(1, amt+1):
                incl_c_i = curr[j-coins[i]] if j-coins[i] >= 0 else 0
                excl_c_i = prev[j] if i-1 >= 0 else 0
                curr[j] = incl_c_i+excl_c_i
            prev, init = curr, False
        return curr[-1]

