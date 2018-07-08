class Solution(object):
    def twoSum(self, a, k):
        lo, hi = 0, len(a)-1
        while lo < hi:
            cand = a[lo]+a[hi]
            if cand < k:
                lo += 1
            elif cand > k:
                hi -= 1
            else:
                # dumb that the return indices aren't zero-based
                return [lo+1, hi+1]
        raise ValueError('I was promised an input with a positive result!')
