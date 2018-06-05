def subsets(n, k):
    assert 0 <= k <= n
    res, cand = [], []

    def _subsets(start):
        if len(cand) == k:
            res.append(cand[:])
        else:
            for j in range(start, n):
                cand.append(j)
                _subsets(j+1)
                cand.pop()
    _subsets(0)
    return res


if __name__ == '__main__':
    import pprint
    pprint.pprint(subsets(3, 3))
    pprint.pprint(subsets(3, 2))
    pprint.pprint(subsets(3, 1))
    pprint.pprint(subsets(3, 0))
