class Solution:
    def swap(self, xs, i, j):
        xs[i], xs[j] = xs[j], xs[i]

    def permute(self, xs, i=0, res=None):
        if res is None:
            res = []
        if xs is None:
            return res
        n = len(xs)
        if i >= n:
            res.append(xs[:])
        else:
            for j in range(i, n):
                self.swap(xs, i, j)
                self.permute(xs, i+1, res)
                self.swap(xs, i, j)
        return res
