from collections import deque


class StackEmpty(Exception):
    pass


class MyStack(object):

    def __init__(self):
        '''Stack implementation with

            T(n) = O(1) (push)
            T(n) = O(n) (pop)
            T(n) = O(1) (top)
            T(n) = O(1) (empty)
            S(n) = O(n)
        '''
        self._p = deque()
        self._q = deque()

    def push(self, x):
        if self._p:
            self._p.append(x)
        else:
            self._q.append(x)

    def pop(self):
        if self._p:
            return self._xfer_from_to(self._p, self._q)
        return self._xfer_from_to(self._q, self._p)

    def _xfer_from_to(self, from_q, to_q):
        while len(from_q) > 1:
            to_q.append(from_q.popleft())
        return from_q.popleft()

    def top(self):
        if self._p:
            return self._p[-1]
        if self._q:
            return self._q[-1]
        raise StackEmpty

    def empty(self):
        return not self._p and not self._q


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())
    print(obj.pop())
    print(obj.empty())
