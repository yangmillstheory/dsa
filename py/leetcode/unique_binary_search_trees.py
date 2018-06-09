def _n_trees(start, end, memo):
    if (start, end) in memo:
        return memo[(start, end)]
    if start > end:
        return 1
    count = 0
    for j in range(start, end+1):
        count += _n_trees(start, j-1, memo)*_n_trees(j+1, end, memo)
    memo[(start, end)] = count
    return count


class Solution:
    def numTrees(self, n):
        return _n_trees(1, n, {})
