class Solution:
    def _subsets(self, xs, i):
        '''Returns a tuple which is the list of subsets, and the count of newly added subsets.'''
        if i == -1:
            return [[]], 0
        prev, m = self._subsets(xs, i-1)
        copy = prev[:]
        n = 0
        for j, subset in enumerate(copy):
            if i and xs[i] == xs[i-1] and j < len(copy)-m:
                continue
            prev.append(subset + [xs[i]])
            n += 1
        return prev, n

    def subsetsWithDup(self, xs):
        xs.sort()
        return self._subsets(xs, len(xs)-1)[0]


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
    print(Solution().subsetsWithDup([1, 1, 1]))
