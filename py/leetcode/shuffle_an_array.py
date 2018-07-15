from random import randint


class Solution(object):
    def __init__(self, a):
        self._orig = [x for x in a]
        self._a = a

    def reset(self):
        self._a = [x for x in self._orig]
        return self._a

    def shuffle(self):
        n, a = len(self._a), self._a
        for i in range(n):
            j = randint(i, n-1)
            a[i], a[j] = a[j], a[i]
        return a
