class Solution:
    def partition(self, xs, lo, hi):
        mid = lo + (hi-lo)//2
        xs[mid], xs[hi] = xs[hi], xs[mid]
        # invariant:
        #
        #   xs[j] <= xs[hi] for all j <= i
        #   xs[j] >  xs[hi] for all j >  i
        i = lo
        for j in range(lo, hi):
            if xs[j] <= xs[hi]:
                xs[j], xs[i] = xs[i], xs[j]
                i += 1
        xs[i], xs[hi] = xs[hi], xs[i]
        return i

    def findKthLargest(self, xs, k):
        '''kth largest element in O(n) time and O(1) space.'''
        n = len(xs)
        lo, hi = 0, n-1
        while lo <= hi:
            p = self.partition(xs, lo, hi)
            if p == n-k:
                return xs[p]
            elif p < n-k:
                lo = p+1
            else:
                hi = p-1
        raise ValueError(xs, k)


if __name__ == '__main__':
    x = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert x == 5, x

    x = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    assert x == 4, x
