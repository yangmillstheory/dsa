class Solution(object):
    def numDecodings(self, s):
        memo, n = {}, len(s)

        def n_decodings_from(start):
            if start in memo:
                return memo[start]
            if start == n:
                return 1
            count = 0
            for j in range(start, n):
                m = int(s[start:j+1])
                if m < 1 or m > 26:
                    break
                count += n_decodings_from(j+1)
            memo[start] = count
            return count
        return n_decodings_from(0)
