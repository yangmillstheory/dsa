class Solution(object):
    def intersection(self, nums1, nums2):
        # O(max(m, n)) time
        # O(max(m, n)) space
        res = []
        seen = {x: False for x in nums2}
        for x in nums1:
            if x in seen and not seen[x]:
                res.append(x)
                seen[x] = True
        return res
