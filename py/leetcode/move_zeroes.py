class Solution(object):
    def moveZeroes(self, xs):
        # T(n) = O(n)
        k = i = 0
        n = len(xs)
        while i < n:
            if xs[i] != 0:
                xs[k], xs[i] = xs[i], xs[k]
                while k < n and xs[k] != 0:
                    k += 1
                if k == n:
                    return
                i = k+1
            else:
                i += 1
