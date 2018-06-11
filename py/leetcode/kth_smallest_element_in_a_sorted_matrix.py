from heapq import heappop, heappush

VISITING = object()


class Solution(object):
    def kthSmallest(self, g, k):
        if not g or not g[0]:
            raise ValueError
        n = len(g)
        heap = [(g[0][0], (0, 0))]
        g[0][0] = VISITING
        for _ in range(k-1):
            x, (i, j) = heappop(heap)
            if i+1 < n and g[i+1][j] != VISITING:
                heappush(heap, (g[i+1][j], (i+1, j)))
                g[i+1][j] = VISITING
            if j+1 < n and g[i][j+1] != VISITING:
                heappush(heap, (g[i][j+1], (i, j+1)))
                g[i][j+1] = VISITING
            g[i][j] = x
        return heappop(heap)[0]
