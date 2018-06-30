class Vertex(object):
    white, gray, black = range(3)

    def __init__(self, i):
        self.i = i
        self.prereqs = []
        self.color = Vertex.white

    def __repr__(self):
        return '({}, {}, {})'.format(self.i, self.color, [d.i for d in self.prereqs])


class Solution(object):
    def canFinish(self, n, prereqs):
        # T(n, p) = S(n, p) = O(n + |p|)
        def _build_graph():
            g = [Vertex(i) for i in range(n)]
            for i, d in prereqs:
                g[i].prereqs.append(g[d])
            return g
        g = _build_graph()

        def has_cycle(v):
            if v.color == Vertex.gray:
                return True
            v.color = Vertex.gray
            found = True
            for d in v.prereqs:
                if d.color != Vertex.black and has_cycle(d):
                    break
            else:
                found = False
            v.color = Vertex.black
            return found
        return not any(has_cycle(v) for v in g)
