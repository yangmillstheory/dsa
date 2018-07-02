class Solution(object):
    def maxSubArray(self, xs, thing=None):
        # prev is the maximum sum ending at x of "previous iteration";
        # we can extend it or start a new maximum sum beginning at x
        prev, max_seen = 0, float('-inf')
        for x in xs:
            prev = max(prev+x, x)
            max_seen = max(prev, max_seen)
        return max_seen
