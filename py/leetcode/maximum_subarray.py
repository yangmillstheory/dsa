class Solution(object):
    def maxSubArray(self, xs):
        prev, max_seen = 0, float('-inf')
        for x in xs:
            prev = max(prev+x, x)
            max_seen = max(prev, max_seen)
        return max_seen
