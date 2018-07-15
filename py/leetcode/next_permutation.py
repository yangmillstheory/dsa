def reverse(a, lo, hi):
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]
        lo += 1
        hi -= 1


class Solution(object):
    def nextPermutation(self, a):
        n = len(a)
        for j in range(n-1, 0, -1):
            if a[j] > a[j-1]:
                k = j
                break
        else:
            reverse(a, 0, n-1)
            return
        for j in range(n-1, k-1, -1):
            if a[j] > a[k-1]:
                i = j
                break
        else:
            raise ValueError(a)
        a[i], a[k-1] = a[k-1], a[i]
        reverse(a, k, n-1)
