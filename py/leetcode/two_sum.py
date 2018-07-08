class Solution(object):
    def twoSum(self, a, k):
        for i, x in enumerate(a):
            for j in range(i+1, len(a)):
                if x+a[j] == k:
                    return [i, j]
        raise ValueError('I was promised an input with a positive result!')
