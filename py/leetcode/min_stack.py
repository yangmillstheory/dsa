class MinStack(object):
    '''An O(1) time and O(n) space min-stack.'''

    def __init__(self):
        self._mins = []
        self._vals = []

    def push(self, x):
        _max = self._mins[-1] if self._mins else float('inf')
        if x <= _max:
            self._mins.append(x)
        self._vals.append(x)

    def pop(self):
        x = self._vals.pop()
        if self._mins and self._mins[-1] == x:
            self._mins.pop()
        return x

    def top(self):
        return self._vals[-1]

    def getMin(self):
        return self._mins[-1] if self._mins else None
