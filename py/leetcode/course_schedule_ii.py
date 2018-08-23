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

        def has_cycle(u, res):
            if u.color == Vertex.gray:
                return True
            u.color = Vertex.gray
            for w in u.prereqs:
                if w.color != Vertex.black and has_cycle(w, res):
                    return True
            res.append(u.i)
            u.color = Vertex.black
            return False
        res = []
        for v in g:
            if v.color == Vertex.white and has_cycle(v, res):
                return []
        return res
