class Vertex(object):
    w, g, b = range(3)

    def __init__(self, i):
        self.i = i
        self.prereqs = []
        self.color = Vertex.w

    def __repr__(self):
        return '({}, {}, {})'.format(self.i, self.color, [d.i for d in self.prereqs])


class Solution(object):
    def canFinish(self, n, prereqs):
        def _build_graph():
            g = [Vertex(i) for i in range(n)]
            for i, d in prereqs:
                g[i].prereqs.append(g[d])
            return g
        g = _build_graph()

        def has_cycle(v):
            if v.color == Vertex.g:
                return True
            v.color = Vertex.g
            found = True
            for d in v.prereqs:
                if d.color != Vertex.b and has_cycle(d):
                    break
            else:
                found = False
            v.color = Vertex.b
            return found
        return not any(has_cycle(v) for v in g)
