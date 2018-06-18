class Solution(object):
    def maxProduct(self, xs):
        prev_min_prod = prev_max_prod = 1
        min_prod, max_prod = float('inf'), float('-inf')
        for x in xs:
            # can extend previous min, or extend previous max, or start a new subarray product;
            # we want to track previous minima to account for the case when x is negative
            cands = [
                prev_min_prod*x,
                prev_max_prod*x,
                x,
            ]
            prev_min_prod, prev_max_prod = min(*cands), max(*cands)
            min_prod, max_prod = min(min_prod, prev_min_prod), max(max_prod, prev_max_prod)
        return max_prod
