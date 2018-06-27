class Solution:
    def majorityElement(self, nums):
        count, last = 0, None
        for x in nums:
            if count == 0:
                last, count = x, 1
            elif last == x:
                count += 1
            else:
                count -= 1
        return last
