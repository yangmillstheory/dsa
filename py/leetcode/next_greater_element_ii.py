class Solution(object):
    def nextGreaterElements(self, a):
        # T(n) = S(n) = O(n)
        m = len(a)
        n = 2*m
        a += a
        res = [-1]*n
        if not a:
            return res
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
