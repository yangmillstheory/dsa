class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph(self, v):
        clones = {}

        def _clone(t):
            if t is None:
                return None
            if t in clones:
                return clones[t]
            clone = clones.setdefault(t, UndirectedGraphNode(t.label))
            for u in t.neighbors:
                clone.neighbors.append(clones.get(u) or _clone(u))
            return clone
        return _clone(v)
