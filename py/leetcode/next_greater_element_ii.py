class Solution(object):
    def _with_shift(self, a):
        # T(n) = O(n) (2 iterations)
        # S(n) = O(n) (list of size n)
        n = len(a)
        res = [-1]*n
        prev_max_right = []
        for j in range(2*n-2, -1, -1):
            i = min(j-n, j)
            if a[i] < a[i+1]:
                res[i] = a[i+1]
                prev_max_right.append(a[i+1])
            else:
                max_right = -1
                while prev_max_right and prev_max_right[-1] <= a[i]:
                    prev_max_right.pop()
                if prev_max_right:
                    max_right = prev_max_right[-1]
                else:
                    prev_max_right.append(a[i])
                res[i] = max_right
        return res

    def _without_shift(self, a):
        # T(n) = O(n) (2*n iterations)
        # S(n) = O(n) (list of size 2*n)
        m = len(a)
        n = 2*m
        a += a
        res = [-1]*n
        prev_max_right = []
        for j in range(n-2, -1, -1):
            if a[j] < a[j+1]:
                res[j] = a[j+1]
                prev_max_right.append(a[j+1])
            else:
                max_right = -1
                while prev_max_right and prev_max_right[-1] <= a[j]:
                    prev_max_right.pop()
                if prev_max_right:
                    max_right = prev_max_right[-1]
                else:
                    prev_max_right.append(a[j])
                res[j] = max_right
        return res[:m]

    def nextGreaterElements(self, a):
        return self._with_shift(a)
