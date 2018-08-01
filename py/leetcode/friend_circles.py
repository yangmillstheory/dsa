def n_circles(g):
    # T(n) = O(n^2)
    # S(n) = O(n)
    d = len(g)
    n, cur, rem = 0, set(), set(range(d))
    while rem:
        n += 1
        cur.add(rem.pop())
        while cur:
            i = cur.pop()
            for j, is_friend in enumerate(g[i]):
                if is_friend and j in rem:
                    cur.add(j)
                    rem.remove(j)
    return n


class Solution(object):
    def findCircleNum(self, g):
        return n_circles(g)
