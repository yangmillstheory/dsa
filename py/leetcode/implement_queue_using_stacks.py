class MyQueue(object):
    def __init__(self):
        self._push_stack = []
        self._pop_stack = []

    def push(self, x):
        # T(n) = O(1)
        self._push_stack.append(x)

    def pop(self):
        # T(n) = O(n)
        self._ensure_pop_stack()
        return self._pop_stack.pop()

    def peek(self):
        # T(n) = O(n)
        self._ensure_pop_stack()
        return self._pop_stack[-1]

    def _ensure_pop_stack(self):
        if not self._pop_stack:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())

    def empty(self):
        # T(n) = O(1)
        return not self._push_stack and not self._pop_stack
