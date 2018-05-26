class Solution:
    def removeDuplicates(self, xs):
        if not xs:
            return 0
        w = 1
        for j, x in enumerate(xs[1:]):
            if x != xs[j]:
                xs[w] = x
                w += 1
        return w


if __name__ == '__main__':
    s = Solution()

    xs = [1, 1, 2]
    n = s.removeDuplicates(xs)
    assert n == 2, n
    assert xs[:n] == [1, 2], xs[:n]

    xs = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    n = s.removeDuplicates(xs)
    assert n == 5, n
    assert xs[:n] == [0, 1, 2, 3, 4], xs[:n]
