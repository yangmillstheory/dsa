import collections

_MaxProfit = collections.namedtuple('_MaxProfit', ['incl', 'excl'])


class Solution(object):
    def rob(self, root):
        def _max_profit(node):
            if not node:
                return _MaxProfit(0, 0)
            max_profit_l = _max_profit(node.left)
            max_profit_r = _max_profit(node.right)
            max_profit_incl = max_profit_l.excl + max_profit_r.excl + node.val
            max_profit_excl = max(max_profit_l) + max(max_profit_r)
            return _MaxProfit(incl=max_profit_incl, excl=max_profit_excl)
        return max(*_max_profit(root))
