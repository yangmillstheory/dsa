class Solution(object):
    def containsNearbyDuplicate(self, a, k):
        # T(n) = O(n)
        # S(n) = O(n)
        ind = {}
        for i, x in enumerate(a):
            if x in ind and 0 < abs(i-ind[x]) <= k:
                return True
            ind[x] = i
        return False
