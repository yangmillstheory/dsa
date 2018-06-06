class Solution:
    def removeDuplicates(self, xs):
        if not xs:
            return 0
        last, w = xs[0], 1
        for i in range(1, len(xs)):
            if xs[i] > last:
                last = xs[w] = xs[i]
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
