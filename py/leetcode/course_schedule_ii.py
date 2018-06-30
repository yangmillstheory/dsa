class Vertex(object):
    white, gray, black = range(3)

    def __init__(self, i):
        self.i = i
        self.prereqs = []
        self.color = Vertex.white


class Solution(object):
    def findOrder(self, n, prereqs):
        # T(n, p) = S(n, p) = O(n + |p|)
        def _build_graph():
            g = [Vertex(i) for i in range(n)]
            for i, d in prereqs:
                g[i].prereqs.append(g[d])
            return g
        g = _build_graph()

        def has_cycle(v, res):
            if v.color == Vertex.gray:
                return True
            v.color, _has_cycle = Vertex.gray, False
            for d in v.prereqs:
                if d.color != Vertex.black and has_cycle(d, res):
                    _has_cycle = True
                    break
            else:
                res.append(v.i)
            v.color = Vertex.black
            return _has_cycle
        res = []
        if any(has_cycle(v, res) for v in g if v.color != Vertex.black):
            return []
        return res
