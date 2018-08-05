class Solution(object):
    def _h_index_slow(self, a):
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

    def _h_index_fast(self, a):
        # T(n) = O(n)
        # S(n) = O(1)
        h, n = float('-inf'), len(a)

        def partition(i, j):
            '''Returns an index p where a[i:j+1] is partitioned around p.'''
            a[i], a[j] = a[j], a[i]
            p = i
            for k in range(i, j):
                if a[k] <= a[j]:
                    a[p], a[k] = a[k], a[p]
                    p += 1
            a[p], a[j] = a[j], a[p]
            return p
        lo, hi = 0, n-1
        while lo <= hi:
            p = partition(lo, hi)
            if a[p] < n-p:
                lo = p+1
            else:
                h = max(h, n-p)
                hi = p-1
        return h if h != float('-inf') else 0

    def hIndex(self, a):
        return self._h_index_fast(a)
