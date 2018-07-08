import bisect


class Solution(object):
    def twoSum(self, a, k):
        for i, x in enumerate(a):
            for j in range(i+1, len(a)):
                if x+a[j] == k:
                    return [i, j]
        raise ValueError


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
