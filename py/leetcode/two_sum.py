import collections


class Solution(object):
    def twoSum(self, a, q):
        # T(n) = O(n)
        # S(n) = O(n)
        ind = collections.defaultdict(set)
        for i, x in enumerate(a):
            ind[x].add(i)
        for i, x in enumerate(a):
            if q-x not in ind:
                continue
            j = ind[q-x].pop()
            if j != i:
                return [i, j]
            elif ind[q-x]:
                return [i, ind[q-x].pop()]
