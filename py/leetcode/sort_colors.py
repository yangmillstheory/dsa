def swap(xs, i, j):
    xs[i], xs[j] = xs[j], xs[i]


class Solution:
    def sortColors(self, xs):
        i = k = 0
        j = len(xs)-1
        while k <= j:
            if xs[k] == 2:
                swap(xs, k, j)
                j -= 1
            elif xs[k] == 1:
                k += 1
            else:
                swap(xs, i, k)
                i += 1
                k += 1


if __name__ == '__main__':
    s = Solution()

    xs = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    s.sortColors(xs)
    assert xs == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

    xs = [0, 1, 2, 0, 1, 2]
    s.sortColors(xs)
    assert xs == [0, 0, 1, 1, 2, 2]
