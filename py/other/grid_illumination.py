def solve(n, lamps):
    '''Solve the grid illumination problem.

        T(n, l) = O(l)
        S(n, l) = O(n)
    '''
    rows = [False for _ in range(n)]
    cols = [False for _ in range(n)]
    pos_diags = [False for _ in range((2*n)-1)]
    neg_diags = [False for _ in range((2*n)-1)]
    for i, j in lamps:
        rows[i] = True
        cols[j] = True
        pos_diags[i+j] = True
        neg_diags[n-1+i-j] = True
    return lambda x, y: rows[x] or cols[y] or pos_diags[x+y] or neg_diags[n-1+x-y]


if __name__ == '__main__':
    dim = 6
    is_lit = solve(dim, [(0, 0), (2, 3), (1, 5)])

    for i in range(dim):
        for j in range(dim):
            if (i, j) in [(3, 1), (5, 2), (5, 4)]:
                assert not is_lit(i, j)
            else:
                assert is_lit(i, j)

    is_lit = solve(dim, [(2, 3), (1, 5)])

    for i in range(dim):
        for j in range(dim):
            if (i, j) in [(0, 0), (0, 2), (3, 0), (3, 1), (4, 0), (4, 4), (5, 2), (5, 4)]:
                assert not is_lit(i, j)
            else:
                assert is_lit(i, j)
