class Solution:
    def subsets(self, xs):
        return self._subsets(xs, len(xs)-1)

    def _subsets(self, xs, i):
        if i == -1:
            return [[]]
        prev = self._subsets(xs, i-1)
        for subset in prev[:]:
            prev.append(subset + [xs[i]])
        return prev
