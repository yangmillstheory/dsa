def find_maximum_subarray(a):
    prev, max_seen = 0, float('-inf')
    for x in a:
        prev = max(prev+x, x)
        max_seen = max(prev, max_seen)
    return max(max_seen, 0)


def buy_and_sell_stock_once(prices):
    return find_maximum_subarray((prices[i]-prices[i-1] for i in range(1, len(prices))))


class Solution(object):
    def maxProfit(self, prices):
        return buy_and_sell_stock_once(prices)
