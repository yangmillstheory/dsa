import collections


class LRUCache(object):

    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key):
        if key not in self._cache:
            return -1
        val = self._cache[key]
        self._cache.move_to_end(key, last=False)
        return val

    def put(self, key, val):
        self._cache[key] = val
        self._cache.move_to_end(key, last=False)
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=True)
