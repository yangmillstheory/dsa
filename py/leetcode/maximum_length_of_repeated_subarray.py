class Solution:
    def find_length_brute_force(self, a, b):
        # O(n^4) solution
        n = len(a)
        max_len = 0
        for i in range(n):
            for j in range(i+1, n+1):
                sub_a = a[i:j]
                for k in range(n-j+i+1):
                    if sub_a == b[k:k+j-i]:
                        max_len = max(max_len, j-i)
        return max_len

    def find_length_dp_1(self, a, b):
        # T(n) = O(n^2)
        # S(n) = O(n^2)
        n = len(a)
        max_len = 0
        # memo[i][j] is the solution for the subproblem on a[:i] and b[:j]
        memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if a[i-1] == b[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                    max_len = max(max_len, memo[i][j])
        return max_len

    def findLength(self, a, b):
        # T(n) = O(n^2)
        # S(n) = O(n)
        n = len(a)
        max_len = 0
        memo = [
            [0 for _ in range(n+1)],  # results from previous iteration
            [0 for _ in range(n+1)],
        ]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if a[i-1] == b[j-1]:
                    memo[1][j] = memo[0][j-1] + 1
                    max_len = max(max_len, memo[1][j])
                else:
                    memo[1][j] = 0
            for j in range(1, n+1):
                memo[0][j] = memo[1][j]
        return max_len
