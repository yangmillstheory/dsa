import itertools


def T(depth, n):
    for j in range(depth, n-depth-1):
        yield depth, j


def R(depth, n):
    for i in range(depth, n-depth-1):
        yield i, -depth-1


def B(depth, n):
    for j in reversed(range(depth+1, n-depth)):
        yield -depth-1, j


def L(depth, n):
    for i in reversed(range(depth+1, n-depth)):
        yield i, depth


def spiral_it(n):
    m = n//2
    it = itertools.chain.from_iterable(
        itertools.chain(T(depth, n), R(depth, n), B(depth, n), L(depth, n))
        for depth in range(m)
    )
    if n % 2:
        it = itertools.chain(it, [(m, m)])
    return it


class Solution(object):
    def generateMatrix(self, n):
        res = [
            [None]*n
            for _ in range(n)
        ]
        for k, (i, j) in enumerate(spiral_it(n)):
            res[i][j] = pow(k+1, 2)
        return res
