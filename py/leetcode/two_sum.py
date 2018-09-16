import collections


class Solution(object):
    def twoSum(self, a, q):
        # T(n) = O(n)
        # S(n) = O(n)
        ind = {x: i for i, x in enumerate(a)}
        for i, x in enumerate(a):
            if q-x in ind and ind[q-x] != i:
                return [i, ind[q-x]]
