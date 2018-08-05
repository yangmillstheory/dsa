class Solution(object):
    def hIndex(self, a):
        # T(n) = O(n*log(n))
        # S(n) = O(1)
        a.sort()
        h, n = float('-inf'), len(a)
        lo, hi = 1, n
        while lo <= hi:
            m = lo+(hi-lo)//2
            if a[n-m] < m:
                hi = m-1
            else:
                h = max(h, m)
                lo = m+1
        return h if h != float('-inf') else 0
