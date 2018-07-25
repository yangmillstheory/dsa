_prev_0_curr_0 = 0, 0
_prev_0_curr_1 = 0, 1
_prev_1_curr_0 = 1, 0
_prev_1_curr_1 = 1, 1


def read(g, i, j):
    if isinstance(g[i][j], tuple):
        return g[i][j]
    return g[i][j], g[i][j]


def write(g, i, j, curr):
    prev = read(g, i, j)[0]
    if not prev and not curr:
        g[i][j] = _prev_0_curr_0
    elif prev and not curr:
        g[i][j] = _prev_1_curr_0
    elif curr and not prev:
        g[i][j] = _prev_0_curr_1
    else:
        g[i][j] = _prev_1_curr_1


def n_adj(g, i, j):
    m, n = len(g), len(g[0])
    s = 0
    for di, dj in [
        [-1, +1],
        [-1, -1],
        [-1, 0],
        [0, +1],
        [0, -1],
        [+1, +1],
        [+1, -1],
        [+1, 0],
    ]:
        if min(i+di, j+dj) >= 0 and i+di < m and j+dj < n and read(g, i+di, j+dj)[0]:
            s += 1
    return s


class Solution(object):
    def _game_of_life_optimized(self, g):
        # T(m, n) = O(m*n) (2 passes)
        # S(m, n) = O(1)
        if not g or not g[0]:
            return
        m, n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                s = n_adj(g, i, j)
                if read(g, i, j)[0]:
                    if s < 2 or s > 3:
                        write(g, i, j, 0)
                elif s == 3:
                    write(g, i, j, 1)
        for i in range(m):
            for j in range(n):
                g[i][j] = read(g, i, j)[1]

    def gameOfLife(self, g):
        return self._game_of_life_optimized(g)


if __name__ == '__main__':
    s = Solution()
    g = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(g)
    import pprint
    pprint.pprint(g)
